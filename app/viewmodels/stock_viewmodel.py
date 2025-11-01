from app.components.new_item import NewItem
import os,sys
from app.core.img import AssetManager

class Stock_ViewModel():
    def __init__(self, stock_view):
        super().__init__()
        self.view= stock_view
        self.assets= AssetManager()

        # access to the main frame(Stock_Frame)
        self.frame= self.view.stock_widget
        self.frame.add_btn.clicked.connect(self.open_add_form)
    

    
    def open_add_form(self):
        dialog= NewItem()
        file_path= "app/resources/style.qss"
        file_path= self.assets.resource_path(file_path)
        with open(file_path,'r',encoding='utf-8') as f:
            dialog.setStyleSheet(f.read())
        
        dialog.exec()