# Manhua Reader,  An application for reading manhuas and manhuas online and offline
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

import resources, consts, mainWindow, reader, pref
from PyQt6.QtGui import QIcon, QPixmap
from settings import Settings
from linker import Link




class Window(QStackedWidget):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Window, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        super().__init__()
        self.window_icon = QIcon()
        self.window_icon.addPixmap(QPixmap(resources.app_logo), QIcon.Mode.Normal, QIcon.State.Off)
        self.setWindowIcon(self.window_icon)

        Settings.init()

        self.objMainWindow = mainWindow.MainWindow(self)
        self.objReader = reader.Reader(self)
        self.objPref = pref.Preference()

        Settings.initObjs(self)

        self.addWidget(self.objMainWindow)
        self.addWidget(self.objReader)
        self.addWidget(self.objPref)
        
        Link.setCreatorWindow(self)
        Themes.themeInit()

        self.objMainWindow.setObjectName(consts.OBJ_MW_NAME)
        self.objReader.setObjectName(consts.OBJ_READER_NAME)
        self.objPref.setObjectName(consts.OBJ_PREF_NAME)
        

        self.setSetting()
        # self.objMainWindow.library.loadLibraryItems()
        self.setTheme(Settings.themeIndex)

        self.objMainWindow.loadHomeTab()
        
    def changeStackIndex(self, w_index: int) -> None:
        self.setCurrentIndex(w_index)

    def setTheme(self, s_index: int) -> None:
        Themes.declareTheme(s_index)
        if s_index == consts.E_THEME_LIGHT_MODE:
            Themes.lightMode(obj=self)
            self.objPref.setThemesBtnChecked(False)
        else:
            Themes.darkMode(obj=self)
            self.objPref.setThemesBtnChecked(True)

    def setSetting(self) -> None:
        Settings.setStates()

