import sys, ctypes

from PyQt6.QtWidgets import (
    QApplication,
    QStackedWidget,
)

import mainWindow, pref, reader
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon, QPixmap


class Link(object):

    def talkToStackWidgetIndex(w_index, obj):
        obj.changeStackIndex(obj, w_index)


class Window(QStackedWidget):
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

        self.windowIcon = QIcon()
        self.windowIcon.addPixmap(QPixmap("MangaReader/resources/logo/owlly.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(self.windowIcon)
        
        self.objMainWindow = mainWindow.MainWindow(Link, self, self.windowIcon)
        self.objReader = reader.Reader(Link, self)
        self.objPref = pref.Preference(Link, self)

        self.addWidget(self.objMainWindow)
        self.addWidget(self.objReader)
        self.addWidget(self.objPref)
        print(self.count())

    def changeStackIndex(self, obj, w_index):
        obj.setCurrentIndex(w_index)


def setTaskBarIcon():
    myappid = u'mycompany.myproduct.subproduct.version' # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    setTaskBarIcon()

    window = Window()
    window.showMaximized()
    sys.exit(app.exec())