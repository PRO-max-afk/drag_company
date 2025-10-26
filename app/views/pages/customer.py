from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame,QSizePolicy,QPushButton,QLineEdit
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtGui import QIcon,QPixmap
from app.components.top_widget import TopWidget
from app.core.img import AssetManager

class Customers(QWidget):
    def __init__(self, parent = None ):
        super().__init__(parent)
        self.customer_layout= QVBoxLayout(self)
        self.customer_layout.setContentsMargins(0,0,0,0)
        self.customer_layout.setSpacing(0)
        self.customer_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        ##
        self.top_widget= TopWidget(
            title="مشتریان",
            sub_title="/ لیست مشتریان موجود، حساب ها و بیلانس مشتریان"
        )
        self.customer_layout.addWidget(self.top_widget)