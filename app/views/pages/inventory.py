from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame,QSizePolicy,QPushButton,QLineEdit
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtGui import QIcon,QPixmap
##components
from app.components.top_widget import TopWidget
from app.components.stock_widget import StockFrame
## ViewModel
from app.viewmodels.stock_viewmodel import Stock_ViewModel


class Stock(QWidget):
    def __init__(self, parent = None ):
        super().__init__(parent)
        self.stock_layout= QVBoxLayout(self)
        self.stock_layout.setContentsMargins(0,0,0,0)
        self.stock_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.stock_layout.setSpacing(0)
        ##top_widget
        self.top_widget= TopWidget(
            title="مدیریت گدام",
            sub_title="/ لیست اجناس، نمایش و کنترل موجودی ها")
        self.stock_layout.addWidget(self.top_widget)
        ##
        self.stock_widget= StockFrame()
        middle_layout= QHBoxLayout()
        middle_layout.addWidget(self.stock_widget,2)
        middle_layout.setContentsMargins(20,20,20,20)
        ##
        self.stock_layout.addLayout(middle_layout)
        ##viewmodel
        self.vm= Stock_ViewModel(self)