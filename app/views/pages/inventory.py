from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame,QSizePolicy
from PyQt6.QtCore import Qt

class Stock(QWidget):
    def __init__(self, parent = None ):
        super().__init__(parent)
        self.stock_layout= QVBoxLayout(self)
        self.stock_layout.setContentsMargins(0,0,0,0)
        self.stock_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.stock_layout.setSpacing(0)
        ##
        self.top_frame()
    
    def top_frame(self):
        frame = QFrame(self)
        frame.setObjectName("top_frames")
        frame.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Preferred)
        frame.setMinimumHeight(60)
        ##
        title_layout = QHBoxLayout(frame)

        # عنوان
        self.title_lb = QLabel("مدیریت گدام", frame)
        self.title_lb.setObjectName("title")
        #
        self.semi_title= QLabel("/ لیست اجناس، نمایش و کنترل موجودی ها",frame)
        self.semi_title.setObjectName("semi_title")
        self.semi_title.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Preferred)
        ##
        title_layout.addStretch(1)
        title_layout.addWidget(self.semi_title, alignment= Qt.AlignmentFlag.AlignRight)
        title_layout.addWidget(self.title_lb, alignment=Qt.AlignmentFlag.AlignRight)
        title_layout.setSpacing(6)
        ##
        self.stock_layout.addWidget(frame)
        return frame
