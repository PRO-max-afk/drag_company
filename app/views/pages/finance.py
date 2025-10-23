from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame,QSizePolicy,QPushButton,QLineEdit
from PyQt6.QtCore import Qt,QSize
from PyQt6.QtGui import QIcon,QPixmap

from app.core.img import AssetManager

class Finance(QWidget):
    def __init__(self, parent = None ):
        super().__init__(parent)
        self.finance_layout= QVBoxLayout(self)
        self.finance_layout.setContentsMargins(0,0,0,0)
        self.finance_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.finance_layout.setSpacing(0)
        ##
        self.assets= AssetManager()

        self.top_frame()
        self.Button_UI()
        self.Label_UI()
        self.Line_edit()

    def top_frame(self):
        frame = QFrame(self)
        frame.setObjectName("top_frames")
        frame.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Preferred)
        frame.setMinimumHeight(60)
        ##main layout
        title_layout = QHBoxLayout(frame)
        # عنوان
        self.title_lb = QLabel("حسابداری", frame)
        self.semi_title= QLabel("/ مدیریت درآمد و هزینه ها، مدیریت حساب بانکی و...",frame)
        #
        right_layout= QHBoxLayout()
        right_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        right_layout.addWidget(self.semi_title, alignment= Qt.AlignmentFlag.AlignRight)
        right_layout.addWidget(self.title_lb, alignment=Qt.AlignmentFlag.AlignRight)
        right_layout.setSpacing(6)
        ##دکمه ها
        self.out_btn= QPushButton(frame)
        self.notifi_btn= QPushButton(frame)
        #
        self.search_line= QLineEdit(frame)
        ##left
        left_layout= QHBoxLayout()
        left_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        left_layout.setSpacing(16)
        left_layout.addWidget(self.out_btn,alignment=Qt.AlignmentFlag.AlignLeft)
        left_layout.addWidget(self.notifi_btn,alignment= Qt.AlignmentFlag.AlignLeft) 
        left_layout.addWidget(self.search_line,alignment= Qt.AlignmentFlag.AlignLeft)
        ##
        title_layout.addLayout(left_layout)
        title_layout.addStretch(1)
        title_layout.addLayout(right_layout)
        ##
        self.finance_layout.addWidget(frame)
        return frame

    ##
    def Label_UI(self):
        self.title_lb.setObjectName("title")
        ##
        self.semi_title.setObjectName("semi_title")
        self.semi_title.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Preferred)
        ###
        search_icon= QPixmap(self.assets.get_asset_path("Vector (Stroke).svg"))
        self.search_lb= QLabel(self.search_line)
        self.search_lb.setFixedSize(12,12)
        self.search_lb.setPixmap(search_icon)
        self.search_lb.setScaledContents(True)
        self.search_lb.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.search_lb.move(self.search_line.width() - 25, (self.search_line.height() -  14) // 2)
    ##
    def Button_UI(self):
        self.out_btn.setObjectName("btn_design")
        out_icon= QIcon(self.assets.get_asset_path("Frame 18.svg"))
        self.out_btn.setIcon(out_icon)
        self.out_btn.setIconSize(QSize(20,20))
        ##
        self.notifi_btn.setObjectName("btn_design")
        notifi_icon= QIcon(self.assets.get_asset_path("Frame 17.svg"))
        self.notifi_btn.setIcon(notifi_icon)
        self.notifi_btn.setIconSize(QSize(20,20))
    ##
    def Line_edit(self):
        self.search_line.setPlaceholderText("جستجو کنید...")
        self.search_line.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Fixed)
        self.search_line.setMaximumSize(200,30)
        self.search_line.setObjectName("search_line")

    def resizeEvent(self,event ):
        window= self.width()
        min_width= int(window * 0.2)
        self.search_line.setMinimumSize(min_width,20)
        #
        icon_x= self.search_line.width() - 25
        icon_y= (self.search_line.height() - self.search_lb.height()) //2
        self.search_lb.move(icon_x,icon_y)
        return super().resizeEvent(event)