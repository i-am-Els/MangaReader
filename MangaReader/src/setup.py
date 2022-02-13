# import sys, ctypes

from themes import Themes

from PyQt6.QtWidgets import (
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

        self.windowIcon = QIcon()
        self.windowIcon.addPixmap(QPixmap("MangaReader/resources/logo/owlly.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(self.windowIcon)
        
        self.objMainWindow = mainWindow.MainWindow(Link, self, self.windowIcon)
        self.objReader = reader.Reader(Link, self)
        self.objPref = pref.Preference(Link, self)

        self.addWidget(self.objMainWindow)
        self.addWidget(self.objReader)
        self.addWidget(self.objPref)

        self.objMainWindow.setObjectName("objMainWindow")
        self.objReader.setObjectName("objReader")
        self.objPref.setObjectName("objPref")

        self.stylesIndex = 0

        self.setTheme(self.stylesIndex)

    def changeStackIndex(self, obj, w_index):
        obj.setCurrentIndex(w_index)

    def setTheme(self, s_index):
        theme = Themes(self)
        obj = self
        if s_index == 0:
            theme.lightMode(obj=obj)
        else:
            theme.darkMode(obj=obj)

        theme.declareTheme(self, s_index, theme)

        
