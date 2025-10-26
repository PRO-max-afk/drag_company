from PyQt6.QtWidgets import QApplication
import sys
from app.viewmodels.main_viewmodel import MainViewModel
from app.views.mainwindow import MainWindow

def main():
    app= QApplication(sys.argv)
    ##veiw model
    vm= MainViewModel()
    ##view
    window= MainWindow(vm)
    window.show()
    
    sys.exit(app.exec())

if __name__== "__main__":
    main()


