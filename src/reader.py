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



from PyQt6.QtWidgets import QWidget, QHBoxLayout, QPushButton, QSizePolicy
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QCursor, QIcon, QFont

from themes import Themes

class Reader(QWidget):
    def __init__(self, obj, win_dow):
        super().__init__()
        self.obj = obj
        self.win_dow = win_dow

        self.themeObj = object()
        self.setting = object()
        self.sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.max_button_size = QSize(36, 36)
        self.min_button_size = QSize(36, 36)
        self.icon_size = QSize(20, 20)
        self.themeIndex = object()

        self.hideNav = bool()
        self.fsState = bool()
        self.readerDisplayIndex = int()
        self.initReaderState = []

    def backAction(self):
        self.obj.talkToStackWidgetIndex(0, self.win_dow)

    def setState(self, state):
        self.readerDisplayIndex = state[0]
        self.hideNav = state[1]
        self.fsState = state[2]
        self.initReaderState = state

    def selfInit(self):
        self.mainLayout = QHBoxLayout()
        self.scrollingLayoutInit()
        self.pagingLayoutInit()
        self.setLayout(self.mainLayout)

    def scrollingLayoutInit(self):
        self.backButtonLayout = QHBoxLayout()
        self.backButton = QPushButton()
        self.backButton.setObjectName("backButton")
        self.backButton.setSizePolicy(self.sizePolicy)
        self.backButton.setMinimumSize(self.min_button_size)
        self.backButton.setMaximumSize(self.max_button_size)
        self.backButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.backButton.setGeometry(0, 0, 36, 36)

        self.backIcon = QIcon()
        self.backButton.setIconSize(self.icon_size)
        self.backButton.setCheckable(True)

        self.backButtonLayout.addWidget(self.backButton)


        self.mainLayout.addLayout(self.backButtonLayout)
        self.backButton.clicked.connect(lambda: self.backAction())

    def pagingLayoutInit(self):
        ...

    def updateLayout(self):
        print("Updating Layout")