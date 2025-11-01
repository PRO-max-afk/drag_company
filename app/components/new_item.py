from PyQt6.QtWidgets import QWidget,QApplication,QDialog,QPushButton,QLabel,QVBoxLayout,QHBoxLayout,QGraphicsDropShadowEffect
from PyQt6.QtCore import Qt,QRect,QRectF,QSize
from PyQt6.QtGui import QIcon,QPainterPath,QPainter,QColor,QBrush
import sys
from app.core.img import AssetManager

class NewItem(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.Window)
        self.setObjectName("new_item")
        self.setFixedSize(500,680)
        self.center_window()
        self.assests= AssetManager() 
        

        self.main_layout= QVBoxLayout(self)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.main_layout.setSpacing(20)
        self.top_item()
        self.Button_UI()
        #QTimer.singleShot(0,self.apply_rounded_corners)
    
    def paintEvent(self, event):
        """رسم بک‌گراند گرد با آنتی‌آلیاسینگ برای گوشه‌های صاف"""
        radius = 20.0
        bg_color = QColor(255, 255, 255, 255)

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # فقط همین کافی است
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QBrush(bg_color))

        rect = QRect(0, 0, self.width(), self.height())
        path = QPainterPath()
        path.addRoundedRect(QRectF(rect), radius, radius)
        painter.drawPath(path)
        painter.end()



    
    def top_item(self):
        self.top_layout= QHBoxLayout()
        self.top_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.top_layout.setContentsMargins(10,10,10,10)
        ##
        self.top_title= QLabel("افزودن جنس جدید",self)
        self.top_title.setObjectName("item_title")
        #
        self.close_btn= QPushButton(self)
        #
        self.top_layout.addWidget(self.close_btn,alignment=Qt.AlignmentFlag.AlignLeft)
        self.top_layout.addWidget(self.top_title)

        self.main_layout.addLayout(self.top_layout)
    
    def Button_UI(self):
        close_icon= QIcon(self.assests.get_asset_path("close.svg"))
        self.close_btn.setIcon(close_icon)
        self.close_btn.setIconSize(QSize(12,12))
        self.close_btn.setObjectName("btn_design")
        self.close_btn.clicked.connect(self.close_page)
    
    def close_page(self):
        self.close()
    
    def center_window(self):
        screen= self.screen().availableGeometry()
        size= self.geometry()
        self.move(
            int((screen.width() - size.width()) / 2),
            int((screen.height() - size.height()) /2)
        )

if __name__=="__main__":
    app= QApplication(sys.argv)
    window= NewItem()
    window.show()
    sys.exit(app.exec())


