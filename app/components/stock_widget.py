from PyQt6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QHBoxLayout, QFrame,
    QSizePolicy, QPushButton, QLineEdit)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap

from app.core.img import AssetManager

class StockFrame(QFrame):
    def __init__(self):
        super().__init__()

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setObjectName("middle_frames")

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setSpacing(20)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.top_items()


    def top_items(self):
        top_layout = QHBoxLayout()
        top_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        top_layout.setContentsMargins(0, 0, 0, 0)

        self.title_lb = QLabel("لیست اجناس", self)
        self.title_lb.setObjectName("title_frame")
        self.title_lb.setMaximumHeight(40)
        top_layout.addWidget(self.title_lb, alignment=Qt.AlignmentFlag.AlignRight)

        self.main_layout.addLayout(top_layout)

