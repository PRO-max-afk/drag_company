from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame,QSizePolicy,QPushButton,QLineEdit
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtGui import QIcon,QPixmap
from app.components.top_widget import TopWidget
from app.core.img import AssetManager

class Settings(QWidget):
    def __init__(self, parent = None ):
        super().__init__(parent)
        self.setings_layout= QVBoxLayout(self)
        self.setings_layout.setContentsMargins(0,0,0,0)
        self.setings_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setings_layout.setSpacing(0)
        ##
        self.top_widget= TopWidget(
            title="مدیریت تنظیمات",
            sub_title="/ شخصی سازی، تنظیم کاربران، بکاپ و...")
        self.setings_layout.addWidget(self.top_widget)