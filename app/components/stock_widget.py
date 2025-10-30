from PyQt6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame,
    QSizePolicy, QPushButton, QComboBox,QTableWidget,QHeaderView,QAbstractItemView,QTableWidgetItem)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap

from app.core.img import AssetManager

class StockFrame(QFrame):
    def __init__(self):
        super().__init__()

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setObjectName("middle_frames")

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setSpacing(20)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.assets= AssetManager()
        self.top_items()
        self.table_UI()
        self.Button_UI()


    def top_items(self):
        top_layout = QHBoxLayout()
        top_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        top_layout.setContentsMargins(0, 0, 0, 0)

        self.title_lb = QLabel("لیست اجناس", self)
        self.title_lb.setObjectName("title_frame")
        self.title_lb.setMaximumHeight(40)

        self.category_combo = QComboBox(self)
        self.category_combo.setObjectName("drop_down")
        items = ["همه", "مسکن"]
        self.category_combo.addItems(items)
        self.category_combo.setFixedSize(80,35)
        self.category_combo.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        ##
        self.add_btn= QPushButton(self)
        self.add_btn.setText("افزودن جنس جدید  ")
        icon= QIcon(self.assets.get_asset_path("add.svg"))
        self.add_btn.setIcon(icon)
        self.add_btn.setObjectName("add_btn")
        self.add_btn.setIconSize(QSize(12,12))
        self.add_btn.setFixedSize(156,31)
        self.add_btn.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        ##
        top_layout.addWidget(self.add_btn,alignment=Qt.AlignmentFlag.AlignLeft)
        top_layout.addStretch(1)
        top_layout.addWidget(self.category_combo, alignment=Qt.AlignmentFlag.AlignRight)
        top_layout.addWidget(self.title_lb, alignment=Qt.AlignmentFlag.AlignRight)
        ##
        middle_layout= QVBoxLayout()
        #
        self.stock_table= QTableWidget(self)
        ##
        self.btn_layout= QHBoxLayout()
        self.btn_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        #
        self.numaric_lb= QLabel("0",self)
        self.numaric_lb.setObjectName("numaric_lb")
        #
        self.right_btn= QPushButton(self)
        self.s_right_btn= QPushButton(self)
        #
        self.left_btn= QPushButton(self)
        self.s_left_btn= QPushButton(self)
        #
        self.pages_combo = QComboBox(self)
        number = [10, 2, 3]
        self.pages_combo.addItems([str(i) for i in number])
        self.pages_combo.setObjectName("page_combo")
        self.pages_combo.setFixedSize(50,24)

        #
        middle_layout.addWidget(self.stock_table)
        middle_layout.addLayout(self.btn_layout)
        ##
        self.main_layout.addLayout(top_layout)
        self.main_layout.addLayout(middle_layout)
    ##
    def table_UI(self):
        self.stock_table.setColumnCount(6)
        self.stock_table.setHorizontalHeaderLabels(["نام جنس","کد محصول","وضعیت","دسته بندی","قیمت","عملیه ها"])
        header= self.stock_table.horizontalHeader()
        header.setDefaultAlignment(Qt.AlignmentFlag.AlignRight)
        self.stock_table.verticalHeader().setVisible(False)
        self.stock_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.stock_table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.stock_table.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.stock_table.setAlternatingRowColors(True)
        self.stock_table.setObjectName("table")
        
        for i in range(self.stock_table.columnCount()):
            if i == 0:
                header.setSectionResizeMode(i, QHeaderView.ResizeMode.Stretch)
            else:
                header.setSectionResizeMode(i, QHeaderView.ResizeMode.ResizeToContents)
    ##
    def Button_UI(self):
        button_info= [
            (self.right_btn,"left.svg"),
            (self.s_right_btn,"s_left.svg"),
            (self.s_left_btn,"s_right.svg"),
            (self.left_btn,"right.svg")]

        for btn,icon in button_info:
            btn.setIcon(QIcon(self.assets.get_asset_path(icon)))
            btn.setIconSize(QSize(24,24))
            btn.setMaximumSize(24,24)
            btn.setObjectName("btn_design")
            self.btn_layout.addWidget(btn)
        self.btn_layout.insertWidget(2, self.numaric_lb,alignment=Qt.AlignmentFlag.AlignCenter)
        self.btn_layout.addWidget(self.pages_combo)




    ##
    def resizeEvent(self, event):
        path="app\\resources\\style.qss"
        with open(path,'r',encoding='utf-8') as f:
            resize_style= f.read()
        window_width = self.width()

        # --- تنظیم اندازه combobox ---
        combo_width = max(60, int(window_width * 0.08))
        combo_height = max(28, int(window_width * 0.03))
        

        # --- تنظیم اندازه و استایل دکمه ---
        if window_width < 900:  # در حالت کوچک شدن پنجره
            new_width = max(80, int(window_width * 0.15))
            new_height = max(25, int(window_width * 0.035))
            self.add_btn.setFixedSize(new_width, new_height)
            self.add_btn.setIconSize(QSize(9, 9))
            self.add_btn.setObjectName("add_btn_resize")
            self.add_btn.setStyleSheet(resize_style)
            ##
            self.category_combo.setFixedSize(combo_width, combo_height)
            self.category_combo.setObjectName("drop_down_resize")
            self.category_combo.setStyleSheet(resize_style)
            ##
            self.pages_combo.setFixedSize(25,14)
            self.pages_combo.setObjectName("page_combo_resize")
            self.pages_combo.setStyleSheet(resize_style)
            ##
            for btn in (self.right_btn,self.left_btn,self.s_right_btn,self.s_left_btn):
                btn.setIconSize(QSize(15,15))
            self.numaric_lb.setObjectName("numaric_resize")
            self.numaric_lb.setStyleSheet(resize_style)
            ##
            self.stock_table.setObjectName("table_resize")
            self.stock_table.setStyleSheet(resize_style)
            
        else:
            self.add_btn.setFixedSize(156, 31)
            self.add_btn.setIconSize(QSize(12, 12))
            self.add_btn.setObjectName("add_btn")
            self.add_btn.setStyleSheet(resize_style)
            ##
            self.category_combo.setObjectName("drop_down")
            self.category_combo.setStyleSheet(resize_style)
            self.category_combo.setFixedSize(75,33)
            ##
            self.pages_combo.setFixedSize(50,24)
            self.pages_combo.setObjectName("page_combo")
            self.pages_combo.setStyleSheet(resize_style)
            ##
            for btn in (self.right_btn,self.left_btn,self.s_right_btn,self.s_left_btn):
                btn.setIconSize(QSize(24,24))
            self.numaric_lb.setObjectName("numaric_lb")
            self.numaric_lb.setStyleSheet(resize_style)
            ##
            self.stock_table.setObjectName("table")
            self.stock_table.setStyleSheet(resize_style)

        return super().resizeEvent(event)


