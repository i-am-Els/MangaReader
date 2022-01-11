from PyQt6.QtWidgets import (
    QMainWindow,
    QStackedWidget,
    QStatusBar,
)

from PyQt6.QtCore import Qt, QSize

import mainWindow
import reader
import settings

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.screen_width = 1366
        #self.screen_height = 768
        self.min_screen_width = 915
        self.min_screen_height = 515
        self.resize_width = 1092
        self.resize_height = 614
        self.appWindowTitle = "Manhua Reader"
        self.resize(QSize(self.resize_width, self.resize_height))
        self.setMinimumSize(QSize(self.min_screen_width, self.min_screen_height))
        self.setWindowTitle(self.appWindowTitle)

       


        #self.mainlayout = QVBoxLayout()
        self.stackWidget = QStackedWidget()

        self.stackWidget.addWidget(mainWindow.MainWindow())
        self.stackWidget.addWidget(reader.Reader())
        self.stackWidget.addWidget(settings.Settings())

        self.stackWidget.setCurrentIndex(0)

        #self.mainlayout.addWidget(self.stackWidget)
        #self.setLayout(self.mainlayout)
        self.setCentralWidget(self.stackWidget)

        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        self.setStyleSheet("""QStatusBar{
            background-color: rgba(0,0,0,40);
        }""")

        
        


