from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame,QSizePolicy
from PyQt6.QtCore import Qt

class Reports(QWidget):
    def __init__(self, parent = None ):
        super().__init__(parent)
        self.report_layout= QVBoxLayout(self)
        self.report_layout.setContentsMargins(0,0,0,0)
        self.report_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.report_layout.setSpacing(0)
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
        self.title_lb = QLabel("مدیریت گزارشات", frame)
        self.title_lb.setObjectName("title")
        #
        self.semi_title= QLabel("/ گزارشات مختلف برای مدیریت بهتر برنامه و کسب کار شما",frame)
        self.semi_title.setObjectName("semi_title")
        self.semi_title.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Preferred)
        ##
        title_layout.addStretch(1)
        title_layout.addWidget(self.semi_title, alignment= Qt.AlignmentFlag.AlignRight)
        title_layout.addWidget(self.title_lb, alignment=Qt.AlignmentFlag.AlignRight)
        title_layout.setSpacing(6)
        ##
        self.report_layout.addWidget(frame)
        return frame
