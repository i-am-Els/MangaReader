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


from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QSizePolicy, QScrollArea
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QCursor, QIcon, QPixmap
import os, consts, resources
from themes import Themes
from linker import Link 
from pathlib import Path
from settings import Settings

class Reader(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.imageList = []
        self.imageCurrent = int()
        self.currentDict = dict()
        self.currentManhuaPath = ''
        self.currentManhuaName = ''
        self.currentChapterIndex = int()
        self.currentIndexPath = ''
        self.currentManhuaChapterLen = int()
        self.currentChapterKey = ''
        self.previousManhuaName = ''
        self.prevPath = ''
        self.manhuaKey = ""
        self.manhuaChanged =  False
        self.size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.max_button_size = QSize(36, 36)
        self.min_button_size = QSize(36, 36)
        self.icon_size = QSize(20, 20)

        self.ifSameChapter = False
        self.majorLayout = QVBoxLayout()

    def setData(self, data: str, index: int = 0) -> None:
        self.currentDict: dict = Settings.libraryMetadata[data]
        self.currentManhuaName = data
        self.currentManhuaPath = self.currentDict["ManhuaPath"] 
        self.currentChapterIndex = index
        self.currentIndexPath = str(self.currentManhuaPath) + "\\" + self.currentDict["Chapters"].get(str(list(self.currentDict["Chapters"].keys())[self.currentChapterIndex]))      
        self.currentManhuaChapterLen = len(self.currentDict["Chapters"])
        self.currentChapterKey = str(list(self.currentDict["Chapters"].keys())[self.currentChapterIndex])

    def backAction(self) -> None:
        Link.callBack(consts.OBJ_MW_NAME, "setFocus")
        self.previousManhuaName = self.currentManhuaName
        Link.callBack(consts.OBJ_WINDOW, "changeStackIndex", consts.E_WINDOW_STACK_MW)

    def calLabelSize(self) -> None:
        if Link.fetchAttribute(consts.OBJ_WINDOW, "currentIndex", True) == consts.E_WINDOW_STACK_READER and Settings.readerDisplayIndex == consts.E_RADIO_SELECTED_WEBTOON:
            self.reScaleMLabel()

    def setState(self, state: list) -> None:
        Settings.readerDisplayIndex = state[0]
        self.hideNav = state[1]
        self.fsState = state[2]

    def selfInit(self) -> None:
        self.majorWidget = QWidget()
        self.setLayout(self.majorLayout)
        self.mainLayout = QHBoxLayout()
        if Settings.readerDisplayIndex == consts.E_RADIO_SELECTED_WEBTOON:
            self.scrollingLayoutInit()
        else:
            self.pagingLayoutInit()
        self.calLabelSize()
        self.majorLayout.addWidget(self.majorWidget)
        self.majorWidget.setLayout(self.mainLayout)

    def scrollingLayoutInit(self) -> None:
        self.leftLayout = QVBoxLayout()
        self.backButton = QPushButton()
        self.backButton.setObjectName(consts.OBJ_READER_BACK_BTN)
        self.backButton.setSizePolicy(self.size_policy)
        self.backButton.setMinimumSize(self.min_button_size)
        self.backButton.setMaximumSize(self.max_button_size)
        self.backButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.backButton.setGeometry(0, 0, 36, 36)
        self.backButton.setToolTip("Return to Description Page")
        self.backButton.setToolTipDuration(consts.TOOLTIP_DURATION)

        self.backIcon = QIcon()
        self.backButton.setIconSize(self.icon_size)
        self.backButton.setCheckable(True)
        self.leftLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.leftLayout.addWidget(self.backButton)

        self.screenLayout = QHBoxLayout()
        self.screenScrollAreaLayout = QVBoxLayout()
        self.screenScrollAreaW = QWidget()
        self.screenLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.screenLayout.setContentsMargins(0, 0, 0,0)
        self.screenScrollAreaLayout.setContentsMargins(0, 0, 0,0)
        self.screenScrollAreaLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        self.screenScrollAreaW.setContentsMargins(0, 0, 0, 0)

        self.setChapterLabels()

        self.spaceEatingWidgetLeft = QWidget()        
        self.spaceEatingWidgetRight = QWidget()
        self.screenScrollAreaW.setLayout(self.screenScrollAreaLayout)

        self.screenLayout.addWidget(self.spaceEatingWidgetLeft)
        self.screenLayout.addWidget(self.screenScrollAreaW)
        self.screenLayout.addWidget(self.spaceEatingWidgetRight)

        self.screenLayout.setStretch(0, 1)
        self.screenLayout.setStretch(1, 2)
        self.screenLayout.setStretch(2, 1)

        self.rightLayout = QVBoxLayout()
        self.setToCoverButton = QPushButton()
        self.setToCoverButton.setObjectName(consts.OBJ_READER_SET_TO_COVER_BTN)
        self.setToCoverButton.setSizePolicy(self.size_policy)
        self.setToCoverButton.setMinimumSize(self.min_button_size)
        self.setToCoverButton.setMaximumSize(self.max_button_size)
        self.setToCoverButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setToCoverButton.setGeometry(0, 0, 36, 36)
        self.setToCoverButton.setToolTip("Set Current Image as Manhua Cover")
        self.setToCoverButton.setToolTipDuration(consts.TOOLTIP_DURATION)

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

    def pagingLayoutInit(self) -> None:
        self.leftLayout = QVBoxLayout()
        self.leftDummyLayout = QVBoxLayout()
        self.backLayout = QVBoxLayout()
        self.previousLayout = QVBoxLayout()
        self.backButton = QPushButton()
        self.backButton.setObjectName(consts.OBJ_READER_BACK_BTN)
        self.backButton.setSizePolicy(self.size_policy)
        self.backButton.setMinimumSize(self.min_button_size)
        self.backButton.setMaximumSize(self.max_button_size)
        self.backButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.backButton.setGeometry(0, 0, 36, 36)
        self.backButton.setToolTip("Return to Description Page")
        self.backButton.setToolTipDuration(consts.TOOLTIP_DURATION)

        self.backIcon = QIcon()
        self.backButton.setIconSize(self.icon_size)
        self.backButton.setCheckable(True)

        self.previousButton = QPushButton()
        self.previousButton.setObjectName(consts.OBJ_READER_PREVIOUS_BTN)
        self.previousButton.setSizePolicy(self.size_policy)
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
        self.manhuaLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        self.nextButton.setObjectName(consts.OBJ_READER_NEXT_BTN)
        self.nextButton.setSizePolicy(self.size_policy)
        self.nextButton.setMinimumSize(self.min_button_size)
        self.nextButton.setMaximumSize(self.max_button_size)
        self.nextButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.nextButton.setGeometry(0, 0, 36, 36)

        self.nextIcon = QIcon()
        self.nextButton.setIconSize(self.icon_size)
        self.nextButton.setCheckable(True)

        self.setToCoverButton = QPushButton()
        self.setToCoverButton.setObjectName(consts.OBJ_READER_SET_TO_COVER_BTN)
        self.setToCoverButton.setSizePolicy(self.size_policy)
        self.setToCoverButton.setMinimumSize(self.min_button_size)
        self.setToCoverButton.setMaximumSize(self.max_button_size)
        self.setToCoverButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setToCoverButton.setGeometry(0, 0, 36, 36)
        self.setToCoverButton.setToolTip("Set Current Image as Manhua Cover")
        self.setToCoverButton.setToolTipDuration(consts.TOOLTIP_DURATION)

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
        self.rightLayout.setStretch(1, 7)
        self.rightLayout.setStretch(2, 1)

        self.mainLayout.addLayout(self.leftLayout)
        self.mainLayout.addLayout(self.screenLayout)
        self.mainLayout.addLayout(self.rightLayout)

        self.mainLayout.setStretch(0, 1)
        self.mainLayout.setStretch(1, 10)
        self.mainLayout.setStretch(2, 1)

        self.backButton.clicked.connect(lambda: self.backAction())
        self.previousButton.clicked.connect(lambda: self.previousAction(Settings.readerDisplayIndex))
        self.nextButton.clicked.connect(lambda: self.nextAction(Settings.readerDisplayIndex))
        self.setToCoverButton.clicked.connect(lambda: self.setToCoverAction())

    def updateLayout(self) -> None:
        self.majorWidget.deleteLater()
        self.selfInit()
        Themes.readerStyle(Settings.readerDisplayIndex)

    def previousAction(self, typeIndex: int) -> None:
        if typeIndex == consts.E_RADIO_SELECTED_LTR:
            if self.imageCurrent > 0:
                self.imageCurrent -= 1
                self.setImageToLabel(self.imageCurrent)
        elif typeIndex == consts.E_RADIO_SELECTED_RTL:
            if self.imageCurrent < (len(self.imageList) - 1):
                self.imageCurrent += 1
                self.setImageToLabel(self.imageCurrent)
    
    def nextAction(self, typeIndex: int) -> None:
        if typeIndex == consts.E_RADIO_SELECTED_LTR:
            if self.imageCurrent < (len(self.imageList) - 1):
                self.imageCurrent += 1
                self.setImageToLabel(self.imageCurrent)
        elif typeIndex == consts.E_RADIO_SELECTED_RTL:
            if self.imageCurrent > 0:
                self.imageCurrent -= 1
                self.setImageToLabel(self.imageCurrent)

    def prevChapter(self) -> None:
        if self.currentChapterIndex > 0:
            currentIndexPath = str(self.currentManhuaPath) + "\\" + self.currentDict["Chapters"].get(str(list(self.currentDict["Chapters"].keys())[self.currentChapterIndex - 1]))
            if os.path.exists(currentIndexPath) and len(os.listdir(currentIndexPath)) != consts.EMPTY:
                self.currentChapterIndex -= 1
                self.currentChapterKey = str(list(self.currentDict["Chapters"].keys())[self.currentChapterIndex])
                self.loadChapterPages(self.currentChapterIndex)
            else:
                Link.callBack(consts.OBJ_LIB_NAME, "reloadManhuaData", self.manhuaKey, (self.currentChapterIndex - 1))
                self.prevChapter()

    def nextChapter(self) -> None:
        if self.currentChapterIndex < (self.currentManhuaChapterLen - 1):
            currentIndexPath = str(self.currentManhuaPath) + "\\" + self.currentDict["Chapters"].get(str(list(self.currentDict["Chapters"].keys())[self.currentChapterIndex + 1]))
            if os.path.exists(currentIndexPath) and len(os.listdir(currentIndexPath)) != consts.EMPTY:
                self.currentChapterIndex += 1
                self.currentChapterKey = str(list(self.currentDict["Chapters"].keys())[self.currentChapterIndex])
                self.loadChapterPages(self.currentChapterIndex)
            else:
                Link.callBack(consts.OBJ_LIB_NAME, "reloadManhuaData", self.manhuaKey, self.currentChapterIndex)
                self.nextChapter()

    def setToCoverAction(self) -> None:
        if Settings.readerDisplayIndex == consts.E_RADIO_SELECTED_WEBTOON:
            n = len(self.imageList)
            v = self.screenScrollArea.verticalScrollBar().value()
            max = self.screenScrollArea.verticalScrollBar().maximum()
            p = (v / max) * 100
            x = int((p/100) * n)
            if x < n:
                imagePath = str(self.currentIndexPath) + "\\" + self.imageList[x]
                Link.callBack(consts.OBJ_LIB_NAME, "setCover", imagePath, self.manhuaKey)
                Link.callBackDeep(consts.OBJ_LIB_NAME, "descriptionPage", "setCover", imagePath)
        else:
            imagePath = str(self.currentIndexPath)  + "\\" + self.imageList[self.imageCurrent]
            Link.callBack(consts.OBJ_LIB_NAME, "setCover", imagePath, self.manhuaKey)
            Link.callBackDeep(consts.OBJ_LIB_NAME, "descriptionPage", "setCover", imagePath)

    def setChapterLabels(self) -> None:
        self.screenScrollArea = QScrollArea()
        self.screenScrollArea.setWidgetResizable(True)
        self.screenScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.screenScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.manhuaLabel = QWidget()

        self.manhuaLayout = QVBoxLayout(self.manhuaLabel)
        self.manhuaLayout.setSpacing(0)
        self.manhuaLayout.setContentsMargins(0, 0, 0, 0)
        # self.manhuaLabel.setLayout(self.manhuaLayout)
        self.screenScrollArea.setWidget(self.manhuaLabel)
        self.setScrollLabelImages()
        self.manhuaLayout.setSpacing(0)
        self.screenScrollAreaLayout.addWidget(self.screenScrollArea)

    def loadChapterPages(self, index: int) -> None:
        self.setFocus()
        self.currentIndexPath = str(self.currentManhuaPath) + "\\" + self.currentDict["Chapters"].get(str(list(self.currentDict["Chapters"].keys())[index])) 
        if os.path.exists(self.currentIndexPath):
            self.currentChapterIndex = index
            self.currentChapterKey = str(list(self.currentDict["Chapters"].keys())[index])
            self.manhuaKey = self.currentDict["ManhuaTitle"]
            self.imageList = []
            self.loadImageList()       
            self.imageCurrent = 0
            if Settings.readerDisplayIndex != consts.E_RADIO_SELECTED_WEBTOON:
                self.setImageToLabel(self.imageCurrent)
            else:
                if self.currentIndexPath != self.prevPath:
                    self.clearLabels()
            self.prevPath = self.currentIndexPath
        else:
            Link.callBack(consts.OBJ_LIB_NAME, "reloadManhuaData", self.manhuaKey, self.currentChapterIndex)

    def loadImageList(self) -> None:
        if os.path.exists(self.currentIndexPath):
            for x in os.listdir(self.currentIndexPath):
                if Path(x).suffix in consts.IMG_EXT_LIST:
                    self.imageList.append(str(x))

    def reScaleMLabel(self) -> None:
        self.setFocus()
        for i in range(self.manhuaLayout.count()):
            layout = self.manhuaLayout.layout()
            item = layout.itemAt(i).widget()
            if type(item) == Reader.ImageLabel:
                pix = item.pixmap()
                item.setPixmap(pix.scaledToWidth(self.screenScrollAreaW.width(), Qt.TransformationMode.SmoothTransformation))

    def setImageToLabel(self, index: int) -> None:
        path = str(self.currentIndexPath) + "\\" + str(self.imageList[index])
        if os.path.exists(path):
            self.manhuaLabel.setPixmap(QPixmap(path))
        else:
            self.imageList.clear()
            self.loadImageList()
            if len(self.imageList) != consts.EMPTY:
                self.imageCurrent = 0
                self.setImageToLabel(self.imageCurrent)
            else:
                Link.callBackDeep(consts.OBJ_LIB_NAME, "descriptionPage", "redisplayChapters")
                Link.callBack(consts.OBJ_WINDOW, "setCurrentIndex", consts.E_WINDOW_STACK_MW)
                Link.callBack(consts.OBJ_LIB_NAME, "setCurrentIndex", consts.E_TAB_LIBRARY_DESCRIPTION_PAGE)

    def setScrollLabelImages(self) -> None:
        self.setFocus()
        for x in self.imageList: 
            path = str(self.currentIndexPath) + "\\" + str(x)
            if os.path.exists(path):
                manhuaLabel = Reader.ImageLabel(path, self.screenScrollAreaW.width())
                self.manhuaLayout.addWidget(manhuaLabel)
            else:
                self.imageList.remove(x)
        self.screenScrollArea.verticalScrollBar().setMaximum(100)

    def clearLabels(self) -> None:
        self.screenScrollArea.deleteLater()
        self.setChapterLabels()
        Themes.readerStyle(Settings.readerDisplayIndex)

    def keyPressEvent(self, event) -> None:
        if Settings.hideNav:
            if Link.fetchAttribute(consts.OBJ_WINDOW, "currentIndex", True) == consts.E_WINDOW_STACK_READER: 
                if event.key() == Qt.Key.Key_A and Settings.readerDisplayIndex != consts.E_RADIO_SELECTED_WEBTOON:
                    if Settings.readerDisplayIndex == consts.E_RADIO_SELECTED_LTR:
                        self.previousAction(consts.E_RADIO_SELECTED_LTR)
                    else:
                        self.previousAction(consts.E_RADIO_SELECTED_RTL)

                elif event.key() == Qt.Key.Key_D and Settings.readerDisplayIndex != consts.E_RADIO_SELECTED_WEBTOON:
                    if Settings.readerDisplayIndex == consts.E_RADIO_SELECTED_LTR:
                        self.nextAction(consts.E_RADIO_SELECTED_LTR)
                    else:
                        self.nextAction(consts.E_RADIO_SELECTED_RTL)

                elif event.key() == Qt.Key.Key_Q:
                    self.prevChapter()

                elif event.key() == Qt.Key.Key_E:
                    self.nextChapter()

    class ImageLabel(QLabel):
        def __init__(self, path: str | Path, width: int):
            super().__init__()
            self.path = path
            # self.width = self.width()
            self.width = width
            self.setScaledContents(True)
            if os.path.exists(self.path):
                self.setPixmap(QPixmap(self.path).scaledToWidth(self.width, Qt.TransformationMode.SmoothTransformation))
            self.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.setStyleSheet("padding: 0px;")
