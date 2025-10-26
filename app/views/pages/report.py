from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame,QSizePolicy,QPushButton,QLineEdit
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtGui import QIcon,QPixmap
from app.components.top_widget import TopWidget
from app.core.img import AssetManager

class Reports(QWidget):
    def __init__(self, parent = None ):
        super().__init__(parent)
        self.report_layout= QVBoxLayout(self)
        self.report_layout.setContentsMargins(0,0,0,0)
        self.report_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.report_layout.setSpacing(0)
        ##
        self.top_widget= TopWidget(
            title="مدیریت گزارشات",
            sub_title="/ گزارشات مختلف برای مدیریت بهتر برنامه و کسب کار شما")
        self.report_layout.addWidget(self.top_widget)