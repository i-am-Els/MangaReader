from themes import Themes

from PyQt6.QtWidgets import (
    QStackedWidget
)

import mainWindow, pref, reader
from PyQt6.QtGui import QIcon, QPixmap
from settings import Settings

class Link(object):

    def talkToStackWidgetIndex(w_index, obj):
        obj.changeStackIndex(obj, w_index)


class Window(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.windowIcon = QIcon()
        self.windowIcon.addPixmap(QPixmap("MangaReader/resources/logo/mrlogoRound.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(self.windowIcon)


        self.objMainWindow = mainWindow.MainWindow(Link, self, self.windowIcon)
        self.objReader = reader.Reader(Link, self)
        self.objPref = pref.Preference(Link, self)

        self.theme = Themes(self)
        self.setting = Settings(self)

        self.addWidget(self.objMainWindow)
        self.addWidget(self.objReader)
        self.addWidget(self.objPref)

        self.objMainWindow.setObjectName("objMainWindow")
        self.objReader.setObjectName("objReader")
        self.objPref.setObjectName("objPref")

        self.setSetting()

        self.setTheme(self.setting.themeIndex)

    def changeStackIndex(self, obj, w_index):
        obj.setCurrentIndex(w_index)

    def setTheme(self, s_index):
        obj = self
        if s_index == 0:
            self.theme.lightMode(obj=obj)
        else:
            self.theme.darkMode(obj=obj)

        self.theme.declareTheme(self, s_index, self.theme)

    def setSetting(self):
        self.objMainWindow.setting = self.setting
        self.objPref.setting = self.setting
        self.objReader.setting = self.setting

        self.setting.setStates()
    

      
        
