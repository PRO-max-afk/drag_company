from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame,QSizePolicy,QPushButton,QLineEdit
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtGui import QIcon,QPixmap
from app.components.top_widget import TopWidget

class Dashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.dash_layout = QVBoxLayout(self)
        self.dash_layout.setContentsMargins(0,0,0,0)
        self.dash_layout.setSpacing(0)
        self.dash_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.top_widget = TopWidget(
            title= "داشبورد",
            sub_title="/ روزنامچه، مدیریت فروش، گزارشات کلی و...")
        self.dash_layout.addWidget(self.top_widget)