from PyQt6.QtWidgets import QApplication, QMainWindow
import sys, setup, ctypes

def setTaskBarIcon():
    myappid = u"mycompany.myproduct.subproduct.version" # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

if __name__ == "__main__":
    app = QApplication([])
    setTaskBarIcon()
    window = QMainWindow()
    stWindow = setup.Window()
    window.setCentralWidget(stWindow)
    window.setWindowIcon(stWindow.windowIcon)
    window.showMaximized()
    sys.exit(app.exec())