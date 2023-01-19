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
from linker import Link
import consts
from pathlib import Path
# import os
from settings import Settings
from themes import ToggleSwitch, Themes

class Preference(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.max_button_size = QSize(36, 36)
        self.min_button_size = QSize(36, 36)
        self.icon_size = QSize(20, 20)
        self.active = 0

        self.fontSize1 = 11
        self.fontSize2 = 9
        self.fontSize3 = 8

        self.readerDisplayList = []
        self.settingsToggleIndex = int()
        self.settingsToggleList = []
        self.updatedReaderState = []

        self.downloadDirPath = object()
        self.newPath = object()
        
        self.numCurrent = 0
        self.numDownloaded = 0
        self.totalDownloads = 0
        self.style = str()
        

        self.size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.gridLayout = QGridLayout()

        # Create baseLayout
        self.baseLayout = QVBoxLayout()        
        self.baseLayout.setSpacing(9)

        # Create an horizontal headerLayout
        self.headerLayout = QHBoxLayout()
        self.headerLayout.setContentsMargins(-1, 10, -1, 10)

        self.bodyLayout = QHBoxLayout()

        # Create a backButton
        self.backButton = QPushButton()
        self.backButton.setObjectName(consts.OBJ_PREF_BACK_BTN)

        self.backButton.setSizePolicy(self.size_policy)
        self.backButton.setMinimumSize(self.min_button_size)
        self.backButton.setMaximumSize(self.max_button_size)
        self.backButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.backButton.setGeometry(0, 0, 36, 36)

        # Set backIcon to backButton
        self.backIcon = QIcon()
        
        self.backButton.setIconSize(self.icon_size)
        self.backButton.setCheckable(True)
        self.backButton.setToolTip("Return to Home")
        self.backButton.setToolTipDuration(consts.TOOLTIP_DURATION)

        self.headerLabel = QLabel("Preference | Settings")
        self.headerLabel.setObjectName(consts.OBJ_PREF_HEADER_LABEL)
        self.headerLabel.setSizePolicy(self.size_policy)
        
        self.headerLabelFont = QFont()
        self.headerLabelFont.setPointSize(self.fontSize1)
        self.headerLabelFont.setBold(True)
        self.headerLabel.setFont(self.headerLabelFont)
        self.headerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.headerLayout.addWidget(self.backButton)
        self.headerLayout.addWidget(self.headerLabel)

        self.headerLayout.setStretch(0, 1)
        self.headerLayout.setStretch(1, 9)
        
        self.buttonsLayout = QVBoxLayout()
        self.buttonsLayout.setSpacing(5)

        self.settingsButton = QPushButton("Settings")
        self.settingsButton.setCheckable(True)
        self.settingsButton.setSizePolicy(self.size_policy)
        self.settingsButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settingsButton.setObjectName(consts.OBJ_PREF_SETTINGS_BTN)

        self.downloadButton = QPushButton("Downloads")
        self.downloadButton.setCheckable(True)
        self.downloadButton.setSizePolicy(self.size_policy)
        self.downloadButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.downloadButton.setObjectName(consts.OBJ_PREF_DOWNLOAD_BTN)

        self.themesButton = QPushButton("Themes")
        self.themesButton.setCheckable(True)
        self.themesButton.setSizePolicy(self.size_policy)
        self.themesButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.themesButton.setObjectName(consts.OBJ_PREF_THEME_BTN)

        self.spaceEater = QWidget()
        self.spaceEater.setSizePolicy(self.size_policy)

        self.buttonsLayout.addWidget(self.settingsButton)
        self.buttonsLayout.addWidget(self.downloadButton)
        self.buttonsLayout.addWidget(self.themesButton)
        self.buttonsLayout.addWidget(self.spaceEater)

        self.buttonsLayout.setObjectName("buttonsLayout")

        self.buttonsLayout.setStretch(0, 1)
        self.buttonsLayout.setStretch(1, 1)
        self.buttonsLayout.setStretch(2, 1)
        self.buttonsLayout.setStretch(3, 12)

        self.stackLayout = QVBoxLayout()
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.setSizePolicy(self.size_policy)
        self.stackedWidget.setObjectName(consts.OBJ_PREF_STACK)

        self.settingsWidget = QWidget()
        self.settingsWidget.setObjectName(consts.OBJ_PREF_STACK_SETTINGS)
        self.settingsWidget.setSizePolicy(self.size_policy)
        self.settingsLayout = QVBoxLayout()
        
        self.settingsWidgetObj()

        self.settingsWidget.setLayout(self.settingsLayout)
        

        self.downloadsWidget = QWidget()
        self.downloadsWidget.setObjectName(consts.OBJ_PREF_STACK_DOWNLOAD)
        self.downloadsWidget.setSizePolicy(self.size_policy)
        self.downloadsLayout = QVBoxLayout()

        self.downloadWidgetObj()
        
        self.downloadsWidget.setLayout(self.downloadsLayout)

        self.themesWidget = QWidget()
        self.themesWidget.setObjectName(consts.OBJ_PREF_STACK_THEME)
        self.themesWidget.setSizePolicy(self.size_policy)
        self.themesLayout = QVBoxLayout()

        self.themesWidgetObj()
        
        self.themesWidget.setLayout(self.themesLayout)

        self.stackedWidget.addWidget(self.settingsWidget)
        self.stackedWidget.addWidget(self.downloadsWidget)
        self.stackedWidget.addWidget(self.themesWidget)

        self.stackLayout.addWidget(self.stackedWidget)

        self.bodyLayout.addLayout(self.buttonsLayout)
        self.bodyLayout.addLayout(self.stackLayout)
        self.bodyLayout.setStretch(0, 2)
        self.bodyLayout.setStretch(1, 8)
        
        self.headerBackgroundWidget = QWidget()
        self.headerBackgroundLayout = QVBoxLayout()
        self.headerBackgroundWidget.setLayout(self.headerLayout)
        self.headerBackgroundLayout.addWidget(self.headerBackgroundWidget)

        self.baseLayout.addLayout(self.headerBackgroundLayout)
        self.baseLayout.addLayout(self.bodyLayout)

        self.baseLayout.setStretch(0, 1)
        self.baseLayout.setStretch(1, 11)
        

        self.gridLayout.addLayout(self.baseLayout, 0, 0, 1, 1)

        self.setLayout(self.gridLayout)
        

        self.backButton.clicked.connect(self.backAction)

        self.settingsButton.clicked.connect(lambda: self.setActive(consts.E_ACTIVE_STACK_SETTINGS))

        self.downloadButton.clicked.connect(lambda: self.setActive(consts.E_ACTIVE_STACK_DOWNLOAD))
        
        self.themesButton.clicked.connect(lambda: self.setActive(consts.E_ACTIVE_STACK_THEME))

    def backAction(self) -> None:
        self.updateReaderState()
        Link.callBack(consts.OBJ_WINDOW, "changeStackIndex", consts.E_WINDOW_STACK_MW)

    def updateReaderState(self) -> None:
        Link.callBack(consts.OBJ_READER_NAME, "updateLayout")

    def setActive(self, activeIndex: int) -> None:
        self.active = activeIndex
        Themes.prefSelectedButtonIndex = self.active
        
        Themes.prefButtonActive(self.active, Settings.themeIndex)

        self.stackedWidget.setCurrentIndex(self.active)

    def settingsWidgetObj(self):
        self.libraryLabel = QLabel("Library")
        self.libraryLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.libraryLabel.setSizePolicy(self.size_policy)

        self.libraryLabelFont = QFont()
        self.libraryLabelFont.setBold(True)
        self.libraryLabelFont.setPointSize(self.fontSize1)

        self.libraryLabel.setFont(self.libraryLabelFont)

        self.libraryLabelLayout = QVBoxLayout()
        self.libraryLabelLayout.addWidget(self.libraryLabel)


        self.autoUpdateLabel = QLabel("Auto Update Library")
        self.autoUpdateLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.autoUpdateLabel.setSizePolicy(self.size_policy)
        self.autoUpdateLabelFont = QFont()
        self.autoUpdateLabelFont.setPointSize(self.fontSize2)
        self.autoUpdateLabel.setFont(self.autoUpdateLabelFont)

        self.autoUpdateLabelLayout = QVBoxLayout()
        self.autoUpdateLabelLayout.addWidget(self.autoUpdateLabel)
        

        self.autoUpdateLabelOne = QLabel("Chapters")
        self.autoUpdateLabelOne.setSizePolicy(self.size_policy)

        self.autoUpdateLabelOneFont = QFont()
        self.autoUpdateLabelOneFont.setPointSize(self.fontSize3)
        self.autoUpdateLabelOne.setFont(self.autoUpdateLabelOneFont)

        self.autoUpdateLabelOneLayout = QHBoxLayout()
        
        self.toggleOne = ToggleSwitch()
        self.toggleOne.setCheckable(True)
        self.toggleOne.setSizePolicy(self.size_policy)

        self.autoUpdateLabelOneLayout.addWidget(self.autoUpdateLabelOne)
        self.autoUpdateLabelOneLayout.addWidget(self.toggleOne)


        self.autoUpdateLabelTwo = QLabel("Cover Image and Description")
        self.autoUpdateLabelTwo.setSizePolicy(self.size_policy)

        self.autoUpdateLabelTwoFont = QFont()
        self.autoUpdateLabelTwoFont.setPointSize(self.fontSize3)
        self.autoUpdateLabelTwo.setFont(self.autoUpdateLabelTwoFont)

        self.autoUpdateLabelTwoLayout = QHBoxLayout()

        self.toggleTwo = ToggleSwitch()
        self.toggleTwo.setCheckable(True)
        self.toggleTwo.setSizePolicy(self.size_policy)

        self.autoUpdateLabelTwoLayout.addWidget(self.autoUpdateLabelTwo)
        self.autoUpdateLabelTwoLayout.addWidget(self.toggleTwo)

        self.autoUpdateLabelOneLayout.setContentsMargins(25, 0, 0, 0)
        self.autoUpdateLabelTwoLayout.setContentsMargins(25, 0, 0, 0)

        self.autoUpdateLabelOneLayout.setStretch(0, 10)
        self.autoUpdateLabelOneLayout.setStretch(1, 1)

        self.autoUpdateLabelTwoLayout.setStretch(0, 10)
        self.autoUpdateLabelTwoLayout.setStretch(1, 1)
        

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


        self.readerLabel = QLabel("Reader")
        self.readerLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.readerLabel.setSizePolicy(self.size_policy)

        self.readerLabelFont = QFont()
        self.readerLabelFont.setBold(True)
        self.readerLabelFont.setPointSize(self.fontSize1)

        self.readerLabel.setFont(self.readerLabelFont)

        
        self.readerLabelLayout = QVBoxLayout()
        self.readerLabelLayout.addWidget(self.readerLabel)

        self.readingModeLabel = QLabel("Default Reading Mode")
        self.readingModeLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.readingModeLabel.setSizePolicy(self.size_policy)
        self.readingModeLabelFont = QFont()
        self.readingModeLabelFont.setPointSize(self.fontSize2)
        self.readingModeLabel.setFont(self.readingModeLabelFont)

        self.readingModeLabelLayout = QVBoxLayout()
        self.readingModeLabelLayout.addWidget(self.readingModeLabel)


        self.radioButtonOne = QRadioButton("Left-to-Right")
        self.radioButtonOne.setSizePolicy(self.size_policy)

        self.radioButtonTwo = QRadioButton("Webtoon/Vertical")
        self.radioButtonTwo.setSizePolicy(self.size_policy)
        
        self.radioButtonThree = QRadioButton("Right-to-Left")
        self.radioButtonThree.setSizePolicy(self.size_policy)

        
        self.radioButtonOne.adjustSize()
        
        self.radioButtonTwo.adjustSize()
        
        self.radioButtonThree.adjustSize()

        self.readerDisplayList = [self.radioButtonOne, self.radioButtonTwo, self.radioButtonThree]

        self.radioButtonLayout = QVBoxLayout()

        
        self.radioButtonLayout.addWidget(self.radioButtonOne)
        self.radioButtonLayout.addWidget(self.radioButtonTwo)
        self.radioButtonLayout.addWidget(self.radioButtonThree)

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


        self.readerNavLabel = QLabel("Use Key shortcuts For Navigation\n\tA -> Previous Page | D -> Next Page\n\tQ -> Previous Chapter | E -> Next Chapter")
        self.readerNavLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.readerNavLabel.setSizePolicy(self.size_policy)
        self.readerNavLabelFont = QFont()
        self.readerNavLabelFont.setPointSize(self.fontSize2)
        self.readerNavLabel.setFont(self.readerNavLabelFont)

        self.readerNavtoggle = ToggleSwitch()
        self.readerNavtoggle.setCheckable(True)
        
        self.readerNavtoggle.setSizePolicy(self.size_policy)

        self.readerNavLayout = QHBoxLayout()

        self.readerNavLayout.addWidget(self.readerNavLabel)
        self.readerNavLayout.addWidget(self.readerNavtoggle)

        self.readerNavLayout.setStretch(0, 10)
        self.readerNavLayout.setStretch(1, 1)



        self.readerFSLabel = QLabel("Open reader in fullscreen")
        self.readerFSLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.readerFSLabel.setSizePolicy(self.size_policy)
        self.readerFSLabelFont = QFont()
        self.readerFSLabelFont.setPointSize(self.fontSize2)
        self.readerFSLabel.setFont(self.readerFSLabelFont)

        self.readerFStoggle = ToggleSwitch()
        self.readerFStoggle.setCheckable(True)
        
        self.readerFStoggle.setSizePolicy(self.size_policy)

        self.readerFSLayout = QHBoxLayout()

        self.readerFSLayout.addWidget(self.readerFSLabel)
        self.readerFSLayout.addWidget(self.readerFStoggle)

        self.readerFSLayout.setStretch(0, 10)
        self.readerFSLayout.setStretch(1, 1)



        self.settingsToggleList = [self.toggleOne, self.toggleTwo, self.readerNavtoggle, self.readerFStoggle]

    
        self.spaceEaterForSettings = QWidget()
        self.spaceEaterForSettings.setSizePolicy(self.size_policy)


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


        self.radioButtonOne.toggled.connect(lambda: self.onRadioClicked(consts.E_RADIO_SELECTED_LTR))
        self.radioButtonTwo.toggled.connect(lambda: self.onRadioClicked(consts.E_RADIO_SELECTED_WEBTOON))
        self.radioButtonThree.toggled.connect(lambda: self.onRadioClicked(consts.E_RADIO_SELECTED_RTL))

        self.toggleOne.clicked.connect(lambda: self.onToggleClicked(consts.E_TOGGLE_AUTO_UPDATE, self.toggleOne))
        self.toggleTwo.clicked.connect(lambda: self.onToggleClicked(consts.E_TOGGLE_AUTO_UPDATE_OTHER, self.toggleTwo))
        self.readerNavtoggle.clicked.connect(lambda: self.onToggleClicked(consts.E_TOGGLE_HIDE_NAV, self.readerNavtoggle))
        self.readerFStoggle.clicked.connect(lambda: self.onToggleClicked(consts.E_TOGGLE_FULLSCREEN, self.readerFStoggle))

    def onRadioClicked(self, radioIndex: int) -> None:
        radioBtn = self.sender()
        if radioBtn.isChecked():
            Settings.readerDisplayIndex = radioIndex
        
    def onToggleClicked(self, btnIndex: int, btn: QWidget) -> None:
        self.toggleBtnState = btn.isChecked()
        self.btnIndex = btnIndex
        if self.btnIndex == consts.E_TOGGLE_AUTO_UPDATE:
            Settings.updateChapter = self.toggleBtnState    
        elif self.btnIndex == consts.E_TOGGLE_AUTO_UPDATE_OTHER:
            Settings.updateOther = self.toggleBtnState  
        elif self.btnIndex == consts.E_TOGGLE_HIDE_NAV:
            Settings.hideNav = self.toggleBtnState  
        else:
            Settings.fsState = self.toggleBtnState  

    def selectDownloadDir(self) -> None:
        self.downloadDirDialog = QFileDialog.getExistingDirectory(self,"Select Download Location", self.newPath)

        self.downloadDirPath = self.convertToPath(self.downloadDirDialog)
        if self.downloadDirDialog != "":
            Settings.downloadNewPath = str(self.downloadDirPath)

            self.newPath = Settings.downloadNewPath 

            self.downloadDirPathDisplay.setText(str(self.newPath))
                     
    def downloadWidgetObj(self) -> None:
        self.downloadDirPathLabel = QLabel("Select Download Location")
        
        self.downloadDirPathLabel.setSizePolicy(self.size_policy)

        self.downloadDirPathDisplay = QLabel(str(self.newPath))
        self.downloadDirPathDisplay.setSizePolicy(self.size_policy)
        self.downloadDirPathBtn = QPushButton("Choose")
        self.downloadDirPathBtn.setSizePolicy(self.size_policy)

        self.downloadDirPathLayout = QHBoxLayout()
        
        self.downloadDirPathLayout.addWidget(self.downloadDirPathLabel)
        self.downloadDirPathLayout.addWidget(self.downloadDirPathDisplay)
        self.downloadDirPathLayout.addWidget(self.downloadDirPathBtn)
        self.downloadDirPathLayout.setStretch(0, 3)
        self.downloadDirPathLayout.setStretch(1, 6)
        self.downloadDirPathLayout.setStretch(2, 1)
        
        self.downloadDirPathLayout.setContentsMargins(0, 5, 0, 0)

        self.downloadQueueHeadLabel = QLabel("Download Queue")
        self.downloadQueueHeadLabel.setSizePolicy(self.size_policy)
        
        # self.downloadQueueHeadLabel.setMaximumHeight(60)
        if self.totalDownloads != consts.EMPTY:
            percentDone = self.percentDone()
        else:
            percentDone = consts.EMPTY
        self.downloadQueueStatusLabel = QLabel(f"Downloading {self.numCurrent} of {self.totalDownloads} : {percentDone}% Done")
        self.downloadQueueStatusLabel.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.downloadQueueStatusLabel.setSizePolicy(self.size_policy)

        # self.downloadQueueStatusLabel.setMaximumHeight(60)

        self.downloadQueue = QListWidget()
        self.downloadQueue.setSizePolicy(self.size_policy)
        
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


        self.compressArchiveLabel = QLabel("Compress Downloads to Archive File *.cbz")
        self.compressArchiveLabel.setSizePolicy(self.size_policy)
        
        self.compressArchiveToggleBtn = ToggleSwitch()
        self.compressArchiveToggleBtn.setCheckable(True)
        
        self.compressArchiveToggleBtn.setSizePolicy(self.size_policy)
        self.compressArchiveToggleBtn.setObjectName(consts.OBJ_PREF_COMPRESSED_BTN)
        

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

    def compressSelect(self, btn) -> None:
        if btn.isChecked():
            Settings.compressionState = True
            
        else:
            Settings.compressionState = False

    def setWindowTheme(self, btn) -> None:
        if btn.isChecked():
            Link.callBack(consts.OBJ_WINDOW, "setTheme", consts.E_THEME_DARK_MODE)
        else:
            Link.callBack(consts.OBJ_WINDOW, "setTheme", consts.E_THEME_LIGHT_MODE)
            
    def themesWidgetObj(self) -> None:
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

    def percentDone(self) -> int:
        return ((self.numDownloaded/self.totalDownloads) * 100 )

    def convertToPath(self, path: str) -> Path:
        path_n = Path(path)
        return path_n
    
    def setThemesBtnChecked(self, bool_value: bool) -> None:
        self.themesBtn.setChecked(bool_value)
        