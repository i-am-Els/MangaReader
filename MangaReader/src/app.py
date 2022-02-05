from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QSize
import sys, setup, ctypes

def setTaskBarIcon():
    myappid = u"mycompany.myproduct.subproduct.version" # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

if __name__ == "__main__":
    app = QApplication([])
    setTaskBarIcon()
    appWindow = QMainWindow()
    stWindow = setup.Window()
    appWindow.setCentralWidget(stWindow)
    appWindow.setWindowIcon(stWindow.windowIcon)

    appWindow.min_screen_width = 915
    appWindow.min_screen_height = 515
    appWindow.resize_width = 1092
    appWindow.resize_height = 614
    appWindow.appWindowTitle = "Manhua Reader"
    appWindow.resize(QSize(appWindow.resize_width, appWindow.resize_height))
    appWindow.setMinimumSize(QSize(appWindow.min_screen_width, appWindow.min_screen_height))
    appWindow.setWindowTitle(appWindow.appWindowTitle)
    appWindow.showMaximized()
    sys.exit(app.exec())