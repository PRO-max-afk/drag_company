from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QMainWindow,
    QStackedWidget, QPushButton, QFrame, QLabel, QSizePolicy
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QRect
from PyQt6.QtGui import QPixmap
from app.core.img import AssetManager
from app.core.font import FontLoader
from functools import partial

## pages
from .pages.dashboard import Dashboard
from .pages.sale import Sales
from .pages.customer import Customers
from .pages.inventory import Stock
from .pages.finance import Finance
from .pages.notification import Notifications
from .pages.report import Reports
from .pages.settings import Settings


class MainWindow(QMainWindow):
    def __init__(self, view_model):
        super().__init__()
        self.vm = view_model
        self.fonts = FontLoader()
        self.fonts.load_all_fonts()
        self.img = AssetManager()

        self.setWindowTitle("برنامه دوا فروشی")

        self.screen = QApplication.primaryScreen().geometry()
        self.setGeometry(self.screen.x(), self.screen.y(), self.screen.width(), self.screen.height())

        self.active_btn = None
        self.panel_width = 250
        self.panel_x = self.screen.width() - self.panel_width

        # --- ساختار اصلی ---
        main_widget = QWidget()
        self.setCentralWidget(main_widget)

        # چیدمان افقی: مرکز + پنل راست
        self.main_layout = QHBoxLayout(main_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # --- QStackedWidget ---
        self.central = QStackedWidget()
        self.main_layout.addWidget(self.central, 1)

        # --- پنل سمت راست ---
        self.side_panel = QWidget()
        self.side_panel.setObjectName("rightbar")
        self.side_panel.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        self.side_panel.setMinimumWidth(self.panel_width)

        self.main_layout.addWidget(self.side_panel)

        # ایجاد محتوای داخل پنل
        self.creating_side_panel()
        self.button_UI()
        self.label_UI()

        # افزودن صفحات
        self.added_pages()

        # اتصال سیگنال‌ها
        self.vm.current_page.connect(self.switch_page)
        self.vm.themechange.connect(self._apply_theme)

        # مقدار اولیه
        self.central.setCurrentIndex(0)
        self.active_btn = self.dashboard
        self.active_btn.setStyleSheet(self.active_style)

        # اعمال تم
        self._apply_theme(self.vm._theme)


    # -------------------------------
    def resizeEvent(self, event):
        width = self.width()
        height = self.height()
        panel_x = width - self.panel_width
        self.side_panel.setGeometry(panel_x, 0, self.panel_width, height)
        return super().resizeEvent(event)


    # -------------------------------
    def creating_side_panel(self):
        side_frame = QFrame(self.side_panel)
        side_frame.setObjectName("btnframe")
        side_frame.setMaximumSize(210, 334)

        self.top_pn_lb = QHBoxLayout()
        self.panel_layout = QVBoxLayout(side_frame)
        self.panel_layout.setContentsMargins(30,0,0,20)
        self.panel_layout.setSpacing(10)

        main_layout = QVBoxLayout(self.side_panel)
        main_layout.addSpacing(50)
        main_layout.addLayout(self.top_pn_lb)
        main_layout.addSpacing(80)
        main_layout.addWidget(side_frame, alignment=Qt.AlignmentFlag.AlignTop)
        main_layout.setContentsMargins(0, 0, 0, 0)


    # -------------------------------
    def button_UI(self):
        self.dashboard = QPushButton("داشبورد")
        self.sale_btn = QPushButton("فروشات")
        self.customer_btn = QPushButton("مشتریان")
        self.finance_btn = QPushButton("حسابداری")
        self.inventory_btn = QPushButton("مدیریت گدام")
        self.report_btn = QPushButton("گزارشات")
        self.notifi_btn = QPushButton("اطلاعیه‌ها")
        self.settings_btn = QPushButton("تنظیمات")

        btn_style_path = "app\\resources\\btn_style.qss"
        btn_style_hover = "app\\resources\\btn_change.qss"
        with open(btn_style_path, 'r', encoding='utf-8') as f:
            self.default_style = f.read()
        with open(btn_style_hover, 'r', encoding='utf-8') as f:
            self.hover_style = f.read()
        with open(btn_style_hover, 'r', encoding='utf-8') as f:
            self.active_style = f.read()

        self.buttons = [
            self.dashboard, self.sale_btn, self.customer_btn,
            self.finance_btn, self.inventory_btn, self.report_btn,
            self.notifi_btn, self.settings_btn
        ]

        for index, btn in enumerate(self.buttons):
            btn.setMaximumSize(210, 33)
            btn.setStyleSheet(self.default_style)
            btn.leaveEvent = lambda event, b=btn: (
                b.setStyleSheet(self.active_style if b == self.active_btn else self.default_style)
            )
            btn.clicked.connect(partial(self.handle_button_click, index, btn))
            self.panel_layout.addWidget(btn)


    # -------------------------------
    def label_UI(self):
        self.top_lb = QLabel("مدیریت دواخانه")
        self.top_lb.setMaximumSize(150, 40)
        self.top_lb.setObjectName("lb")

        self.icon_lb = QLabel()
        pix = QPixmap(self.img.get_asset_path("226516965_726b9247-8c91-4533-bee4-e2cd1038d4ed.svg"))
        self.icon_lb.setPixmap(pix)
        self.icon_lb.setScaledContents(True)
        self.icon_lb.setMaximumSize(50, 40)
        self.icon_lb.setObjectName("btnframe")

        self.top_pn_lb.addWidget(self.top_lb)
        self.top_pn_lb.addWidget(self.icon_lb)


    # -------------------------------
    def handle_button_click(self, index, button):
        if self.active_btn is not None and self.active_btn != button:
            self.active_btn.setStyleSheet(self.default_style)
        self.active_btn = button
        self.active_btn.setStyleSheet(self.active_style)
        self.vm.goTo(index)


    # -------------------------------
    def added_pages(self):
        self.central.addWidget(Dashboard())
        self.central.addWidget(Sales())
        self.central.addWidget(Customers())
        self.central.addWidget(Finance())
        self.central.addWidget(Stock())
        self.central.addWidget(Reports())
        self.central.addWidget(Notifications())
        self.central.addWidget(Settings())


    # -------------------------------
    def switch_page(self, index: int):
        self.central.setCurrentIndex(index)


    # -------------------------------
    def _apply_theme(self, theme: str):
        try:
            path = f'app\\resources\\{theme}_style.qss' if theme == 'dark' else 'app\\resources\\style.qss'
            with open(path, 'r', encoding='utf-8') as f:
                qss = f.read()
            self.setStyleSheet(qss)
            print(f"✅ {theme} theme applied successfully")
        except Exception as e:
            print(f"theme load failed: {e}")
