from PyQt6.QtCore import QObject,pyqtSignal

class MainViewModel(QObject):
    current_page= pyqtSignal(int)
    themechange= pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self._current_index= 0
        self._theme= "light"
    
    def current_index(self): return self._current_index
    
    def goTo(self, index:int):
        if index != self._current_index and 0 <= index <= 7:
            self._current_index= index
            self.current_page.emit(self._current_index)


    def toggleTheme(self):
        self._theme = "dark" if self._theme == "light" else "light"
        self.themechange.emit(self._theme) 
