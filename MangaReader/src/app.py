from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QSizeGrip
from PyQt6.QtCore import QSize, Qt, QPoint
import sys, setup, ctypes
from themes import WindowTitleBar
from setup import MoveableWindow

def setTaskBarIcon():
    myappid = u"mycompany.myproduct.subproduct.version" # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)



if __name__ == "__main__":
    app = QApplication([])
    setTaskBarIcon()
    appWindow = MoveableWindow()
    appWindowTitleCustom = appWindow.appWindowTitle = "Manhua Reader"

    appLayout = QVBoxLayout()
    appWidget = QWidget()

    stWindow = setup.Window()
    stWindowLayout = QVBoxLayout()
    stWindowLayout.addWidget(stWindow)

    customTitleBar = WindowTitleBar(appWindow, appWindowTitleCustom, stWindow.windowIcon)

    cLayout = QVBoxLayout()
    cWidget = QWidget()
    
    cWidget.setLayout(customTitleBar)
    cLayout.addWidget(cWidget)

    cLayout.setSpacing(0)
    cWidget.setStyleSheet("QWidget{background-color: rgba(72, 75, 106, 1); color: white;}")
    appLayout.addLayout(cLayout)
    appLayout.addLayout(stWindowLayout)

    appLayout.setStretch(0, 1)
    appLayout.setStretch(1, 20)
    appLayout.setSpacing(0)

    appLayout.setContentsMargins(0,0,0,0)

    # appWidget.setLayout(appLayout)

    appWindow.setWindowIcon(stWindow.windowIcon)
    
    
    # appWindow.setCentralWidget(appWidget)
    appWindow.setLayout(appLayout)
    appWindow.setWindowFlags(Qt.WindowType.FramelessWindowHint)

    appWindow.min_screen_width = 1092
    appWindow.min_screen_height = 614

    appWindow.setMinimumSize(QSize(appWindow.min_screen_width, appWindow.min_screen_height))
    appWindow.setWindowTitle(appWindow.appWindowTitle)
    appWindow.showMaximized()
    




    sys.exit(app.exec())