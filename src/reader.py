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



from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QSizePolicy
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
        
        self.majorLayout = QVBoxLayout()
        

    def backAction(self):
        self.obj.talkToStackWidgetIndex(0, self.win_dow)

    def setState(self, state):
        self.readerDisplayIndex = state[0]
        self.hideNav = state[1]
        self.fsState = state[2]
        self.initReaderState = state

    def selfInit(self):
        self.majorWidget = QWidget()
        self.setLayout(self.majorLayout)
        self.mainLayout = QHBoxLayout()
        if self.readerDisplayIndex == 1:
            self.scrollingLayoutInit()
        else:
            self.pagingLayoutInit()
        self.majorLayout.addWidget(self.majorWidget)
        self.majorWidget.setLayout(self.mainLayout)

    def scrollingLayoutInit(self):
        self.leftLayout = QVBoxLayout()
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
        self.leftLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.leftLayout.addWidget(self.backButton)

        self.screenLayout = QVBoxLayout()

        self.rightLayout = QVBoxLayout()
        self.setToCoverButton = QPushButton()
        self.setToCoverButton.setObjectName("setToCoverButton")
        self.setToCoverButton.setSizePolicy(self.sizePolicy)
        self.setToCoverButton.setMinimumSize(self.min_button_size)
        self.setToCoverButton.setMaximumSize(self.max_button_size)
        self.setToCoverButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setToCoverButton.setGeometry(0, 0, 36, 36)

        self.setToCoverIcon = QIcon()
        self.setToCoverButton.setIconSize(self.icon_size)
        self.setToCoverButton.setCheckable(True)
        self.rightLayout.setAlignment(Qt.AlignmentFlag.AlignBottom)        
        self.rightLayout.addWidget(self.setToCoverButton)


        self.mainLayout.addLayout(self.leftLayout)
        self.mainLayout.addLayout(self.screenLayout)
        self.mainLayout.addLayout(self.rightLayout)
        
        self.mainLayout.setStretch(0, 1)
        self.mainLayout.setStretch(1, 10)
        self.mainLayout.setStretch(2, 1)
        self.backButton.clicked.connect(lambda: self.backAction())
        self.setToCoverButton.clicked.connect(lambda: self.setToCoverAction())

    def pagingLayoutInit(self):
        self.leftLayout = QVBoxLayout()
        self.leftDummyLayout = QVBoxLayout()
        self.backLayout = QVBoxLayout()
        self.previousLayout = QVBoxLayout()
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

        self.previousButton = QPushButton()
        self.previousButton.setObjectName("previousButton")
        self.previousButton.setSizePolicy(self.sizePolicy)
        self.previousButton.setMinimumSize(self.min_button_size)
        self.previousButton.setMaximumSize(self.max_button_size)
        self.previousButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.previousButton.setGeometry(0, 0, 36, 36)

        self.previousIcon = QIcon()
        self.previousButton.setIconSize(self.icon_size)
        self.previousButton.setCheckable(True)

        self.backLayout.addWidget(self.backButton)
        self.previousLayout.addWidget(self.previousButton)

        self.backLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.previousLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)

        self.spaceEatingWidget2 = QWidget()
        self.leftDummyLayout.addWidget(self.spaceEatingWidget2)
        
        self.leftLayout.addLayout(self.backLayout)
        self.leftLayout.addLayout(self.previousLayout)
        self.leftLayout.addLayout(self.leftDummyLayout)

        self.leftLayout.setStretch(0, 1)
        self.leftLayout.setStretch(1, 5)
        self.leftLayout.setStretch(2, 1)

        self.screenLayout = QVBoxLayout()

        self.rightLayout = QVBoxLayout()
        self.rightDummyLayout = QVBoxLayout()
        self.nextLayout = QVBoxLayout()
        self.setToCoverLayout = QVBoxLayout()
        self.nextButton = QPushButton()
        self.nextButton.setObjectName("nextButton")
        self.nextButton.setSizePolicy(self.sizePolicy)
        self.nextButton.setMinimumSize(self.min_button_size)
        self.nextButton.setMaximumSize(self.max_button_size)
        self.nextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nextButton.setGeometry(0, 0, 36, 36)

        self.nextIcon = QIcon()
        self.nextButton.setIconSize(self.icon_size)
        self.nextButton.setCheckable(True)

        self.setToCoverButton = QPushButton()
        self.setToCoverButton.setObjectName("setToCoverButton")
        self.setToCoverButton.setSizePolicy(self.sizePolicy)
        self.setToCoverButton.setMinimumSize(self.min_button_size)
        self.setToCoverButton.setMaximumSize(self.max_button_size)
        self.setToCoverButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setToCoverButton.setGeometry(0, 0, 36, 36)

        self.setToCoverIcon = QIcon()
        self.setToCoverButton.setIconSize(self.icon_size)
        self.setToCoverButton.setCheckable(True)

        self.nextLayout.addWidget(self.nextButton)
        self.setToCoverLayout.addWidget(self.setToCoverButton)

        self.nextLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.setToCoverLayout.setAlignment(Qt.AlignmentFlag.AlignBottom) 

        self.spaceEatingWidget = QWidget()
        self.rightDummyLayout.addWidget(self.spaceEatingWidget)

        self.rightLayout.addLayout(self.rightDummyLayout)
        self.rightLayout.addLayout(self.nextLayout)
        self.rightLayout.addLayout(self.setToCoverLayout)

        self.rightLayout.setStretch(0, 1)
        self.rightLayout.setStretch(1, 5)
        self.rightLayout.setStretch(2, 1)

        self.mainLayout.addLayout(self.leftLayout)
        self.mainLayout.addLayout(self.screenLayout)
        self.mainLayout.addLayout(self.rightLayout)

        self.mainLayout.setStretch(0, 1)
        self.mainLayout.setStretch(1, 10)
        self.mainLayout.setStretch(2, 1)

        self.backButton.clicked.connect(lambda: self.backAction())
        self.previousButton.clicked.connect(lambda: self.previousAction(self.readerDisplayIndex))
        self.nextButton.clicked.connect(lambda: self.nextAction(self.readerDisplayIndex))
        self.setToCoverButton.clicked.connect(lambda: self.setToCoverAction())

    def updateLayout(self):
        self.majorWidget.deleteLater()
        self.selfInit()
        self.themeObj.readerStyle(self, self.readerDisplayIndex)

    def previousAction(self, typeIndex):
        ...
    
    def nextAction(self, typeIndex):
        ...

    def setToCoverAction(self):
        ...