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




from datetime import datetime
from pathlib import Path
import os, re
from themes import Themes
from PyQt6.QtWidgets import (
    QStackedWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QTabWidget,
    QWidget,
    QLineEdit,
    QLabel,
    QSizePolicy,
    QMessageBox,
    QPushButton,
    QFileDialog,
    QComboBox, 
    QScrollArea
)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QCursor, QIcon, QPixmap, QFont

from archive import Archiver


class MainWindow(QWidget):
    def __init__(self, obj, win_dow, window_Icon, appW, parent=None):
        super(MainWindow, self).__init__(parent)
        self.obj = obj
        self.win_dow = win_dow
        self.window_Icon = window_Icon 
        self.appW = appW
        self.max_button_size = QSize(36, 36)
        self.min_button_size = QSize(16, 16)
        self.themeObj = object()
        self.setting = object()
        self.curZipFileList = list()

        self.initPath = object()
        self.newPath = object()
        self.themeIndex = int()
        self.tabIndex = 0
        self.apiIndex = int()

        self.icon_size = QSize(20, 20)
        self.localDirImport = []
        self.localSingleImport = []
        self.history = []
        self.historyData =list()

        self.apiName = []
        self.firstRun = True
        self.launchDone = False

        self.localManhuaTitleDict = dict()
        self.manhuaObj = object()

        self.sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        

        self.create_widgets()

    def create_widgets(self):
        self.gridLayout = QGridLayout()

        # Create a centralLayout to hold all other layouts
        self.centralLayout = QVBoxLayout()
        self.centralLayout.setSpacing(9)

        # Create an horizontal layout to hold all search functions
        self.searchLayout = QHBoxLayout()
        self.searchLayout.setContentsMargins(-1, 10, -1, 10)
        # Create search function widgets

        # Menu/Option button 
        self.menuButton = QPushButton()
        self.menuButton.setCheckable(True)
        
        self.menuButton.setSizePolicy(self.sizePolicy)
        self.menuButton.setMinimumSize(self.min_button_size)
        self.menuButton.setMaximumSize(self.max_button_size)
        self.menuButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.menuIcon = QIcon()
        self.menuButton.setIconSize(self.icon_size)
        self.menuButton.setObjectName("menuButton")
        self.menuButton.setToolTip("Preference Menu")
        self.menuButton.setToolTipDuration(3000)

        # TextBox
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("Enter Search keyword here... e.g 'Shinkeji no Kyojin', 'Bleach', 'Kimetsu no yaiba' etc...")
        
        self.lineEdit.setSizePolicy(self.sizePolicy)
        self.lineEdit.setMinimumSize(QSize(0, 36))
        self.lineEdit.setMaximumSize(QSize(1366, 36))
        self.lineEdit.setMaxLength(36)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit") 

        # Search Button
        self.searchButton = QPushButton()
        self.searchButton.setCheckable(True)
        
        self.searchButton.setSizePolicy(self.sizePolicy)
        self.searchButton.setMinimumSize(self.min_button_size)
        self.searchButton.setMaximumSize(self.max_button_size)
        self.searchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.searchButton.setToolTip("Search Manhua")
        self.searchButton.setToolTipDuration(3000)

        self.searchIcon = QIcon()
        self.searchButton.setIconSize(self.icon_size)
        self.searchButton.setObjectName("searchButton")

        # Local Search
        self.localSearchButton = QPushButton()
        self.localSearchButton.setCheckable(True)
        
        self.localSearchButton.setSizePolicy(self.sizePolicy)
        self.localSearchButton.setMinimumSize(self.min_button_size)
        self.localSearchButton.setMaximumSize(self.max_button_size)
        self.localSearchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.localSearchButton.setToolTip("Load Manhua Bundle from local disk")
        self.localSearchButton.setToolTipDuration(3000)

        self.localSearchIcon = QIcon()
        self.localSearchButton.setIconSize(self.icon_size)
        self.localSearchButton.setObjectName("localSearchButton")

        self.localSearchButtonSingleFormat = QPushButton()
        self.localSearchButtonSingleFormat.setCheckable(True)
        self.localSearchButtonSingleFormat.setSizePolicy(self.sizePolicy)
        self.localSearchButtonSingleFormat.setMinimumSize(self.min_button_size)
        self.localSearchButtonSingleFormat.setMaximumSize(self.max_button_size)
        self.localSearchButtonSingleFormat.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.localSearchButtonSingleFormat.setToolTip("Load Manhua in Archive formats from local disk")
        self.localSearchButtonSingleFormat.setToolTipDuration(3000)

        self.localSearchIconSingleFormat = QIcon()
        self.localSearchButtonSingleFormat.setIconSize(self.icon_size)
        self.localSearchButtonSingleFormat.setObjectName("localSearcButtonSingleFormat")

        self.refreshButton = QPushButton()
        self.refreshButton.setCheckable(True)
        self.refreshButton.setSizePolicy(self.sizePolicy)
        self.refreshButton.setMinimumSize(self.max_button_size)
        self.refreshButton.setMaximumSize(self.max_button_size)
        self.refreshButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.refreshButton.setToolTip("Refresh Home tab")
        self.refreshButton.setToolTipDuration(3000)
        
        self.refreshIcon = QIcon()
        self.refreshButton.setIconSize(self.icon_size)
        self.refreshButton.setObjectName("refreshButton")

        self.apiButton = QPushButton()
        # self.apiButton.addItems(self.apiName)
        self.apiButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.apiButton.setToolTip("Manhua plugin dropdown here...")

        self.apiButton.setCheckable(True)
        self.apiButton.setSizePolicy(self.sizePolicy)
        self.apiButton.setFixedHeight(36)
        self.apiButton.setFixedWidth(100)
        
        self.apiCombo = QComboBox()
        
        self.apiCombo.setSizePolicy(self.sizePolicy)
        self.apiCombo.setFixedHeight(3)
        self.apiCombo.setFixedWidth(3)

        self.apiButtonLayout = QHBoxLayout()
        self.apiButtonLayout.addWidget(self.apiButton)
        self.apiButtonLayout.addWidget(self.apiCombo)

        self.apiButtonLayout.setSpacing(0)
        self.apiButtonLayout.setContentsMargins(0,0, 0, 0)
        self.apiButtonLayout.setStretch(0, 12)
        self.apiButtonLayout.setStretch(1, 1)

        self.apiButtonWidget = QWidget()
        self.apiButtonWidget.setObjectName("apiWidget")
        self.apiButtonWidget.setLayout(self.apiButtonLayout)
        self.apiButtonWidget.setFixedSize(QSize(120, 36))

        # Add Widgets to searchLayout
        self.searchLayout.addWidget(self.menuButton)
        self.searchLayout.addWidget(self.refreshButton)
        self.searchLayout.addWidget(self.localSearchButton)
        self.searchLayout.addWidget(self.localSearchButtonSingleFormat)
        self.searchLayout.addWidget(self.lineEdit)
        self.searchLayout.addWidget(self.searchButton)
        self.searchLayout.addWidget(self.apiButtonWidget)
        
        self.searchLayout.setStretch(0, 1)
        self.searchLayout.setStretch(1, 1)
        self.searchLayout.setStretch(2, 1)
        self.searchLayout.setStretch(3, 1)
        self.searchLayout.setStretch(4, 6)
        self.searchLayout.setStretch(5, 1)
        self.searchLayout.setStretch(6, 1)

        self.searchLayout.setContentsMargins(3, 5, 0, 5)

        # Create another horizontal layout to hold objects of focus
        self.containerLayout = QHBoxLayout()
        # Create a Vetical layout to hold the tabwidget
        self.homeLayout = QVBoxLayout()
        # self.create_home_widgets()***

        # Create a vertical layout to hold the list of previously read manhuas
        self.historyLayout = QVBoxLayout()
        # Create widgets for the historyLayout
        self.historyLabel = QLabel()
        self.historyLabel.setText("Recent Manhua")
        self.historyLabel.setObjectName("historyLabel")
        self.historyLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.historyListView = QWidget()
        self.historyListViewL = QVBoxLayout(self.historyListView)
        self.scroll = QScrollArea(self.historyListView)
        self.scroll.setWidgetResizable(True)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.historyScrollItems()

        self.historyListViewL.setContentsMargins(0, 0, 0, 0)
        self.historyListView.setLayout(self.historyListViewL)

        self.historyListView.setMinimumWidth(320)
        self.historyListView.setObjectName("historyListView")
        self.scrollW.setObjectName("historyScroll")
        self.scroll.setObjectName("scroll")

        self.toggleLayout = QHBoxLayout()

        self.toggleGridView = QPushButton()
        self.toggleGridView.setCheckable(True)
        self.toggleGridView.setObjectName("toggleGridView")

        self.toggleListView = QPushButton()
        self.toggleListView.setCheckable(True)
        self.toggleListView.setObjectName("toggleListView")
        
        self.toggleGridView.setSizePolicy(self.sizePolicy)
        self.toggleGridView.setMinimumSize(self.min_button_size * 1.75)
        self.toggleGridView.setMaximumSize(self.min_button_size * 1.75)
        self.toggleGridView.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        self.toggleListView.setSizePolicy(self.sizePolicy)
        self.toggleListView.setMinimumSize(self.min_button_size * 1.75)
        self.toggleListView.setMaximumSize(self.min_button_size * 1.75)
        self.toggleListView.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.toggleList = [self.toggleGridView, self.toggleListView]
        self.toggleViewValue = ["Grid View", "List View"]

        self.previousViewOptionIndex = 0
        self.viewOptionIndex = 1

        self.view = QLabel(self.toggleViewValue[self.viewOptionIndex])

        self.selectView(self.viewOptionIndex)

        self.toggleLayout.addWidget(self.view)
        self.toggleLayout.addWidget(self.toggleList[0])
        self.toggleLayout.addWidget(self.toggleList[1])

        self.toggleLayout.setStretch(0, 4)
        self.toggleLayout.setStretch(1, 1)
        self.toggleLayout.setStretch(2, 1)

        self.create_home_widgets()

        self.historySubLayout = QVBoxLayout()

        self.historySubLayout.addWidget(self.historyLabel)    
        self.historySubLayout.addWidget(self.historyListView)

        self.historyLayout.addLayout(self.historySubLayout)
        self.historyLayout.addLayout(self.toggleLayout)

        self.historyLayout.setStretch(0, 8)
        self.historyLayout.setStretch(1, 1)
        self.historyLayout.setSpacing(5)

        # Add homeLayout and historyLayout to containerLayout
        self.containerLayout.addLayout(self.homeLayout)
        self.containerLayout.addLayout(self.historyLayout)

        # Set Layout Stretch policy
        self.containerLayout.setStretch(0, 7)
        self.containerLayout.setStretch(1, 3)
        
        #Add searchLayout and containerLayout to centralLayout
        self.centralLayout.addLayout(self.searchLayout)
        self.centralLayout.addLayout(self.containerLayout)
        self.centralLayout.setStretch(0, 2)
        self.centralLayout.setStretch(1, 10)
        
        self.gridLayout.addLayout(self.centralLayout, 0, 0, 1, 1)

        self.setLayout(self.gridLayout)
        
        self.searchButton.clicked.connect(self.search)
        self.lineEdit.returnPressed.connect(self.searchButton.click)
        
        self.menuButton.clicked.connect(self.menuAction)
        self.refreshButton.clicked.connect(self.refreshAction)

        self.apiButton.clicked.connect(lambda:self.apiComboPopUp())

        self.apiCombo.currentIndexChanged.connect(self.setApiIndex)

        self.localSearchButton.clicked.connect(self.localSearchAction)
        # self.localSearchButton.clicked.connect(self.autoAdd)
        self.localSearchButtonSingleFormat.clicked.connect(self.localSearchSingleFormatAction)
        self.tabWidget.currentChanged.connect(lambda:self.changeTabBarIcon())
        self.toggleGridView.clicked.connect( lambda: self.selectViewTypeByObj('toggleGrid'))
        self.toggleListView.clicked.connect(lambda: self.selectViewTypeByObj('toggleList'))


    def historyScrollItems(self):
        self.scrollW = QWidget()

        self.historyScrollL = QVBoxLayout(self.scrollW)
        self.historyScrollL.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll.setWidget(self.scrollW)
        self.historyScrollL.setContentsMargins(5, 10, 5, 10)
        self.reloadHistory()
        self.historyListViewL.addWidget(self.scroll)
        
    def reloadHistory(self):
        # self.historyStorage
        ...

    def resetHistory(self):
        self.scrollW.deleteLater()
        self.historyScrollItems()

    def setApiIndex(self, intIndex):
        clickedIndex = intIndex

        self.apiIndex = clickedIndex
    
        if self.firstRun == True and self.apiIndex == 0:
            self.firstRun = False
        else:
            self.setting.setObjMState()
            self.loadApi(intIndex)

    def apiComboPopUp(self):
        self.apiCombo.showPopup()

    def create_home_widgets(self):
        self.tabWidget = QTabWidget()

        self.home = QWidget()

        self.homeIcon = QIcon()

        self.homeTabStackLayout = QVBoxLayout()

        self.homeTabStack = QStackedWidget()

        # self.loadHomeTab()

        self.homeTabStackLayout.setContentsMargins(0, 0, 0, 0)

        self.homeTabStackLayout.addWidget(self.homeTabStack)

        self.home.setLayout(self.homeTabStackLayout)

        self.library = Library(self.appW, self.win_dow, parent=self)
        self.library.setObjectName("libraryOrigin")
        self.libraryIcon = QIcon() 

        self.tabWidget.addTab(self.home, self.homeIcon, "Home")
        self.tabWidget.addTab(self.library, self.libraryIcon, "Library")
        self.tabWidget.setCurrentIndex(0)
        if self.themeIndex == 0:
            Themes.changeTabBarIconLight(self) # Changes selected tabbar icon
        else:
            Themes.changeTabBarIconDark(self)

        self.tabWidget.setSizePolicy(self.sizePolicy)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setIconSize(QSize(64, 24))

        self.homeLayout.addWidget(self.tabWidget)

    def changeTabBarIcon(self):
        self.tabIndex = self.tabWidget.currentIndex()
        if self.themeIndex == 0:
            Themes.changeTabBarIconLight(self)
        else:
            Themes.changeTabBarIconDark(self)

    def loadApi(self, api_Index):
        ...

    def loadHomeItems(self):# More Work 'Online Mode'
        # self.loadApi(self.apiIndex)
        ...

    def loadHomeLocalItems(self):# More Work 'Offline Mode'
        pass

    def search(self):# More Work
        self.keyword = self.lineEdit.text()
        if self.keyword != "":
            print(self.keyword)

    def menuAction(self):
        self.obj.talkToStackWidgetIndex(2, self.win_dow)

    def refreshAction(self):
        pageToRefreshIndex = self.homeTabStack.currentIndex()
        if self.homeTabStack.currentIndex() == 0:
            print("Refused to change Index will refresh instead")
            self.homeTabStack.setCurrentIndex(0)
        else:
            self.homeTabStack.setCurrentIndex(0)
        self.refresh(pageToRefreshIndex)

    def refresh(self, refreshPgIndex):# Much More work
        if (refreshPgIndex == 0) or (refreshPgIndex == 3):
            self.loadApi(self.apiIndex)

    def changeStackIndex(self, obj, w_index):
        obj.setCurrentIndex(w_index)

    def loadHomeTab(self):
        self.homeDisplay = QWidget()
        self.noInternetDisplay = QWidget()
        self.noSearchResult = QWidget()
        self.searchResultPage = QWidget()
        self.descriptionPage = QWidget()
        
        self.loadHomeDisplay()
        self.loadNoInternetDisplay()
        self.loadNoSearchResult()
        self.loadSearchResultPage()
        self.loadDescriptionPage()      

        self.homeTabStack.addWidget(self.homeDisplay)
        self.homeTabStack.addWidget(self.noInternetDisplay)
        self.homeTabStack.addWidget(self.noSearchResult)
        self.homeTabStack.addWidget(self.searchResultPage)
        self.homeTabStack.addWidget(self.descriptionPage)

        self.homeTabStack.setCurrentIndex(1)
  
    def loadHomeDisplay(self):# More Work
        self.homeDisplayLayout = QGridLayout()
        

        self.homeDisplay.setLayout(self.homeDisplayLayout)

    def loadNoInternetDisplay(self):
        self.noInternetDisplayLayout = QVBoxLayout()

        self.noInternetDisplayLabelpix = QLabel()
        self.noInternetDisplayLabeltxt = QLabel("No Internet Connection")


        self.noInternetDisplayLabelpix.setSizePolicy(self.sizePolicy) 
        self.pixPixmap = QPixmap('resources/icons/icons8-without-internet-100.png')
        self.noInternetDisplayLabelpix.setPixmap(self.pixPixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))
        self.noInternetDisplayLabelpix.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.noInternetDisplayLabeltxt.setSizePolicy(self.sizePolicy)
        #self.noInternetDisplayLabeltxt.setMaximumHeight(50)
        self.noInternetDisplayLabelFont = QFont()
        self.noInternetDisplayLabelFont.setPointSize(16)
        self.noInternetDisplayLabelFont.setBold(False)
        self.noInternetDisplayLabeltxt.setFont(self.noInternetDisplayLabelFont)
        self.noInternetDisplayLabeltxt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.spaceEater1 = QWidget()
        self.spaceEater1.setSizePolicy(self.sizePolicy)

        self.spaceEater2 = QWidget()
        self.spaceEater2.setSizePolicy(self.sizePolicy)

        self.noInternetDisplayLayout.addWidget(self.spaceEater1)
        self.noInternetDisplayLayout.addWidget(self.noInternetDisplayLabelpix)
        self.noInternetDisplayLayout.addWidget(self.noInternetDisplayLabeltxt)
        self.noInternetDisplayLayout.addWidget(self.spaceEater2)


        self.noInternetDisplayLayout.setStretch(0, 5)
        self.noInternetDisplayLayout.setStretch(1, 1)
        self.noInternetDisplayLayout.setStretch(2, 1)
        self.noInternetDisplayLayout.setStretch(3, 6)

        self.noInternetDisplay.setLayout(self.noInternetDisplayLayout)

    def loadNoSearchResult(self):
        self.noSearchResultLayout = QVBoxLayout()

        self.noSearchResultLabelpix = QLabel()
        self.noSearchResultLabeltxt = QLabel("Keyword not Found")


        self.noSearchResultLabelpix.setSizePolicy(self.sizePolicy) 
        self.spixPixmap = QPixmap('resources/icons/page-not-found.png')
        self.noSearchResultLabelpix.setPixmap(self.spixPixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))
        self.noSearchResultLabelpix.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.noSearchResultLabeltxt.setSizePolicy(self.sizePolicy)
        #self.noInternetDisplayLabeltxt.setMaximumHeight(50)
        self.noSearchResultLabelFont = QFont()
        self.noSearchResultLabelFont.setPointSize(16)
        self.noSearchResultLabelFont.setBold(False)
        self.noSearchResultLabeltxt.setFont(self.noSearchResultLabelFont)
        self.noSearchResultLabeltxt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.spaceEater1 = QWidget()
        self.spaceEater1.setSizePolicy(self.sizePolicy)

        self.spaceEater2 = QWidget()
        self.spaceEater2.setSizePolicy(self.sizePolicy)

        self.noSearchResultLayout.addWidget(self.spaceEater1)
        self.noSearchResultLayout.addWidget(self.noSearchResultLabelpix)
        self.noSearchResultLayout.addWidget(self.noSearchResultLabeltxt)
        self.noSearchResultLayout.addWidget(self.spaceEater2)


        self.noSearchResultLayout.setStretch(0, 5)
        self.noSearchResultLayout.setStretch(1, 1)
        self.noSearchResultLayout.setStretch(2, 1)
        self.noSearchResultLayout.setStretch(3, 6)

        self.noSearchResult.setLayout(self.noSearchResultLayout)

    def loadSearchResultPage(self):
        self.resultLayout = QGridLayout()

    def loadDescriptionPage(self):
        self.descriptionLayout = QHBoxLayout()
        pass

    def viewTypeAction(self, gridView):
        if gridView == True:
            self.toggleGridIcon = QIcon()
            self.toggleGridIcon.addPixmap(QPixmap("resources/icons/icons8-grid-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.toggleGridView.setIcon(self.toggleGridIcon)
            self.toggleGridView.setIconSize(self.icon_size * 1.1)
            
            self.toggleListDisabledIcon =QIcon()
            self.toggleListDisabledIcon.addPixmap(QPixmap("resources/icons/icons8-list-disabled-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.toggleListView.setIcon(self.toggleListDisabledIcon)
            self.toggleListView.setIconSize(self.icon_size * 1.1)

            self.view.setText("Grid View")
            self.previousViewOptionIndex = 0

            if self.launchDone:
                self.library.switchLayout()
                
            return self.viewOptionIndex, self.previousViewOptionIndex

        else:
            self.toggleListIcon = QIcon()
            self.toggleListIcon.addPixmap(QPixmap("resources/icons/icons8-list-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.toggleListView.setIcon(self.toggleListIcon)
            self.toggleListView.setIconSize(self.icon_size * 1.1)
            
            self.toggleGridDisabledIcon = QIcon()
            self.toggleGridDisabledIcon.addPixmap(QPixmap("resources/icons/icons8-grid-disabled-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.toggleGridView.setIcon(self.toggleGridDisabledIcon)
            self.toggleGridView.setIconSize(self.icon_size * 1.1)

            self.view.setText("List View")
            self.previousViewOptionIndex = 1

            if self.launchDone:
                self.library.switchLayout()
            return self.viewOptionIndex, self.previousViewOptionIndex
    
    def selectViewTypeByObj(self, objName):
        if objName == "toggleGrid":
            self.viewOptionIndex = 0
            self.selectView(self.viewOptionIndex)
        else:
            self.viewOptionIndex = 1
            self.selectView(self.viewOptionIndex)

    def selectView(self, view_index):
        if view_index == 0 and view_index != self.previousViewOptionIndex:
            self.viewIsGrid = True
            self.viewTypeAction(self.viewIsGrid)
        else:
            if view_index == 1 and view_index != self.previousViewOptionIndex:
                self.viewIsGrid = False
                self.viewTypeAction(self.viewIsGrid)
   
    def popDialog(self, type):
        if type == 'empty':
            txt, t_txt = "Bundle is empty, Please select a filled directory", "Empty Bundle Error"
        elif type == 'structure':
            txt, t_txt = "There are 2 scenarios that raise this error: Bundle Structure Error or No Image Found\nTip 1: Select a Parent folder that has chapters arranged in sub-folders.\nTip 2: The chapter sub-folders MUST contain images.", "Structure or File Error"
        elif type == 'badFile':
            txt, t_txt = "The supposed archive file might contain a bad or corrupted file...\nUnable to completely read archive.", "Bad/Corrupted Archive File"
        elif type == 'none':
            txt, t_txt = "Selected file is not a valid archive file. Select A readable archive file such as '.cbz', '.zip' files.", "Not an Archive File"
        elif type == 'duplicate':
            txt, t_txt = "The manhua title already exists in your library, select another title", "Duplicate Action"
        
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Icon.Information)
        messageBox.setText(txt)
        messageBox.setWindowTitle(t_txt)
        messageBox.setStandardButtons(QMessageBox.StandardButton.Ok)
        messageBox.setWindowIcon(self.window_Icon)
        messageBox.exec()

    def localSearchAction(self):
        self.localDirDialog = QFileDialog.getExistingDirectory(self,"Select Manhua Title",self.newPath)

        self.localDirPath = self.convertToPath(self.localDirDialog)
        dir = list(os.listdir(self.localDirPath))
        

        if len(dir) == 0:
            self.popDialog('empty')
            self.localSearchAction()

        elif self.localDirDialog == '':
            pass

        elif self.localDirDialog != '' and len(dir) != 0:
            rightStructure = self.library.correctDirStructure(self.localDirPath)
            if rightStructure == True:
                self.newPath = self.extractParentFolderPath(self.localDirPath)
                self.setting.libraryNewPath = self.newPath

                self.library.addToLibrary(self.localDirPath)
            else:
                self.popDialog('structure')
                self.localSearchAction()

    def localSearchSingleFormatAction(self):
        self.localSingleDialog = QFileDialog().getOpenFileName(self, 'Open Archived Manhua File', self.newPath, 'Archived Files (*.cbz *zip)')
        self.localSinglePath = self.convertToPath(self.localSingleDialog[0])

        if os.path.isfile(self.localSinglePath) and Path(self.localSinglePath).suffix in ['.cbz', '.zip']:  
            self.localFileName = self.extractFileName(self.localSinglePath)

            self.parentLocalSinglePath = self.extractParentFolderPath(self.localSinglePath)

            self.localSingleImport = [self.localSinglePath, self.localFileName, self.parentLocalSinglePath]
            self.newPath = self.parentLocalSinglePath

            self.setting.libraryNewPath = self.newPath

            ziper = Archiver()
            outPath = Path(self.setting.extractionNewPath + str(Path(self.localFileName).stem) + "\\")
            print(outPath)
            if not os.path.exists(outPath):
                os.makedirs(outPath)
            # self.curZipFileList = ziper.extractCbz(self.localSinglePath, outPath, self)
            # self.library.libraryArchiveMetaDataList = self.curZipFileList
            # Library.launchArchiveReader(self.curZipFileList)

        elif self.localSingleDialog == ('', ''):
            pass

        elif not(os.path.isfile(self.localSinglePath)):
            self.popDialog('none')
            self.localSearchSingleFormatAction()
        
    def convertToPath(self, path):
        path_n = Path(path)
        return path_n

    def extractParentFolderPath(self, path):
        path_n = os.path.dirname(path)
        return path_n

    def extractFileName(self, path):
        file_n = os.path.basename(path)
        return file_n


class Library(QStackedWidget):
    def __init__(self, appW, window, parent):
        super(Library, self).__init__(parent)
        self.parent = parent
        self.sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.gridX = 0
        self.gridY = 0
        self.gridYLimit = 7
        self.appW = appW
        self.win_dow = window
        self.previousOpen = ""

        self.libraryMetadata = dict()
        self.libraryListdata = list()
        self.libraryArchiveMetaDataList = dict()

        self.noItems = QWidget()
        self.libraryShelf = QWidget()
        self.descriptionPage = Description(self)
        
        self.addWidget(self.noItems)
        self.addWidget(self.libraryShelf)
        self.addWidget(self.descriptionPage)
        
        self.setCurrentIndex(0)

        self.setNoItemsWidget()

        self.loadLibraryLayout()
        self.parent.launchDone = True

    def setNoItemsWidget(self):
        self.noItemsLabel = QLabel()
        self.noItemsPixmap = QPixmap("resources/icons/digital-library.png")
        self.noItemsLabel.setPixmap(self.noItemsPixmap.scaled(256, 256, Qt.AspectRatioMode.KeepAspectRatio))
        self.noItemsLayout = QVBoxLayout()
        self.noItemsLayout.addWidget(self.noItemsLabel, alignment=Qt.AlignmentFlag.AlignCenter)

        self.noItems.setLayout(self.noItemsLayout)

    def loadLibraryItems(self):
        self.libraryScrollAreaWidget = QWidget()

        if self.parent.viewIsGrid:
            self.libraryShelfGridLayout = QGridLayout(self.libraryScrollAreaWidget)
            self.libraryScrollArea.setWidget(self.libraryScrollAreaWidget)
            self.libraryShelfGridLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
            self.libraryShelfGridLayout.setDefaultPositioning(0, Qt.Orientation.Horizontal)
            self.libraryShelfGridLayout.setContentsMargins(5, 10, 5, 10)
            self.libraryShelfGridLayout.setSpacing(10)

        else:
            self.libraryShelfListLayout = QVBoxLayout(self.libraryScrollAreaWidget)
            self.libraryShelfListLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
            self.libraryScrollArea.setWidget(self.libraryScrollAreaWidget)
            self.libraryShelfListLayout.setContentsMargins(5, 10, 5, 10)

        self.recreateManhuas()

        if self.parent.viewIsGrid:
            if self.appW.windowState() == Qt.WindowState.WindowMaximized or self.appW.windowState() == Qt.WindowState.WindowFullScreen:
                self.libraryMaximized()
            elif self.appW.windowState() == Qt.WindowState.WindowNoState or self.appW.windowState() == Qt.WindowState.WindowActive:
                self.libraryResized()
        else:
            self.libraryListReDisplay()

        self.libraryShelfLayout.addWidget(self.libraryScrollArea)
        
    def loadLibraryLayout(self):
        self.libraryShelfLayout = QVBoxLayout(self.libraryShelf)
        self.libraryShelfLayout.setContentsMargins(0, 0, 0, 0)

        self.libraryScrollArea = QScrollArea(self.libraryShelf)
        self.libraryScrollArea.setWidgetResizable(True)
        self.libraryScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.loadLibraryItems()
        self.libraryShelf.setLayout(self.libraryShelfLayout)

    def addToLibraryAction(self, manhuaObj):
        self.calculateLibraryDimension()
        spacing = self.calculateLibrarySpacing()
        if self.parent.viewIsGrid:
            self.libraryShelfGridLayout.setSpacing(spacing)
            if self.gridYLimit >= self.gridY: 
                self.libraryShelfGridLayout.addWidget(manhuaObj, self.gridX, self.gridY)
            else:
                self.gridY = 0
                self.gridX += 1
                self.libraryShelfGridLayout.addWidget(manhuaObj, self.gridX, self.gridY)
            self.gridY += 1
        else:
            self.libraryShelfListLayout.addWidget(manhuaObj)
        self.parent.tabWidget.setCurrentIndex(1)
        self.setCurrentIndex(1)

    def libraryMaximized(self):
        dimension = self.calculateLibraryDimension()
        spacing = self.calculateLibrarySpacing()
        self.libraryDisplayChangeAction(dimension, spacing)
        
    def libraryResized(self):
        dimension = self.calculateLibraryDimension()
        spacing = self.calculateLibrarySpacing()
        self.libraryDisplayChangeAction(dimension, spacing)

    def libraryDisplayChangeAction(self, limit, spacing):
        self.gridYLimit = limit
        self.libraryItemLength = len(self.libraryListdata)
        
        self.libraryShelfGridLayout.setSpacing(spacing)

        if self.libraryItemLength != 0:
            xLen = int(self.libraryItemLength / (limit + 1))
            if self.libraryItemLength % (limit + 1) != 0:
                xLen += 1
            i = 0
            for x in range(xLen):
                for y  in range(limit + 1):
                    if i < self.libraryItemLength:
                        self.libraryShelfGridLayout.addWidget(self.libraryListdata[i], x, y)
                        self.gridX = x
                        self.gridY = y + 1
                        i += 1
                    else:
                        break

    def libraryListReDisplay(self):
        self.libraryItemLength = len(self.libraryListdata)
        if self.libraryItemLength != 0:
            for x in range(self.libraryItemLength):
                # self.libraryListdata[x].switchVariant("grid")
                self.libraryShelfListLayout.addWidget(self.libraryListdata[x])

    def correctDirStructure(self, path):
        correct = False
        imageExtList = ['.jpeg', '.jpg', '.png']

        for x in os.listdir(path):
            xPath = os.path.join(path, x)
            if os.path.isdir(xPath):
                correct = not(any(os.path.isdir(os.path.join(xPath, y)) == True for y in os.listdir(xPath))) and any((Path(os.path.join(xPath, y)).suffix in imageExtList) for y in os.listdir(xPath))
                if correct == True:
                    break
        return correct

    def addToLibrary(self, path):
        manhuaMetaDict = dict()
        manhuaChapterList = list()

        manhuaMetaDict["ManhuaTitle"] = Path(path).stem
        manhuaMetaDict["ManhuaPath"] = str(path)
        emptyCover = True

        for x in os.listdir(path):
            xPath = os.path.join(path, x)
            if os.path.isdir(xPath):
                # sChapterName = str(Path(xPath).name)
                sChapterName = Path(xPath).name
                manhuaChapterList.append(sChapterName)
            elif Path(xPath).suffix in ['.jpeg', '.jpg', '.png'] and emptyCover == True:
                manhuaMetaDict["ManhuaCover"] = xPath
                emptyCover = False
        if emptyCover == True:
            manhuaMetaDict["ManhuaCover"] = self.parent.themeObj.defaultCoverImage
            
        sortedManhuaChapterDict = self.sortChapters(manhuaChapterList)
        manhuaMetaDict["Chapters"] = sortedManhuaChapterDict
        manhuaMetaDict["IsFav"] = False
        manhuaMetaDict["Status"] = "Local Manhua Bundle"
        manhuaMetaDict["Description"] = "No Description... This file is a locally imported file, metadata consist of no description..."

        if not((manhuaMetaDict["ManhuaTitle"]) in self.libraryMetadata):
            self.libraryMetadata.update({manhuaMetaDict["ManhuaTitle"] : manhuaMetaDict})
            self.manhuaObj = Manhua(self.libraryMetadata[manhuaMetaDict["ManhuaTitle"]], self)
            self.libraryListdata.append(self.manhuaObj)
            self.addToLibraryAction(self.manhuaObj)
        else:
            self.parent.popDialog('duplicate')

    def sortChapters(self, someList):
        newSortedDict = dict()
        initIndexHolderList = list()
        indexHolderList = list()
        chapterNameList = list()
        for item in someList:
            dTxt = re.findall(r"((ch+(ap)?(ter)?)+(\W|_)*(\d+(?:\.\d+)?))", str(item).casefold())
            desiredTxt = dTxt[0]
            initIndexHolderList.append(desiredTxt[-1])
            if '.' in desiredTxt[-1]:
                indexHolderList.append(float(desiredTxt[-1]))
            else:
                indexHolderList.append(int(desiredTxt[-1]))
            chapterName = 'Chapter ' + str(desiredTxt[-1])
            chapterNameList.append(chapterName)
        indexHolderList.sort()
        for i in indexHolderList:
            for j in initIndexHolderList:
                if str(i) == j:
                    ind = initIndexHolderList.index(j)
                    newSortedDict.update({chapterNameList[ind] : someList[ind]})
        return newSortedDict

    def recreateManhuas(self):
        self.libraryListdata.clear()
        for k in self.libraryMetadata.keys():
            self.manhuaObj = Manhua(self.libraryMetadata[k], self)
            self.libraryListdata.append(self.manhuaObj)

    def switchLayout(self):
        self.libraryScrollAreaWidget.deleteLater()
        self.loadLibraryItems()

    def openDescription(self, dataDict):
        if dataDict["ManhuaTitle"] != self.previousOpen:
            self.descriptionPage.setData(dataDict)
            self.descriptionPage.resetChapters()
            self.win_dow.objReader.setData(dataDict["ManhuaTitle"])
            self.win_dow.objReader.previousManhuaName = self.previousOpen
            self.previousOpen = dataDict["ManhuaTitle"]

        self.setCurrentIndex(2)

    def calculateLibraryDimension(self):
        dimensionV = self.geometry().width()

        dimension = int(dimensionV / Manhua.manhuaSize.width()) - 2
        self.gridYLimit = dimension
        return dimension

    def calculateLibrarySpacing(self):
        spacingV = self.geometry().width()
        dimension = int(spacingV / Manhua.manhuaSize.width()) - 1
        spacing = spacingV - (Manhua.manhuaSize.width() * dimension)
        spacing = int(spacing / dimension)
        return spacing

    def launchReader(self, index):
        if(self.win_dow.objReader.fsState == True and self.appW.windowState() != Qt.WindowState.WindowMaximized):
            self.appW.customTitleBar.toggleRestore()
        self.win_dow.objReader.loadChapterPages(index)
        self.win_dow.objReader.setFocus()
        self.win_dow.setCurrentIndex(1)

    def setCover(self, path, manhuaName):
        self.libraryMetadata[manhuaName]["ManhuaCover"] = str(path)
        manhuasData = list(self.libraryMetadata.keys())
        index = manhuasData.index(manhuaName)
        self.libraryListdata[index].manhuaCoverPixmap = QPixmap(str(path)).scaled(90, 120, Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.libraryListdata[index].manhuaCoverDisplayLabel.setPixmap(self.libraryListdata[index].manhuaCoverPixmap)

    @staticmethod
    def launchArchiveReader(info):
        
        ...

class History(QPushButton):
    def __init__(self, manhuaName, chapter, index, path, parent):
        super().__init__()
        self.manhuaName = manhuaName
        # self.dataDict = self.parent.win_dow.objMainWindow.library.libraryMetadata[self.manhuaName]
        self.chapter = chapter
        self.chapterIndex = index
        self.path = path
        self.time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.parent = parent
        self.labelString = f"{self.manhuaName} - {self.chapter}\n{self.time}"
        self.setText(self.labelString)
         
        self.setStyleSheet("QPushButton{ text-align:  left; border-radius: 5px; padding-left: 10px;} QPushButton:hover { color: white; }")
        self.setMinimumHeight(50)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.clicked.connect(lambda: self.launchHistory())
        self.dict = dict()
        self.dict["ManhuaName"] = self.manhuaName
        self.dict["Chapter"] = self.chapter
        self.dict["ChapterIndex"] = self.chapterIndex
        self.dict["ChapterPath"] = self.path
        self.dict["ReadTime"] = self.time
        
    def launchHistory(self):
        self.parent.setData(self.manhuaName, self.chapterIndex)
        self.parent.win_dow.objMainWindow.library.launchReader(self.chapterIndex)

    def setValues(self, chapter, index, path):
        self.chapter = chapter
        self.chapterIndex = index
        self.path = path
        self.time = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.labelString = f"{self.manhuaName} - {self.chapter}\n{self.time}"
        self.dict["Chapter"] = self.chapter
        self.dict["ChapterIndex"] = self.chapterIndex
        self.dict["ChapterPath"] = self.path
        self.dict["ReadTime"] = self.time
        self.setText(self.labelString)



        

class Chapter(QPushButton):
    def __init__(self, sTitle, pTitlePath, index, parent):
        super().__init__()
        self.title = sTitle
        self.titlePath = pTitlePath
        self.parent = parent
        self.index = index
        
        self.fm = self.fontMetrics()
        self.pathText = self.titlePath
        self.elidedText = self.fm.elidedText(self.pathText, Qt.TextElideMode.ElideMiddle, 250)

        self.labelString = f"{self.title} \n{self.elidedText}"
        self.setText(self.labelString)
        self.setStyleSheet("QPushButton{ text-align:  left; border-radius: 5px; padding-left: 10px;} QPushButton:hover { color: white; }")
        self.setMinimumHeight(50)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.clicked.connect(lambda: self.parent.launchReader(self.index))



class Manhua(QPushButton):
    manhuaSize = QSize(120, 170)
    
    def __init__(self, metadata, parent=None):
        super(Manhua, self).__init__(parent)
        self.metadata: dict = metadata
        self.parent = parent
        self.setCheckable(True)
        # self.setChecked(False)
        self.manhuaName = metadata["ManhuaTitle"]
        self.manhuaPath = Path(metadata["ManhuaPath"])
        self.manhuaCover = Path(metadata["ManhuaCover"])
        self.manhuaChapters = metadata["Chapters"]
        self.manhuaId = metadata["ManhuaTitle"]
        self.isFavorite = metadata["IsFav"]
        self.bookmarkPosition = object()
        self.sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setObjectName(self.manhuaName)
        
        

        # self.manhuaCoverLabel = QLabel()  #Holds the description page image
        self.recreateObjectWidgets()
       
        if self.parent.parent.viewIsGrid:
            self.manhuaBgLayoutGrid = QVBoxLayout()
            self.displayGridVariant()
        else:
            self.manhuaBgLayoutList = QHBoxLayout()
            self.displayListVariant()

        self.clicked.connect(lambda: self.parent.openDescription(self.metadata))
        
    def recreateObjectWidgets(self):
        self.manhuaCoverDisplayLabel = QLabel()
        self.manhuaCoverDisplayLabel.setObjectName("manhuaLabel")
        self.manhuaCoverDisplayLabel.setSizePolicy(self.sizePolicy)
        self.manhuaCoverLayout = QVBoxLayout()
        self.manhuaDetailsLayout = QHBoxLayout()
        self.manhuaDetailsLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # self.manhuaDetailsWidget = QWidget()
        self.manhuaNameLabel = QLabel()
        self.manhuaNameLabel.setObjectName("nameLabel")
        self.manhuaFavoriteButton = QPushButton()
        self.manhuaFavoriteButton.setSizePolicy(self.sizePolicy)
        self.manhuaFavoriteButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.manhuaFavoriteButtonIcon = QIcon()

        self.manhuaCoverPixmap = QPixmap(str(self.manhuaCover)).scaled(90, 120, Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.manhuaCoverDisplayLabel.setPixmap(self.manhuaCoverPixmap)
        self.manhuaCoverLayout.addWidget(self.manhuaCoverDisplayLabel)
        self.manhuaCoverLayout.setSpacing(0)
        self.manhuaCoverLayout.setContentsMargins(0, 0, 0, 0)

        self.manhuaNameLabel.setText(self.manhuaName)
        self.manhuaNameLabel.setSizePolicy(self.sizePolicy)
        self.manhuaNameLabelFont = QFont()
        self.manhuaNameLabelFont.setPointSize(7)
        self.manhuaNameLabelFont.setBold(False)
        self.manhuaNameLabel.setFont(self.manhuaNameLabelFont)
        self.manhuaNameLabel.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.manhuaNameLabel.setMaximumHeight(20)

        self.manhuaFavoriteButtonIcon.addPixmap(QPixmap("resources/icons/icons8-favourite-64.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.manhuaFavoriteButton.setIcon(self.manhuaFavoriteButtonIcon)
        self.manhuaFavoriteButton.setFixedSize(QSize(20, 20))
        self.manhuaFavoriteButton.setObjectName("fav")

        # self.manhuaDetailsWidget.setLayout(self.manhuaDetailsLayout)
        self.manhuaDetailsLayout.addWidget(self.manhuaNameLabel)
        self.manhuaDetailsLayout.addWidget(self.manhuaFavoriteButton)

        self.manhuaCoverDisplayLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.checkFav(self.isFavorite)

        self.setStyleSheet(" QLabel#manhuaLabel{ padding: 7px; border-radius: 5px; background-color: white; border: none;}  QLabel#nameLabel{ padding: 1px; border-radius: 5px;} QPushButton#fav { background: rgb(147,148,165);  border: none; border-radius: 5px;} QPushButton#fav:hover { background-color: rgb(72,75,106)} .Manhua { border-radius: 5px; background-color: white;} .Manhua:hover{ background: rgba(0, 0, 0, 40); }")

        self.manhuaFavoriteButton.clicked.connect(lambda: self.favorite(self.isFavorite))

    def displayGridVariant(self):
        self.manhuaDetailsLayout.setStretch(0, 7)
        self.manhuaDetailsLayout.setStretch(1, 2)
        self.manhuaDetailsLayout.setSpacing(1)
        self.manhuaDetailsLayout.setContentsMargins(0, 0, 0, 0)

        self.manhuaBgLayoutGrid.addLayout(self.manhuaCoverLayout)
        self.manhuaBgLayoutGrid.addLayout(self.manhuaDetailsLayout)

        self.manhuaBgLayoutGrid.setStretch(0, 7)
        self.manhuaBgLayoutGrid.setStretch(1, 1)
        self.manhuaBgLayoutGrid.setSpacing(1)
        self.manhuaBgLayoutGrid.setContentsMargins(5, 5, 5, 10)
        
        self.setLayout(self.manhuaBgLayoutGrid)
        self.setMaximumSize(self.manhuaSize)
        self.setMinimumSize(self.manhuaSize)
    
    def displayListVariant(self):
        self.manhuaDetailsLayout.setStretch(0, 10)
        self.manhuaDetailsLayout.setStretch(1, 1)
        self.manhuaDetailsLayout.setSpacing(1)
        self.manhuaDetailsLayout.setContentsMargins(0, 0, 0, 0)

        self.manhuaBgLayoutList.addLayout(self.manhuaCoverLayout)
        self.manhuaBgLayoutList.addLayout(self.manhuaDetailsLayout)

        self.manhuaBgLayoutList.setStretch(0, 1)
        self.manhuaBgLayoutList.setStretch(1, 7)
        self.manhuaBgLayoutList.setSpacing(1)
        self.manhuaBgLayoutList.setContentsMargins(5, 5, 5, 10)

        self.setLayout(self.manhuaBgLayoutList)
        self.setMinimumHeight(140)
        self.setMaximumHeight(140)

    def checkFav(self, isFavorite):
        if isFavorite == False:
            self.removeFavorite()
        else:
            self.addToFavorite()

    def favorite(self, isFavorite):
        if isFavorite == False:
            self.addToFavorite()
            self.isFavorite = True
        else:
            self.removeFavorite()
            self.isFavorite = False

    def addToFavorite(self):
        self.manhuaFavoriteButtonIcon.addPixmap(QPixmap("resources/icons/icons8-favourite-checked-64.png"))
        self.manhuaFavoriteButton.setIcon(self.manhuaFavoriteButtonIcon)
        self.parent.libraryMetadata[self.manhuaName]["IsFav"] = True
        ...
    
    def removeFavorite(self):
        self.manhuaFavoriteButtonIcon.addPixmap(QPixmap("resources/icons/icons8-favourite-64.png"))
        self.manhuaFavoriteButton.setIcon(self.manhuaFavoriteButtonIcon)
        self.parent.libraryMetadata[self.manhuaName]["IsFav"] = False

    def deleteSelf(self):
        ...
        
    

class Description(QWidget):
    def __init__(self, parent):
        super(Description, self).__init__(parent)
        self.sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.max_button_size = QSize(36, 36)
        self.min_button_size = QSize(16, 16)
        self.icon_size = QSize(20, 20)
        self.parent = parent
        self.launchDone = False
        self.dataDict = dict()
        self.descChapters = dict()
        self.chapterLen = int()
        self.createDescriptionWidget()
        self.launchDone = True

        self.exitButton.clicked.connect(lambda: self.exitPage())
        self.setObjectName("descPage")
        
    def createDescriptionWidget(self):
        self.mainLayout = QHBoxLayout()
        
        self.infoLayout = QVBoxLayout()
        
        self.infoHeaderLayout = QHBoxLayout()
        self.exitButton = QPushButton()
        self.exitButton.setObjectName("backDescButton")

        self.exitButton.setSizePolicy(self.sizePolicy)
        self.exitButton.setMinimumSize(self.min_button_size)
        self.exitButton.setMaximumSize(self.max_button_size)
        self.exitButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.exitButton.setGeometry(0, 0, 36, 36)
        self.exitButton.setToolTip("Return to Home")
        self.exitButton.setToolTipDuration(3000)
        self.exitButtonIcon = QIcon()
        self.exitButton.setIconSize(self.icon_size)
        self.exitButton.setCheckable(True)

        self.modeTag = QLabel()
        self.infoHeaderLayout.addWidget(self.exitButton)
        self.infoHeaderLayout.addWidget(self.modeTag)

        self.infoDescriptionLayout = QHBoxLayout()
        self.nameLabel = QLabel()
        self.synopsisLabel = QLabel()
        self.nameLabelQ = QWidget()
        self.nameLabelL = QVBoxLayout(self.nameLabelQ)

        self.nameLabelL.addWidget(self.nameLabel) 
        self.nameLabelL.addWidget(self.synopsisLabel) 

        self.nameLabelL.setStretch(0, 1)
        self.nameLabelL.setStretch(1, 4)
        self.nameLabelL.setSpacing(1)
        self.nameLabelL.setContentsMargins(0, 0, 0, 0)

        self.coverLabel = QLabel()
        self.coverLabel.setMaximumSize(Manhua.manhuaSize * 1.)
        self.describeManhuaLabel = QLabel()

        self.infoDescriptionLayout.addWidget(self.coverLabel)
        self.infoDescriptionLayout.addWidget(self.nameLabelQ)
        self.infoDescriptionLayout.setContentsMargins(0, 0, 0, 0)

        self.infoDescriptionLayout.setStretch(0, 1)
        self.infoDescriptionLayout.setStretch(1, 3)

        self.chapterDetailsLayout = QVBoxLayout()
        self.chapterDetailsLayout.addWidget(self.describeManhuaLabel)

        self.infoLayout.addLayout(self.infoHeaderLayout)
        self.infoLayout.addLayout(self.infoDescriptionLayout)
        self.infoLayout.addLayout(self.chapterDetailsLayout)

        self.infoLayout.setStretch(0, 1)
        self.infoLayout.setStretch(1, 2)
        self.infoLayout.setStretch(2, 7)

        self.chaptersLayout = QVBoxLayout()

        self.chaptersSelectionLayout = QVBoxLayout()
        self.selectionWidget = QWidget()
        self.selectionLayout = QVBoxLayout(self.selectionWidget)
        self.selectionLayout.setContentsMargins(0, 0, 0, 0)

        self.scrollArea = QScrollArea(self.selectionWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.loadDescriptionItems()

        self.selectionWidget.setLayout(self.selectionLayout)
        self.chaptersSelectionLayout.addWidget(self.selectionWidget)
        self.chaptersLayout.addLayout(self.chaptersSelectionLayout)

        self.mainLayout.addLayout(self.infoLayout)
        self.mainLayout.addLayout(self.chaptersLayout)

        self.mainLayout.setStretch(0, 1)
        self.mainLayout.setStretch(1, 1)
        
        self.setLayout(self.mainLayout)

    def loadDescriptionItems(self):
        self.scrollAreaWidget = QWidget()

        self.chapterDescListLayout = QVBoxLayout(self.scrollAreaWidget)
        self.chapterDescListLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scrollArea.setWidget(self.scrollAreaWidget)
        self.chapterDescListLayout.setContentsMargins(5, 10, 5, 10)

        self.chapterDescListDisplay()

        self.selectionLayout.addWidget(self.scrollArea)

    def setData(self, dataDict):
        self.dataDict = dataDict
        self.setName(dataDict["ManhuaTitle"])
        self.setCover(dataDict["ManhuaCover"])
        self.setChapters(dataDict["Chapters"])
        self.setStatus(dataDict["Status"])
        self.setDesc(dataDict["Description"])
        self.chapterLen = len(self.descChapters)

    def setName(self, name):
        self.nameLabel.setText(name)
        self.nameLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.nameLabelFont = QFont()
        self.nameLabelFont.setBold(True)
        self.nameLabelFont.setPointSize(16)
        self.nameLabel.setFont(self.nameLabelFont)
        self.currentManhua = self.dataDict["ManhuaTitle"]

    def setCover(self, cover):
        w, h = self.coverLabel.width(), self.coverLabel.height()
        self.coverPixmap = QPixmap(str(cover)).scaled(w, h, Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.coverLabel.setPixmap(self.coverPixmap)
        self.coverLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def setDesc(self, desc):
        self.synopsisLabel.setText(desc)
        self.synopsisLabel.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.synopsisLabel.setWordWrap(True)

    def setChapters(self, chapters):
        self.descChapters = chapters

    def setStatus(self, status):
        self.modeTag.setText(status)

    def setPath(self, pPath, path):
        path = str(pPath) + '\\' + str(path) + '\\'
        return path

    def resetChapters(self):
        self.scrollAreaWidget.deleteLater()
        self.loadDescriptionItems()

    def chapterDescListDisplay(self):
        for x in range(len(self.descChapters)):
            key = list(self.descChapters.keys())[x]
            iPath = self.descChapters.get(key)
            path = self.setPath(self.dataDict["ManhuaPath"], iPath)
            chap = Chapter(key, path, x, self.parent)
            self.chapterDescListLayout.addWidget(chap)

    def exitPage(self):
        self.parent.setCurrentIndex(1)
