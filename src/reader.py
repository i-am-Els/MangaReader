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



from email.charset import QP
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QSizePolicy, QScrollArea
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QCursor, QIcon, QPixmap
import os
from pathlib import Path

# from themes import Themes

class Reader(QWidget):
    def __init__(self, obj, win_dow):
        super().__init__()
        self.obj = obj
        self.win_dow = win_dow
        self.imageList = []
        self.imageCurrent = int()
        self.currentPath = ''
        self.manhuaKey = ""

        self.themeObj = object()
        self.setting = object()
        self.sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.max_button_size = QSize(36, 36)
        self.min_button_size = QSize(36, 36)
        self.icon_size = QSize(20, 20)
        self.themeIndex = object()
        self.mlWidth = int()
        self.mlHeight = int()

        self.hideNav = bool()
        self.fsState = bool()
        self.readerDisplayIndex = int()
        self.initReaderState = []
        
        self.majorLayout = QVBoxLayout()
        

    def backAction(self):
        self.obj.talkToStackWidgetIndex(0, self.win_dow)

    def calLabelSize(self):
        self.mlWidth = self.manhuaLabel.width()
        self.mlHeight = self.manhuaLabel.height()
        # if self.win_dow.currentIndex == 1:
            # self.reScaleMLabel()
            # ...

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
        self.calLabelSize()
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
        self.backButton.setToolTip("Return to Description Page")
        self.backButton.setToolTipDuration(3000)

        self.backIcon = QIcon()
        self.backButton.setIconSize(self.icon_size)
        self.backButton.setCheckable(True)
        self.leftLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.leftLayout.addWidget(self.backButton)

        self.screenLayout = QHBoxLayout()
        self.manhuaLabel = QLabel()
        self.manhuaLabel.setScaledContents(True)
        self.manhuaLabel.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        self.spaceEatingWidgetLeft = QWidget()        
        self.spaceEatingWidgetRight = QWidget()
        self.screenLayout.addWidget(self.spaceEatingWidgetLeft)
        self.screenLayout.addWidget(self.manhuaLabel)
        self.screenLayout.addWidget(self.spaceEatingWidgetRight)

        self.screenLayout.setStretch(0, 1)
        self.screenLayout.setStretch(1, 2)
        self.screenLayout.setStretch(2, 1)

        self.rightLayout = QVBoxLayout()
        self.setToCoverButton = QPushButton()
        self.setToCoverButton.setObjectName("setToCoverButton")
        self.setToCoverButton.setSizePolicy(self.sizePolicy)
        self.setToCoverButton.setMinimumSize(self.min_button_size)
        self.setToCoverButton.setMaximumSize(self.max_button_size)
        self.setToCoverButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setToCoverButton.setGeometry(0, 0, 36, 36)
        self.setToCoverButton.setToolTip("Set Current Image as Manhua Cover")
        self.setToCoverButton.setToolTipDuration(3000)

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
        self.backButton.setToolTip("Return to Description Page")
        self.backButton.setToolTipDuration(3000)

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

        self.spaceEatingWidgetDown = QWidget()
        self.leftDummyLayout.addWidget(self.spaceEatingWidgetDown)
        
        self.leftLayout.addLayout(self.backLayout)
        self.leftLayout.addLayout(self.previousLayout)
        self.leftLayout.addLayout(self.leftDummyLayout)

        self.leftLayout.setStretch(0, 1)
        self.leftLayout.setStretch(1, 5)
        self.leftLayout.setStretch(2, 1)

        self.screenLayout = QHBoxLayout()
        self.manhuaLabel = QLabel()
        self.manhuaLabel.setScaledContents(True)
        self.manhuaLabel.setSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        self.spaceEatingWidgetLeft = QWidget()        
        self.spaceEatingWidgetRight = QWidget()
        self.screenLayout.addWidget(self.spaceEatingWidgetLeft)
        self.screenLayout.addWidget(self.manhuaLabel)
        self.screenLayout.addWidget(self.spaceEatingWidgetRight)

        self.screenLayout.setStretch(0, 1)
        self.screenLayout.setStretch(1, 2)
        self.screenLayout.setStretch(2, 1)

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
        self.setToCoverButton.setToolTip("Set Current Image as Manhua Cover")
        self.setToCoverButton.setToolTipDuration(3000)

        self.setToCoverIcon = QIcon()
        self.setToCoverButton.setIconSize(self.icon_size)
        self.setToCoverButton.setCheckable(True)

        self.nextLayout.addWidget(self.nextButton)
        self.setToCoverLayout.addWidget(self.setToCoverButton)

        self.nextLayout.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.setToCoverLayout.setAlignment(Qt.AlignmentFlag.AlignBottom) 

        self.spaceEatingWidgetUp = QWidget()
        self.rightDummyLayout.addWidget(self.spaceEatingWidgetUp)

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
        if typeIndex == 0:
            if self.imageCurrent > 0:
                self.imageCurrent -= 1
                self.setImageToLabel(self.imageCurrent)
        elif typeIndex == 2:
            if self.imageCurrent < (len(self.imageList) - 1):
                self.imageCurrent += 1
                self.setImageToLabel(self.imageCurrent)
    
    def nextAction(self, typeIndex):
        if typeIndex == 0:
            if self.imageCurrent < (len(self.imageList) - 1):
                self.imageCurrent += 1
                self.setImageToLabel(self.imageCurrent)
        elif typeIndex == 2:
            if self.imageCurrent > 0:
                self.imageCurrent -= 1
                self.setImageToLabel(self.imageCurrent)

    def setToCoverAction(self):
        imagePath = str(self.currentPath) + self.imageList[self.imageCurrent]
        print(imagePath)
        self.win_dow.objMainWindow.library.setCover(imagePath, self.manhuaKey)



    def loadChapterPages(self, path, key):
        self.currentPath = path
        self.manhuaKey = key
        self.imageList = []
        for x in os.listdir(path):
            if Path(x).suffix in ['.jpeg', '.jpg', '.png']:
                self.imageList.append(str(x))
        self.imageCurrent = 0
        self.setImageToLabel(self.imageCurrent)

    # def reScaleMLabel(self):
    #     self.manhuaLabel.pixmap().scaled(self.mlWidth, self.mlHeight, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation)

    def setImageToLabel(self, index):
        path = str(self.currentPath) + self.imageList[index]
        self.manhuaLabel.setPixmap(QPixmap(path))
        # self.manhuaLabel.setPixmap(QPixmap(path).scaled(self.mlWidth, self.mlHeight, Qt.AspectRatioMode.IgnoreAspectRatio, Qt.TransformationMode.SmoothTransformation))
