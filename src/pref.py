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




from PyQt6.QtWidgets import (
    QStackedWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QWidget,
    QLabel,
    QSizePolicy,
    QPushButton,
    QRadioButton,
    QListWidget,
    QFileDialog
)

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QCursor, QIcon, QFont

from pathlib import Path
# import os

from themes import ToggleSwitch

class Preference(QWidget):
    def __init__(self, obj, win_dow):
        super().__init__()
        self.obj = obj
        self.win_dow = win_dow

        self.themeObj = object()
        self.setting = object()
        
        # self.themeObj = self.win_dow.theme
        # self.setting = self.win_dow.setting

        self.max_button_size = QSize(36, 36)
        self.min_button_size = QSize(36, 36)
        self.icon_size = QSize(20, 20)
        self.active = 0
        self.themeIndex = int()

        self.fontSize1 = 11
        self.fontSize2 = 9
        self.fontSize3 = 8

        self.compressionState = bool()
        self.themeButtonState = bool()
        self.updateChapter = bool()
        self.updateOther = bool()
        self.hideNav = bool()
        self.fsState = bool()
        self.readerDisplayIndex = int()
        self.readerDisplayList = []
        self.settingsToggleIndex = int()
        self.settingsToggleList = []
        self.initReaderState = []
        self.updatedReaderState = []

        self.downloadDirPath = object()
        self.initPath = object()
        self.newPath = object()
        
        

        self.sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        #-----------------------------------------------
        self.gridLayout = QGridLayout()

        # Create baseLayout
        self.baseLayout = QVBoxLayout()        
        self.baseLayout.setSpacing(9)

        #-----------------------------------------------
        # Create an horizontal headerLayout
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setContentsMargins(-1, 10, -1, 10)

        self.bodyLayout = QHBoxLayout()

        #-----------------------------------------------
        # Create a backButton
        self.backButton = QPushButton()
        self.backButton.setObjectName("backButton")

        self.backButton.setSizePolicy(self.sizePolicy)
        self.backButton.setMinimumSize(self.min_button_size)
        self.backButton.setMaximumSize(self.max_button_size)
        self.backButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.backButton.setGeometry(0, 0, 36, 36)

        # Set backIcon to backButton
        self.backIcon = QIcon()
        
        self.backButton.setIconSize(self.icon_size)
        self.backButton.setCheckable(True)
        self.backButton.setToolTip("Return to Home")
        self.backButton.setToolTipDuration(3000)

        #-----------------------------------------------
        self.headerLabel = QLabel("Preference | Settings")
        self.headerLabel.setObjectName("headerLabel")
        self.headerLabel.setSizePolicy(self.sizePolicy)
        
        self.headerLabelFont = QFont()
        self.headerLabelFont.setPointSize(self.fontSize1)
        self.headerLabelFont.setBold(True)
        self.headerLabel.setFont(self.headerLabelFont)
        self.headerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        #-----------------------------------------------
        self.headerLayout.addWidget(self.backButton)
        self.headerLayout.addWidget(self.headerLabel)

        self.headerLayout.setStretch(0, 1)
        self.headerLayout.setStretch(1, 9)
        #-----------------------------------------------
        self.buttonsLayout = QVBoxLayout()
        self.buttonsLayout.setSpacing(5)

        self.settingsButton = QPushButton("Settings")
        self.settingsButton.setCheckable(True)
        self.settingsButton.setSizePolicy(self.sizePolicy)
        self.settingsButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settingsButton.setObjectName("settingsButton")

        self.downloadButton = QPushButton("Downloads")
        self.downloadButton.setCheckable(True)
        self.downloadButton.setSizePolicy(self.sizePolicy)
        self.downloadButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.downloadButton.setObjectName("downloadButton")

        self.themesButton = QPushButton("Themes")
        self.themesButton.setCheckable(True)
        self.themesButton.setSizePolicy(self.sizePolicy)
        self.themesButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.themesButton.setObjectName("themesButton")

        self.spaceEater = QWidget()
        self.spaceEater.setSizePolicy(self.sizePolicy)

        self.buttonsLayout.addWidget(self.settingsButton)
        self.buttonsLayout.addWidget(self.downloadButton)
        self.buttonsLayout.addWidget(self.themesButton)
        self.buttonsLayout.addWidget(self.spaceEater)

        self.buttonsLayout.setObjectName("buttonsLayout")

        self.buttonsLayout.setStretch(0, 1)
        self.buttonsLayout.setStretch(1, 1)
        self.buttonsLayout.setStretch(2, 1)
        self.buttonsLayout.setStretch(3, 12)


        #-----------------------------------------------
        self.stackLayout = QVBoxLayout()
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.setSizePolicy(self.sizePolicy)
        self.stackedWidget.setObjectName(u"prefStacked")

        self.settingsWidget = QWidget()
        self.settingsWidget.setObjectName("settingsWidget")
        self.settingsWidget.setSizePolicy(self.sizePolicy)
        self.settingsLayout = QVBoxLayout()
        
        self.settingsWidgetObj()

        self.settingsWidget.setLayout(self.settingsLayout)
        

        self.downloadsWidget = QWidget()
        self.downloadsWidget.setObjectName("downloadsWidget")
        self.downloadsWidget.setSizePolicy(self.sizePolicy)
        self.downloadsLayout = QVBoxLayout()

        self.downloadWidgetObj()
        
        self.downloadsWidget.setLayout(self.downloadsLayout)

        self.themesWidget = QWidget()
        self.themesWidget.setObjectName("themesWidget")
        self.themesWidget.setSizePolicy(self.sizePolicy)
        self.themesLayout = QVBoxLayout()

        self.themesWidgetObj()
        
        self.themesWidget.setLayout(self.themesLayout)

        self.stackedWidget.addWidget(self.settingsWidget)
        self.stackedWidget.addWidget(self.downloadsWidget)
        self.stackedWidget.addWidget(self.themesWidget)

        #---------------------------------------------------
        self.stackLayout.addWidget(self.stackedWidget)

        #-----------------------------------------------
        self.bodyLayout.addLayout(self.buttonsLayout)
        self.bodyLayout.addLayout(self.stackLayout)
        self.bodyLayout.setStretch(0, 2)
        self.bodyLayout.setStretch(1, 8)
        #-----------------------------------------------
        self.headerBackgroundWidget = QWidget()
        self.headerBackgroundLayout = QVBoxLayout()
        self.headerBackgroundWidget.setLayout(self.headerLayout)
        self.headerBackgroundLayout.addWidget(self.headerBackgroundWidget)

        self.baseLayout.addLayout(self.headerBackgroundLayout)
        self.baseLayout.addLayout(self.bodyLayout)

        self.baseLayout.setStretch(0, 1)
        self.baseLayout.setStretch(1, 11)
        #-----------------------------------------------

        self.gridLayout.addLayout(self.baseLayout, 0, 0, 1, 1)

        self.setLayout(self.gridLayout)
        #-----------------------------------------------

        self.backButton.clicked.connect(self.backAction)

        self.settingsButton.clicked.connect(lambda: self.setActive(0))

        self.downloadButton.clicked.connect(lambda: self.setActive(1))
        
        self.themesButton.clicked.connect(lambda: self.setActive(2))

    def backAction(self):
        self.setting.setPrefVariables()
        self.updateReaderState()
        self.obj.talkToStackWidgetIndex(0, self.win_dow)

    def updateReaderState(self):
        if self.initReaderState != self.win_dow.objReader.initReaderState:
            self.updatedReaderState = self.initReaderState
            self.win_dow.objReader.setState(self.updatedReaderState)
            self.win_dow.objReader.updateLayout()

    def changeStackIndex(self, obj, w_index):
        obj.setCurrentIndex(w_index)

    def setActive(self, activeIndex):
        self.active = activeIndex
        
        self.themeObj.prefButtonActive(self.active, self.themeIndex)

        self.stackedWidget.setCurrentIndex(self.active)

    def settingsWidgetObj(self):
        self.libraryLabel = QLabel("Library")
        self.libraryLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.libraryLabel.setSizePolicy(self.sizePolicy)

        self.libraryLabelFont = QFont()
        self.libraryLabelFont.setBold(True)
        self.libraryLabelFont.setPointSize(self.fontSize1)

        self.libraryLabel.setFont(self.libraryLabelFont)

        self.libraryLabelLayout = QVBoxLayout()
        self.libraryLabelLayout.addWidget(self.libraryLabel)

        #----------------------------------------------

        self.autoUpdateLabel = QLabel("Auto Update Library")
        self.autoUpdateLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.autoUpdateLabel.setSizePolicy(self.sizePolicy)
        self.autoUpdateLabelFont = QFont()
        self.autoUpdateLabelFont.setPointSize(self.fontSize2)
        self.autoUpdateLabel.setFont(self.autoUpdateLabelFont)

        self.autoUpdateLabelLayout = QVBoxLayout()
        self.autoUpdateLabelLayout.addWidget(self.autoUpdateLabel)
        #------------------

        self.autoUpdateLabelOne = QLabel("Chapters")
        self.autoUpdateLabelOne.setSizePolicy(self.sizePolicy)

        self.autoUpdateLabelOneFont = QFont()
        self.autoUpdateLabelOneFont.setPointSize(self.fontSize3)
        self.autoUpdateLabelOne.setFont(self.autoUpdateLabelOneFont)

        self.autoUpdateLabelOneLayout = QHBoxLayout()
        
        self.toggleOne = ToggleSwitch()
        self.toggleOne.setCheckable(True)
        self.toggleOne.setSizePolicy(self.sizePolicy)

        self.autoUpdateLabelOneLayout.addWidget(self.autoUpdateLabelOne)
        self.autoUpdateLabelOneLayout.addWidget(self.toggleOne)

        #------------------

        self.autoUpdateLabelTwo = QLabel("Cover Image and Description")
        self.autoUpdateLabelTwo.setSizePolicy(self.sizePolicy)

        self.autoUpdateLabelTwoFont = QFont()
        self.autoUpdateLabelTwoFont.setPointSize(self.fontSize3)
        self.autoUpdateLabelTwo.setFont(self.autoUpdateLabelTwoFont)

        self.autoUpdateLabelTwoLayout = QHBoxLayout()

        self.toggleTwo = ToggleSwitch()
        self.toggleTwo.setCheckable(True)
        self.toggleTwo.setSizePolicy(self.sizePolicy)

        self.autoUpdateLabelTwoLayout.addWidget(self.autoUpdateLabelTwo)
        self.autoUpdateLabelTwoLayout.addWidget(self.toggleTwo)

        self.autoUpdateLabelOneLayout.setContentsMargins(25, 0, 0, 0)
        self.autoUpdateLabelTwoLayout.setContentsMargins(25, 0, 0, 0)

        self.autoUpdateLabelOneLayout.setStretch(0, 10)
        self.autoUpdateLabelOneLayout.setStretch(1, 1)

        self.autoUpdateLabelTwoLayout.setStretch(0, 10)
        self.autoUpdateLabelTwoLayout.setStretch(1, 1)
        #------------------

        self.autoUpdateLayout = QVBoxLayout()
        self.autoUpdateLayoutInner = QVBoxLayout()

        self.autoUpdateLayoutInner.addLayout(self.autoUpdateLabelOneLayout)
        self.autoUpdateLayoutInner.addLayout(self.autoUpdateLabelTwoLayout)

        self.autoUpdateLayout.addLayout(self.autoUpdateLabelLayout)
        self.autoUpdateLayout.addLayout(self.autoUpdateLayoutInner)

        self.autoUpdateLayout.setStretch(0, 1)
        self.autoUpdateLayout.setStretch(1, 1)
        self.autoUpdateLayout.setSpacing(0)

        self.libraryLayout = QVBoxLayout()
        self.libraryLayout.addLayout(self.libraryLabelLayout)
        self.libraryLayout.addLayout(self.autoUpdateLayout)


        #---------------------------------------------------
        self.readerLabel = QLabel("Reader")
        self.readerLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.readerLabel.setSizePolicy(self.sizePolicy)

        self.readerLabelFont = QFont()
        self.readerLabelFont.setBold(True)
        self.readerLabelFont.setPointSize(self.fontSize1)

        self.readerLabel.setFont(self.readerLabelFont)

        
        self.readerLabelLayout = QVBoxLayout()
        self.readerLabelLayout.addWidget(self.readerLabel)

        #------------------------
        self.readingModeLabel = QLabel("Default Reading Mode")
        self.readingModeLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.readingModeLabel.setSizePolicy(self.sizePolicy)
        self.readingModeLabelFont = QFont()
        self.readingModeLabelFont.setPointSize(self.fontSize2)
        self.readingModeLabel.setFont(self.readingModeLabelFont)

        self.readingModeLabelLayout = QVBoxLayout()
        self.readingModeLabelLayout.addWidget(self.readingModeLabel)

        #------------------------

        self.radioButtonOne = QRadioButton("Left-to-Right")
        self.radioButtonOne.setSizePolicy(self.sizePolicy)

        self.radioButtonTwo = QRadioButton("Webtoon/Vertical")
        self.radioButtonTwo.setSizePolicy(self.sizePolicy)
        
        self.radioButtonThree = QRadioButton("Right-to-Left")
        self.radioButtonThree.setSizePolicy(self.sizePolicy)

        
        self.radioButtonOne.adjustSize()
        
        self.radioButtonTwo.adjustSize()
        
        self.radioButtonThree.adjustSize()

        self.readerDisplayList = [self.radioButtonOne, self.radioButtonTwo, self.radioButtonThree]

        self.radioButtonLayout = QVBoxLayout()

        
        self.radioButtonLayout.addWidget(self.radioButtonOne)
        self.radioButtonLayout.addWidget(self.radioButtonTwo)
        self.radioButtonLayout.addWidget(self.radioButtonThree)
        #------------------

        self.radioButtonLayout.setStretch(0, 1)
        self.radioButtonLayout.setStretch(1, 1)
        self.radioButtonLayout.setStretch(2, 1)
        self.radioButtonLayout.setSpacing(0)

        self.radioButtonLayout.setContentsMargins(45, 0, 0, 0)


        self.readerChoiceInnerLayout = QVBoxLayout()

        self.readerChoiceInnerLayout.addLayout(self.readingModeLabelLayout)
        self.readerChoiceInnerLayout.addLayout(self.radioButtonLayout)

        self.readerChoiceInnerLayout.setStretch(0, 1)
        self.readerChoiceInnerLayout.setStretch(1, 1)


        self.readerLayout = QVBoxLayout()
        self.readerLayout.addLayout(self.readerLabelLayout)
        self.readerLayout.addLayout(self.readerChoiceInnerLayout)

        #----------------------------------------------

        self.readerNavLabel = QLabel("Use Key shortcuts For Navigation\n\tA -> Previous Page | D -> Next Page\n\tQ -> Previous Chapter | E -> Next Chapter")
        self.readerNavLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.readerNavLabel.setSizePolicy(self.sizePolicy)
        self.readerNavLabelFont = QFont()
        self.readerNavLabelFont.setPointSize(self.fontSize2)
        self.readerNavLabel.setFont(self.readerNavLabelFont)

        self.readerNavtoggle = ToggleSwitch()
        self.readerNavtoggle.setCheckable(True)
        
        self.readerNavtoggle.setSizePolicy(self.sizePolicy)

        self.readerNavLayout = QHBoxLayout()

        self.readerNavLayout.addWidget(self.readerNavLabel)
        self.readerNavLayout.addWidget(self.readerNavtoggle)

        self.readerNavLayout.setStretch(0, 10)
        self.readerNavLayout.setStretch(1, 1)


        #----------------------------------------------

        self.readerFSLabel = QLabel("Open reader in fullscreen")
        self.readerFSLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.readerFSLabel.setSizePolicy(self.sizePolicy)
        self.readerFSLabelFont = QFont()
        self.readerFSLabelFont.setPointSize(self.fontSize2)
        self.readerFSLabel.setFont(self.readerFSLabelFont)

        self.readerFStoggle = ToggleSwitch()
        self.readerFStoggle.setCheckable(True)
        
        self.readerFStoggle.setSizePolicy(self.sizePolicy)

        self.readerFSLayout = QHBoxLayout()

        self.readerFSLayout.addWidget(self.readerFSLabel)
        self.readerFSLayout.addWidget(self.readerFStoggle)

        self.readerFSLayout.setStretch(0, 10)
        self.readerFSLayout.setStretch(1, 1)



        self.settingsToggleList = [self.toggleOne, self.toggleTwo, self.readerNavtoggle, self.readerFStoggle]

        #----------------------------------------------
    
        self.spaceEaterForSettings = QWidget()
        self.spaceEaterForSettings.setSizePolicy(self.sizePolicy)


        # self.spaceEaterForLayout = QVBoxLayout()
        # self.spaceEaterForLayout.addWidget(self.spaceEaterForSettings)
    
        self.settingsLayout = QVBoxLayout()
        
        self.settingsLayout.addLayout(self.libraryLayout)
        self.settingsLayout.addLayout(self.readerLayout)
        self.settingsLayout.addLayout(self.readerNavLayout)
        self.settingsLayout.addLayout(self.readerFSLayout)
        self.settingsLayout.addWidget(self.spaceEaterForSettings)

        self.settingsLayout.setStretch(0, 1)
        self.settingsLayout.setStretch(1, 1)
        self.settingsLayout.setStretch(2, 1)
        self.settingsLayout.setStretch(3, 1)
        self.settingsLayout.setStretch(4, 10)
        self.settingsLayout.setSpacing(0)

        #--------------------------------------------------
        self.radioButtonOne.toggled.connect(lambda: self.onRadioClicked(0))
        self.radioButtonTwo.toggled.connect(lambda: self.onRadioClicked(1))
        self.radioButtonThree.toggled.connect(lambda: self.onRadioClicked(2))

        self.toggleOne.clicked.connect(lambda: self.onToggleClicked(0, self.toggleOne))
        self.toggleTwo.clicked.connect(lambda: self.onToggleClicked(1, self.toggleTwo))
        self.readerNavtoggle.clicked.connect(lambda: self.onToggleClicked(2, self.readerNavtoggle))
        self.readerFStoggle.clicked.connect(lambda: self.onToggleClicked(3, self.readerFStoggle))

    def onRadioClicked(self, radioIndex):
        radioBtn = self.sender()
        self.readerDisplayIndex = radioIndex
        if radioBtn.isChecked():
            self.setting.readerDisplayIndex = radioIndex
        
    def onToggleClicked(self, btnIndex, btn):
        self.toggleBtnState = btn.isChecked()
        self.btnIndex = btnIndex
        if self.btnIndex == 0:
            self.setting.updateChapter = self.toggleBtnState
        elif self.btnIndex == 1:
            self.setting.updateOther = self.toggleBtnState
        elif self.btnIndex == 2:
            self.setting.hideNav = self.toggleBtnState
        else:
            self.setting.fsState = self.toggleBtnState

    def selectDownloadDir(self):
        self.downloadDirDialog = QFileDialog.getExistingDirectory(self,"Select Download Location", self.newPath)

        self.downloadDirPath = self.convertToPath(self.downloadDirDialog)
        if self.downloadDirDialog != "":
            self.setting.downloadNewPath = str(self.downloadDirPath)

            self.newPath = self.setting.downloadNewPath

            self.downloadDirPathDisplay.setText(str(self.newPath))
                     
    def downloadWidgetObj(self):
        self.downloadDirPathLabel = QLabel("Select Download Location")
        
        self.downloadDirPathLabel.setSizePolicy(self.sizePolicy)
        

        self.downloadDirPathDisplay = QLabel(str(self.newPath))
        self.downloadDirPathDisplay.setSizePolicy(self.sizePolicy)
        self.downloadDirPathBtn = QPushButton("Choose")
        self.downloadDirPathBtn.setSizePolicy(self.sizePolicy)

        self.downloadDirPathLayout = QHBoxLayout()
        
        self.downloadDirPathLayout.addWidget(self.downloadDirPathLabel)
        self.downloadDirPathLayout.addWidget(self.downloadDirPathDisplay)
        self.downloadDirPathLayout.addWidget(self.downloadDirPathBtn)
        self.downloadDirPathLayout.setStretch(0, 3)
        self.downloadDirPathLayout.setStretch(1, 6)
        self.downloadDirPathLayout.setStretch(2, 1)

        
        self.downloadDirPathLayout.setContentsMargins(0, 5, 0, 0)

        self.downloadQueueHeadLabel = QLabel("Download Queue")
        self.downloadQueueHeadLabel.setSizePolicy(self.sizePolicy)
        
        # self.downloadQueueHeadLabel.setMaximumHeight(60)


        self.downloadQueueStatusLabel = QLabel("Downloading 0 of 0")
        self.downloadQueueStatusLabel.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.downloadQueueStatusLabel.setSizePolicy(self.sizePolicy)

        # self.downloadQueueStatusLabel.setMaximumHeight(60)

        self.downloadQueue = QListWidget()
        self.downloadQueue.setSizePolicy(self.sizePolicy)
        
        # self.downloadQueue.setMaximumHeight(200)
        
        self.downloadQueueListLayout = QVBoxLayout()
        self.downloadQueueListLayout.addWidget(self.downloadQueue)

        self.downloadQueueInnerLayout = QHBoxLayout()

        self.downloadQueueInnerLayout.addWidget(self.downloadQueueHeadLabel)
        self.downloadQueueInnerLayout.addWidget(self.downloadQueueStatusLabel)
        self.downloadQueueInnerLayout.setStretch(0, 4)
        self.downloadQueueInnerLayout.setStretch(1, 1)

        self.downloadQueueLayout = QVBoxLayout()
        self.downloadQueueLayout.addLayout(self.downloadQueueInnerLayout)
        self.downloadQueueLayout.addLayout(self.downloadQueueListLayout)
        self.downloadQueueLayout.setStretch(0, 1)
        self.downloadQueueLayout.setStretch(1, 12)

        
        self.downloadQueueLayout.setContentsMargins(0, 0, 0, 0)


        self.compressArchiveLabel = QLabel("Compress Downloads to Archive File To cbz")
        self.compressArchiveLabel.setSizePolicy(self.sizePolicy)
        
        # self.compressArchiveLabel.setMaximumHeight(60)


        # self.radioCbz = QRadioButton("To CBZ")
        # self.radioCbz.setChecked(True)
        # self.radioCbz.setSizePolicy(self.sizePolicy)

        # self.radioCbr = QRadioButton("To CBR")
        # self.radioCbr.setSizePolicy(self.sizePolicy)
        
        self.compressArchiveToggleBtn = ToggleSwitch()
        self.compressArchiveToggleBtn.setCheckable(True)
        
        self.compressArchiveToggleBtn.setSizePolicy(self.sizePolicy)
        self.compressArchiveToggleBtn.setObjectName("compressButton")
        

        self.compressArchiveLayout = QHBoxLayout()

        self.compressArchiveLayout.addWidget(self.compressArchiveLabel)
        # self.compressArchiveLayout.addWidget(self.radioCbz)
        # self.compressArchiveLayout.addWidget(self.radioCbr)
        self.compressArchiveLayout.addWidget(self.compressArchiveToggleBtn)

        self.compressArchiveLayout.setStretch(0, 7)
        self.compressArchiveLayout.setStretch(1, 1)
        # self.compressArchiveLayout.setStretch(2, 1)
        # self.compressArchiveLayout.setStretch(3, 1)
        self.compressArchiveLayout.setSpacing(0)

        self.compressArchiveLayout.setContentsMargins(3, 3, 10, 3)

        self.downloadsLayout.addLayout(self.downloadDirPathLayout)
        self.downloadsLayout.addLayout(self.downloadQueueLayout)
        self.downloadsLayout.addLayout(self.compressArchiveLayout)
        

        self.downloadsLayout.setStretch(0, 1)
        self.downloadsLayout.setStretch(1, 15)
        self.downloadsLayout.setStretch(2, 1)

        self.downloadsLayout.setSpacing(0)
        self.downloadsLayout.setContentsMargins(0, 0, 0, 5)
        
        self.downloadDirPathBtn.clicked.connect(lambda: self.selectDownloadDir())

        self.compressArchiveToggleBtn.clicked.connect(lambda: self.compressSelect(self.compressArchiveToggleBtn))

    def compressSelect(self, btn):
        if btn.isChecked():
            self.setting.compressionState = True
            # self.radioCbr.setDisabled(False)
            # self.radioCbz.setDisabled(False)
            
        else:
            self.setting.compressionState = False
            # self.radioCbr.setDisabled(True)
            # self.radioCbz.setDisabled(True)

    def setWindowTheme(self, btn):
        if btn.isChecked():
            self.win_dow.setTheme(1)
        else:
            self.win_dow.setTheme(0)
        self.setting.setPrefVariables()
            
    def themesWidgetObj(self):
        self.themesLabel = QLabel("Dark Theme")
        self.themesBtn = ToggleSwitch()

        self.themeLabelLayout = QHBoxLayout()
        self.themeLabelLayout.addWidget(self.themesLabel)
        self.themeLabelLayout.addWidget(self.themesBtn)

        self.themeLabelLayout.setStretch(0, 10)
        self.themeLabelLayout.setStretch(1, 1)
        


        self.spaceE = QLabel()


        self.spaceEL = QVBoxLayout()
        self.spaceEL.addWidget(self.spaceE, alignment=Qt.AlignmentFlag.AlignCenter)

        self.themesLayout.addLayout(self.themeLabelLayout)
        self.themesLayout.addLayout(self.spaceEL)

        self.themesBtn.clicked.connect(lambda: self.setWindowTheme(self.themesBtn))

    def convertToPath(self, path):
        path_n = Path(path)
        return path_n
        