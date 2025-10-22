from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout,QPushButton,QFrame,QHBoxLayout,QSizePolicy
from PyQt6.QtCore import Qt

class Customers(QWidget):
    def __init__(self, parent = None ):
        super().__init__(parent)
        self.customer_layout= QVBoxLayout(self)
        self.customer_layout.setContentsMargins(0,0,0,0)
        self.customer_layout.setSpacing(0)
        self.customer_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        ##
        self.top_frame()
        
    
    def top_frame(self):
        frame= QFrame(self)
        frame.setMinimumHeight(60)
        frame.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Preferred)
        frame.setObjectName("top_frames")
        
        title_layout= QHBoxLayout(frame)
        ##
        self.title_lb= QLabel("مشتریان",frame)
        self.title_lb.setObjectName("title")
        ##
        self.semi_title= QLabel("/ لیست مشتریان موجود، حساب ها و بیلانس مشتریان",frame)
        self.semi_title.setObjectName("semi_title")
        self.semi_title.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Preferred)
        ##
        title_layout.addStretch(1)
        title_layout.addWidget(self.semi_title,alignment=(Qt.AlignmentFlag.AlignRight))
        title_layout.addWidget(self.title_lb,alignment=(Qt.AlignmentFlag.AlignRight))
        title_layout.setSpacing(6)
        ##
        self.customer_layout.addWidget(frame)
        return frame

