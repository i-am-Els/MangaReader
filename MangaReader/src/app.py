from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QMainWindow, QSizePolicy
from PyQt6.QtCore import QSize
import sys, setup, ctypes
from themes import WindowTitleBar, MoveableWindow

def setTaskBarIcon():
    myappid = u"mycompany.myproduct.subproduct.version" # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    app.setOrganizationName("El's")
    app.setOrganizationDomain("els.ng")
    app.setApplicationName("Manhua Reader")
    

    setTaskBarIcon()
    appWindow = QMainWindow()
    appWindowTitleCustom = appWindow.appWindowTitle = "Manhua Reader"

    sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

    appLayout = QVBoxLayout()
    appWidget = QWidget()

    stWindow = setup.Window()
    stWindowLayout = QVBoxLayout()
    stWindowLayout.addWidget(stWindow)

    customTitleBar = WindowTitleBar(appWindow, appWindowTitleCustom, stWindow.windowIcon)

    cLayout = QVBoxLayout()
    cWidget = MoveableWindow(appWindow)
    cWidget.setSizePolicy(sizePolicy)
    cWidget.setFixedHeight(30)
    cWidget.refIcon = customTitleBar.restoreIcon
    cWidget.refIconIcon = customTitleBar.restoreIconIcon
    
    cWidget.setLayout(customTitleBar)
    cWidget.setMaximumHeight(30)
    cWidget.setStyleSheet("QWidget{background-color: rgba(72, 75, 106, 0.65); color: white;}")
    cLayout.addWidget(cWidget)
    cLayout.setSpacing(0)
    cLayout.setContentsMargins(0,0,0,0)
    
    appLayout.addLayout(cLayout)
    appLayout.addLayout(stWindowLayout)

    appLayout.setStretch(0, 1)
    appLayout.setStretch(1, 20)
    appLayout.setSpacing(0)

    appLayout.setContentsMargins(0,0,0,0)

    appWidget.setLayout(appLayout)

    # appWindow.setWindowIcon(stWindow.windowIcon)
    
    
    appWindow.setCentralWidget(appWidget)

    appWindow.min_screen_width = 1092
    appWindow.min_screen_height = 614

    appWindow.setMinimumSize(QSize(appWindow.min_screen_width, appWindow.min_screen_height))
    appWindow.setWindowTitle(appWindow.appWindowTitle)

    app.setWindowIcon(stWindow.windowIcon)
    appWindow.showMaximized()
    

    sys.exit(app.exec())