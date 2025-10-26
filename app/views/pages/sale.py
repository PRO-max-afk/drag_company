from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame,QSizePolicy,QPushButton,QLineEdit
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtGui import QIcon,QPixmap
from app.components.top_widget import TopWidget
from app.core.img import AssetManager

class Sales(QWidget):
    def __init__(self, parent = None ):
        super().__init__(parent)
        self.sale_layout= QVBoxLayout(self)
        self.sale_layout.setContentsMargins(0,0,0,0)
        self.sale_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.sale_layout.setSpacing(0)
        ##
        self.top_widget= TopWidget(
            title="فروشات",
            sub_title="/ فروش جدید، لیست فروشات اخیر، چاپ فاکتور")
        self.sale_layout.addWidget(self.top_widget)
