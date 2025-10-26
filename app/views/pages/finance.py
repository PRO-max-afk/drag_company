from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame,QSizePolicy,QPushButton,QLineEdit
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtGui import QIcon,QPixmap

from app.components.top_widget import TopWidget

class Finance(QWidget):
    def __init__(self, parent = None ):
        super().__init__(parent)
        self.finance_layout= QVBoxLayout(self)
        self.finance_layout.setContentsMargins(0,0,0,0)
        self.finance_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.finance_layout.setSpacing(0)
        ##
        self.top_widget= TopWidget(
            title="حسابداری",
            sub_title="/ مدیریت درآمد و هزینه ها، مدیریت حساب بانگی و...")
        self.finance_layout.addWidget(self.top_widget)