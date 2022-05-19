# Manhua Reader,  An application for reading mangas and manhuas online and offline
# Copyright (C) 2022  Eniola Emmanuel Olawale

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.



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
    def __init__(self, appW):
        super().__init__()
        self.appW = appW
        self.windowIcon = QIcon()
        self.windowIcon.addPixmap(QPixmap("resources/logo/mrlogoRound.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(self.windowIcon)


        self.objMainWindow = mainWindow.MainWindow(Link, self, self.windowIcon, self.appW)
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

        self.objMainWindow.themeObj = self.theme
        self.objReader.themeObj = self.theme
        self.objPref.themeObj = self.theme


        # self.objMainWindow.library.loadLibraryTab()
        self.objMainWindow.loadHomeTab()
        
    def changeStackIndex(self, obj, w_index):
        obj.setCurrentIndex(w_index)

    def setTheme(self, s_index):
        obj = self
        if s_index == 0:
            self.theme.lightMode(obj=obj)
            self.objPref.themesBtn.setChecked(False)
        else:
            self.theme.darkMode(obj=obj)
            self.objPref.themesBtn.setChecked(True)

        self.theme.declareTheme(self, s_index)

    def setSetting(self):
        self.objMainWindow.setting = self.setting
        self.objPref.setting = self.setting
        self.objReader.setting = self.setting

        self.setting.setStates()
    

      
        
