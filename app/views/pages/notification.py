from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame,QSizePolicy,QPushButton,QLineEdit
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtGui import QIcon,QPixmap
from app.components.top_widget import TopWidget
from app.core.img import AssetManager

class Notifications(QWidget):
    def __init__(self, parent = None ):
        super().__init__(parent)
        self.notifi_layout= QVBoxLayout(self)
        self.notifi_layout.setContentsMargins(0,0,0,0)
        self.notifi_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.notifi_layout.setSpacing(0)
        ##
        self.top_widget= TopWidget(
            title="مدیریت اطلاعیه ها",
            sub_title="/ هشدار های تاریخ انقضاء و کمبود موجودی اجناس")
        self.notifi_layout.addWidget(self.top_widget)