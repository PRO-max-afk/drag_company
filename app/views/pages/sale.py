from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout,QPushButton,QFrame,QSizePolicy,QHBoxLayout
from PyQt6.QtCore import Qt

class Sales(QWidget):
    def __init__(self, parent = None ):
        super().__init__(parent)
        self.sale_layout= QVBoxLayout(self)
        self.sale_layout.setContentsMargins(0,0,0,0)
        self.sale_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.sale_layout.setSpacing(0)
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
        self.title_lb = QLabel("فروشات", frame)
        self.title_lb.setObjectName("title")
        #
        self.semi_title= QLabel("/ فروش جدید، لیست فروشات اخیر، چاپ فاکتور",frame)
        self.semi_title.setObjectName("semi_title")
        self.semi_title.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Preferred)
        ##
        title_layout.addStretch(1)
        title_layout.addWidget(self.semi_title, alignment= Qt.AlignmentFlag.AlignRight)
        title_layout.addWidget(self.title_lb, alignment=Qt.AlignmentFlag.AlignRight)
        title_layout.setSpacing(6)
        ##
        self.sale_layout.addWidget(frame)
        return frame
