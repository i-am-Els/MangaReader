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




from linker import Link
from pathlib import Path
import os, re, consts, resources, color, utilities
from history import History
from themes import Themes
from settings import Settings
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
    QPushButton,
    QFileDialog,
    QComboBox, 
    QScrollArea
)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QCursor, QIcon, QPixmap, QFont

from archive import Archiver

class MainWindow(QWidget):
    def __init__(self, parent: QStackedWidget) -> None:
        super(MainWindow, self).__init__(parent)
        self.parent: QStackedWidget = parent
        self.max_button_size: QSize = QSize(consts.MAX_BTN_SIZE, consts.MAX_BTN_SIZE)
        self.min_button_size: QSize = QSize(consts.MIN_BTN_SIZE, consts.MIN_BTN_SIZE)


        self.newPath = Settings.libraryNewPath
        self.tabIndex: int = consts.E_TAB_HOME_INDEX

        self.icon_size: QSize = QSize(consts.ICON_SIZE, consts.ICON_SIZE)
        self.localDirImport = []
        self.localSingleImport = []
        # self.history = []

        self.apiName = []
        self.firstRun = True
        self.launchDone = False

        self.manhuaObj = object()

        self.size_policy: QSizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.create_widgets()
    
    def getWindowIcon(self) -> QIcon:
        return self.parent.window_icon

    def create_widgets(self) -> None:
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
        
        self.menuButton.setSizePolicy(self.size_policy)
        self.menuButton.setMinimumSize(self.min_button_size)
        self.menuButton.setMaximumSize(self.max_button_size)
        self.menuButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.menuIcon = QIcon()
        self.menuButton.setIconSize(self.icon_size)
        self.menuButton.setObjectName(consts.OBJ_MW_MENU_BTN)
        self.menuButton.setToolTip("Preference Menu")
        self.menuButton.setToolTipDuration(consts.TOOLTIP_DURATION)

        # TextBox
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("[Non-Functional]Enter Search keyword here... e.g 'Shinkeji no Kyojin', 'Bleach', 'Kimetsu no yaiba' etc...")
        
        self.lineEdit.setSizePolicy(self.size_policy)
        self.lineEdit.setMinimumSize(QSize(0, 36))
        self.lineEdit.setMaximumSize(QSize(1366, 36))
        self.lineEdit.setMaxLength(36)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName(consts.OBJ_MW_LINE_EDIT) 

        # Search Button
        self.searchButton = QPushButton()
        self.searchButton.setCheckable(True)
        
        self.searchButton.setSizePolicy(self.size_policy)
        self.searchButton.setMinimumSize(self.min_button_size)
        self.searchButton.setMaximumSize(self.max_button_size)
        self.searchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.searchButton.setToolTip("[Non-Functional]Search Manhua")
        self.searchButton.setToolTipDuration(consts.TOOLTIP_DURATION)

        self.searchIcon = QIcon()
        self.searchButton.setIconSize(self.icon_size)
        self.searchButton.setObjectName(consts.OBJ_MW_SEARCH_BTN)

        # Local Search
        self.localSearchButton = QPushButton()
        self.localSearchButton.setCheckable(True)
        
        self.localSearchButton.setSizePolicy(self.size_policy)
        self.localSearchButton.setMinimumSize(self.min_button_size)
        self.localSearchButton.setMaximumSize(self.max_button_size)
        self.localSearchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.localSearchButton.setToolTip("Load Manhua Bundle from local disk")
        self.localSearchButton.setToolTipDuration(consts.TOOLTIP_DURATION)

        self.localSearchIcon = QIcon()
        self.localSearchButton.setIconSize(self.icon_size)
        self.localSearchButton.setObjectName(consts.OBJ_MW_LOCAL_SEARCH_BTN)

        self.localSearchButtonSingleFormat = QPushButton()
        self.localSearchButtonSingleFormat.setCheckable(True)
        self.localSearchButtonSingleFormat.setSizePolicy(self.size_policy)
        self.localSearchButtonSingleFormat.setMinimumSize(self.min_button_size)
        self.localSearchButtonSingleFormat.setMaximumSize(self.max_button_size)
        self.localSearchButtonSingleFormat.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.localSearchButtonSingleFormat.setToolTip("Load Manhua in Archive formats from local disk")
        self.localSearchButtonSingleFormat.setToolTipDuration(consts.TOOLTIP_DURATION)

        self.localSearchIconSingleFormat = QIcon()
        self.localSearchButtonSingleFormat.setIconSize(self.icon_size)
        self.localSearchButtonSingleFormat.setObjectName(consts.OBJ_MW_LOCAL_SEARCH_ARCHIVE_BTN)

        self.refreshButton = QPushButton()
        self.refreshButton.setCheckable(True)
        self.refreshButton.setSizePolicy(self.size_policy)
        self.refreshButton.setMinimumSize(self.max_button_size)
        self.refreshButton.setMaximumSize(self.max_button_size)
        self.refreshButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.refreshButton.setToolTip("[Non-Functional]Refresh Home tab")
        self.refreshButton.setToolTipDuration(consts.TOOLTIP_DURATION)
        
        self.refreshIcon = QIcon()
        self.refreshButton.setIconSize(self.icon_size)
        self.refreshButton.setObjectName(consts.OBJ_MW_REFRESH_BTN)

        self.apiButton = QPushButton()
        # self.apiButton.addItems(self.apiName)
        self.apiButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.apiButton.setToolTip("[Non-Functional]Manhua plugin dropdown here...")

        self.apiButton.setCheckable(True)
        self.apiButton.setSizePolicy(self.size_policy)
        self.apiButton.setFixedHeight(36)
        self.apiButton.setFixedWidth(100)
        
        self.apiCombo = QComboBox()
        
        self.apiCombo.setSizePolicy(self.size_policy)
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
        self.apiButtonWidget.setObjectName(consts.OBJ_MW_API_BTN_WIDGET)
        self.apiButtonWidget.setLayout(self.apiButtonLayout)
        self.apiButtonWidget.setFixedSize(QSize(120, 36))


        self.clearHistoryButton = QPushButton()
        self.clearHistoryButton.setCheckable(True)
        self.clearHistoryButton.setSizePolicy(self.size_policy)
        self.clearHistoryButton.setMinimumSize(self.max_button_size)
        self.clearHistoryButton.setMaximumSize(self.max_button_size)   
        self.clearHistoryButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))     
        self.clearHistoryButton.setToolTip("Clear history data")
        self.clearHistoryButton.setToolTipDuration(consts.TOOLTIP_DURATION)
        
        self.clearHistoryIcon = QIcon()
        self.clearHistoryButton.setIconSize(self.icon_size)
        self.clearHistoryButton.setObjectName(consts.OBJ_MW_CLEAR_HISTORY_BTN)

        # Add Widgets to searchLayout
        self.searchLayout.addWidget(self.menuButton)
        self.searchLayout.addWidget(self.refreshButton)
        self.searchLayout.addWidget(self.localSearchButton)
        self.searchLayout.addWidget(self.localSearchButtonSingleFormat)
        self.searchLayout.addWidget(self.lineEdit)
        self.searchLayout.addWidget(self.searchButton)
        self.searchLayout.addWidget(self.apiButtonWidget)
        self.searchLayout.addWidget(self.clearHistoryButton)
        
        self.searchLayout.setStretch(0, 1)
        self.searchLayout.setStretch(1, 1)
        self.searchLayout.setStretch(2, 1)
        self.searchLayout.setStretch(3, 1)
        self.searchLayout.setStretch(4, 6)
        self.searchLayout.setStretch(5, 1)
        self.searchLayout.setStretch(6, 1)
        self.searchLayout.setStretch(7, 1)

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
        self.historyLabel.setObjectName(consts.OBJ_MW_HISTORY_LABEL)
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
        self.historyListView.setObjectName(consts.OBJ_MW_HISTORY_LIST)
        self.scrollW.setObjectName(consts.OBJ_MW_HISTORY_SCROLL_W)
        self.scroll.setObjectName(consts.OBJ_MW_SCROLL)

        self.toggleLayout = QHBoxLayout()

        self.toggleGridView = QPushButton()
#        self.toggleGridIcon = QIcon()
        self.toggleGridView.setCheckable(True)
        self.toggleGridView.setObjectName(consts.OBJ_MW_TOGGLE_GRID_BTN)

        self.toggleListView = QPushButton()
#        self.toggleListIcon = QIcon()
        self.toggleListView.setCheckable(True)
        self.toggleListView.setObjectName(consts.OBJ_MW_TOGGLE_LIST_BTN)
        
        self.toggleGridView.setSizePolicy(self.size_policy)
        self.toggleGridView.setMinimumSize(self.min_button_size * 1.75)
        self.toggleGridView.setMaximumSize(self.min_button_size * 1.75)
        self.toggleGridView.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        self.toggleListView.setSizePolicy(self.size_policy)
        self.toggleListView.setMinimumSize(self.min_button_size * 1.75)
        self.toggleListView.setMaximumSize(self.min_button_size * 1.75)
        self.toggleListView.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))


        self.view = QLabel(consts.E_MW_GRID_TEXT if Settings.viewIsGrid == True else consts.E_MW_LIST_TEXT)

        self.selectViewTypeByObj(Settings.viewIsGrid)

        self.toggleLayout.addWidget(self.view)
        self.toggleLayout.addWidget(self.toggleGridView)
        self.toggleLayout.addWidget(self.toggleListView)

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
        self.clearHistoryButton.clicked.connect(self.clearAllHistoryData)

        self.apiButton.clicked.connect(lambda:self.apiComboPopUp())

        self.apiCombo.currentIndexChanged.connect(self.setApiIndex)

        self.localSearchButton.clicked.connect(self.localSearchAction)
        self.localSearchButtonSingleFormat.clicked.connect(self.localSearchSingleFormatAction)
        self.tabWidget.currentChanged.connect(lambda:self.changeTabBarIcon())
        self.toggleGridView.clicked.connect( lambda: self.selectViewTypeByObj(True))
        self.toggleListView.clicked.connect(lambda: self.selectViewTypeByObj(False))

    def clearAllHistoryData(self) -> None:
        Settings.historyData.clear()
        for x in range(self.historyScrollL.layout().count()):
            self.historyScrollL.layout().itemAt(x).widget().deleteLater()

    def historyScrollItems(self) -> None:
        self.scrollW = QWidget()

        self.historyScrollL = QVBoxLayout(self.scrollW)
        self.historyScrollL.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scroll.setWidget(self.scrollW)
        self.historyScrollL.setContentsMargins(5, 10, 5, 10)
        if self.launchDone:
            self.themeObj.resetHistoryStyle()
        if len(Settings.historyData) != 0:
            self.reloadHistory()
        self.historyListViewL.addWidget(self.scroll)
        
    def reloadHistory(self):
        for x in Settings.historyData:
            hist = History(False)
            hist.initData(x["manhuaTitle"], x["chapter"], x["path"], x["index"], x["page"], x["time"])
            hist.setTimeUpdatable(True)
            self.historyScrollL.addWidget(hist)

    def resetHistory(self) -> None:
        self.scrollW.deleteLater()
        self.historyScrollItems()

    def setApiIndex(self, intIndex: int) -> None:
        clickedIndex = intIndex

        Settings.apiIndex = clickedIndex
    
        if self.firstRun == True and Settings.apiIndex == 0:
            self.firstRun = False
        else:
            Settings.setObjMState()
            self.loadApi(intIndex)

    def apiComboPopUp(self) -> None:
        self.apiCombo.showPopup()

    def create_home_widgets(self) -> None:
        self.tabWidget = QTabWidget()

        self.home = QWidget()

        self.homeIcon = QIcon()

        self.homeTabStackLayout = QVBoxLayout()

        self.homeTabStack = QStackedWidget()

        # self.loadHomeTab()

        self.homeTabStackLayout.setContentsMargins(0, 0, 0, 0)

        self.homeTabStackLayout.addWidget(self.homeTabStack)

        self.home.setLayout(self.homeTabStackLayout)

        self.library = Library(self)
        self.library.setObjectName(consts.OBJ_MW_LIBRARY)
        self.libraryIcon = QIcon() 

        self.tabWidget.addTab(self.home, self.homeIcon, "Home")
        self.tabWidget.addTab(self.library, self.libraryIcon, "Library")
        self.tabWidget.setCurrentIndex(consts.E_TAB_HOME_INDEX)
        if len(Settings.libraryMetadata) != 0:
            self.tabWidget.setCurrentIndex(consts.E_TAB_LIBRARY_INDEX)
        if Settings.themeIndex == consts.E_THEME_LIGHT_MODE:
            Themes.changeTabBarIconLight(self)
        else:
            Themes.changeTabBarIconDark(self)

        self.tabWidget.setSizePolicy(self.size_policy)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setIconSize(QSize(64, 24))

        self.homeLayout.addWidget(self.tabWidget)

    def changeTabBarIcon(self) -> None:
        self.tabIndex = self.tabWidget.currentIndex()
        if Settings.themeIndex == consts.E_THEME_LIGHT_MODE:
            Themes.changeTabBarIconLight(self)
        else:
            Themes.changeTabBarIconDark(self)

    def loadApi(self, api_Index) -> None:
        ...

    def loadHomeItems(self) -> None:# More Work 'Online Mode'
        # self.loadApi(Settings.apiIndex)
        ...

    def loadHomeLocalItems(self)  -> None:# More Work 'Offline Mode'
        pass

    def search(self) -> None:# More Work
        self.keyword = self.lineEdit.text()
        if self.keyword != "":
            # print(self.keyword)
            pass

    def menuAction(self) -> None:
        Link.callBack(consts.OBJ_WINDOW, "changeStackIndex", consts.E_WINDOW_STACK_PREF)

    def refreshAction(self) -> None:
        if self.tabWidget.currentIndex() == consts.E_TAB_HOME_INDEX:
            pageToRefreshIndex = self.homeTabStack.currentIndex()
            if self.homeTabStack.currentIndex() == consts.E_TAB_HOME_INNER_MAIN:
                # print("Refused to change Index will refresh instead")
                self.homeTabStack.setCurrentIndex(consts.E_TAB_HOME_INNER_MAIN)
            else:
                self.homeTabStack.setCurrentIndex(consts.E_TAB_HOME_INNER_MAIN)
            self.refresh(pageToRefreshIndex)
        else:
            self.library.refresh()

    def refresh(self, refreshPgIndex: int) -> None:# Much More work
        if (refreshPgIndex == consts.E_TAB_HOME_INNER_MAIN) or (refreshPgIndex == consts.E_TAB_HOME_RESULT_PAGE):
            self.loadApi(Settings.apiIndex)

    def loadHomeTab(self) -> None:
        self.homeDisplay = QWidget()
        self.noInternetDisplay = QWidget()
        self.noSearchResult = QWidget()
        self.searchResultPage = QWidget()
        
        self.loadHomeDisplay()
        self.loadNoInternetDisplay()
        self.loadNoSearchResult()
        self.loadSearchResultPage()

        self.homeTabStack.addWidget(self.homeDisplay)
        self.homeTabStack.addWidget(self.noInternetDisplay)
        self.homeTabStack.addWidget(self.noSearchResult)
        self.homeTabStack.addWidget(self.searchResultPage)

        self.homeTabStack.setCurrentIndex(consts.E_TAB_HOME_NO_INTERNET)
  
    def loadHomeDisplay(self) -> None:# More Work
        self.homeDisplayLayout = QGridLayout()
        ...
        ...
        ...
        self.homeDisplay.setLayout(self.homeDisplayLayout)

    def loadNoInternetDisplay(self) -> None:
        self.noInternetDisplayLayout = QVBoxLayout()

        self.noInternetDisplayLabelpix = QLabel()
        self.noInternetDisplayLabeltxt = QLabel("No Internet Connection")


        self.noInternetDisplayLabelpix.setSizePolicy(self.size_policy)
        self.pixPixmap = QPixmap(resources.no_internet)
        
        self.noInternetDisplayLabelpix.setPixmap(self.pixPixmap.scaled(250, 250, Qt.AspectRatioMode.KeepAspectRatio))
        self.noInternetDisplayLabelpix.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.noInternetDisplayLabeltxt.setSizePolicy(self.size_policy)
        #self.noInternetDisplayLabeltxt.setMaximumHeight(50)
        self.noInternetDisplayLabelFont = QFont()
        self.noInternetDisplayLabelFont.setPointSize(16)
        self.noInternetDisplayLabelFont.setBold(False)
        self.noInternetDisplayLabeltxt.setFont(self.noInternetDisplayLabelFont)
        self.noInternetDisplayLabeltxt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.spaceEater1 = QWidget()
        self.spaceEater1.setSizePolicy(self.size_policy)

        self.spaceEater2 = QWidget()
        self.spaceEater2.setSizePolicy(self.size_policy)

        self.noInternetDisplayLayout.addWidget(self.spaceEater1)
        self.noInternetDisplayLayout.addWidget(self.noInternetDisplayLabelpix)
        self.noInternetDisplayLayout.addWidget(self.noInternetDisplayLabeltxt)
        self.noInternetDisplayLayout.addWidget(self.spaceEater2)


        self.noInternetDisplayLayout.setStretch(0, 5)
        self.noInternetDisplayLayout.setStretch(1, 1)
        self.noInternetDisplayLayout.setStretch(2, 1)
        self.noInternetDisplayLayout.setStretch(3, 6)

        self.noInternetDisplay.setLayout(self.noInternetDisplayLayout)

    def loadNoSearchResult(self) -> None:
        self.noSearchResultLayout = QVBoxLayout()

        self.noSearchResultLabelpix = QLabel()
        self.noSearchResultLabeltxt = QLabel("Keyword not Found")


        self.noSearchResultLabelpix.setSizePolicy(self.size_policy) 
        self.spixPixmap = QPixmap(resources.page_not_found)
        self.noSearchResultLabelpix.setPixmap(self.spixPixmap.scaled(250, 250, Qt.AspectRatioMode.KeepAspectRatio))
        self.noSearchResultLabelpix.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.noSearchResultLabeltxt.setSizePolicy(self.size_policy)
        self.noSearchResultLabelFont = QFont()
        self.noSearchResultLabelFont.setPointSize(16)
        self.noSearchResultLabelFont.setBold(False)
        self.noSearchResultLabeltxt.setFont(self.noSearchResultLabelFont)
        self.noSearchResultLabeltxt.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.spaceEater1 = QWidget()
        self.spaceEater1.setSizePolicy(self.size_policy)

        self.spaceEater2 = QWidget()
        self.spaceEater2.setSizePolicy(self.size_policy)

        self.noSearchResultLayout.addWidget(self.spaceEater1)
        self.noSearchResultLayout.addWidget(self.noSearchResultLabelpix)
        self.noSearchResultLayout.addWidget(self.noSearchResultLabeltxt)
        self.noSearchResultLayout.addWidget(self.spaceEater2)


        self.noSearchResultLayout.setStretch(0, 5)
        self.noSearchResultLayout.setStretch(1, 1)
        self.noSearchResultLayout.setStretch(2, 1)
        self.noSearchResultLayout.setStretch(3, 6)

        self.noSearchResult.setLayout(self.noSearchResultLayout)

    def loadSearchResultPage(self) -> None:
        self.resultLayout = QGridLayout()

    def viewTypeAction(self) -> None:
        self.toggleGridView.setIconSize(self.icon_size * 1.1)
        self.toggleListView.setIconSize(self.icon_size * 1.1)
        
        if self.launchDone:
            Themes.setViewOptionStyle()
            self.library.switchLayout()
    
    def selectViewTypeByObj(self, isGrid)  -> None:
        if isGrid == True:
            Settings.viewIsGrid = True
            self.viewTypeAction()
        else:
            Settings.viewIsGrid = False
            self.viewTypeAction()               
   
    

    def localSearchAction(self) -> None:
        try:
            self.localDirDialog = QFileDialog.getExistingDirectory(self,"Select Manhua Title",self.newPath)

            self.localDirPath = utilities.convertToPath(self.localDirDialog)
            dir = list(os.listdir(self.localDirPath))
            

            if len(dir) == consts.EMPTY:
                utilities.popDialog(consts.E_DIALOG_EMPTY)
                self.localSearchAction()

            elif self.localDirDialog == '':
                pass

            elif self.localDirDialog != '' and len(dir) != consts.EMPTY:
                rightStructure = utilities.correctDirStructure(self.localDirPath)
                if rightStructure == True:
                    self.newPath = utilities.extractParentFolderPath(self.localDirPath)
                    Settings.libraryNewPath = self.newPath

                    self.library.addToLibrary(self.localDirPath, consts.E_STATUS_OFFLINE)
                else:
                    utilities.popDialog(consts.E_DIALOG_STRUCTURE)
                    self.localSearchAction()
        except PermissionError:
            utilities.popDialog(consts.E_DIALOG_PERMISSION)
            self.localSearchAction()

    def localSearchSingleFormatAction(self) -> None:
        self.localSingleDialog = QFileDialog().getOpenFileName(self, 'Open Archived Manhua File', self.newPath, 'Archived Files (*.cbz *zip)')
        self.localSinglePath = utilities.convertToPath(self.localSingleDialog[0])

        if os.path.isfile(self.localSinglePath) and Path(self.localSinglePath).suffix in ['.cbz', '.zip']:  
            self.localFileName = utilities.extractFileName(self.localSinglePath)

            self.parentLocalSinglePath = utilities.extractParentFolderPath(self.localSinglePath)

            self.localSingleImport = [self.localSinglePath, self.localFileName, self.parentLocalSinglePath]
            self.newPath = self.parentLocalSinglePath

            Settings.libraryNewPath = self.newPath

            ziper = Archiver()
            outPath = Path(Settings.extractionNewPath + str(Path(self.localFileName).stem) + "\\")

            if not os.path.exists(outPath):
                os.makedirs(outPath)
                
            curZipFile = ziper.extractCbz(self.localSinglePath, outPath, self)
            dir = list(os.listdir(curZipFile))

            if curZipFile != '' and len(dir) != consts.EMPTY:
                rightStructure = utilities.correctDirStructure(curZipFile)
                if rightStructure == True:
                    self.newPath = utilities.extractParentFolderPath(curZipFile)
                    Settings.libraryNewPath = self.newPath

                    self.library.addToLibrary(curZipFile, consts.E_STATUS_ARCHIVE)
                else:
                    utilities.popDialog(consts.E_DIALOG_STRUCTURE)

        elif self.localSingleDialog == ('', ''):
            pass

        elif not(os.path.isfile(self.localSinglePath)):
            utilities.popDialog(consts.E_DIALOG_NONE)
            self.localSearchSingleFormatAction()


    def setTabIndex(self, tabIndex: int) -> None:
        self.tabWidget.setCurrentIndex(tabIndex)

class Library(QStackedWidget):
    def __init__(self, parent) -> None:
        super(Library, self).__init__(parent)
        self.size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.parent = parent
        self.gridX = 0
        self.gridY = 0
        self.gridYLimit = 7
        self.previousOpen = ""

        self.libraryListdata = list()

        self.noItems = QWidget(self)
        self.libraryShelf = QWidget(self)
        self.descriptionPage = Description()
        
        self.addWidget(self.noItems)
        self.addWidget(self.libraryShelf)
        self.addWidget(self.descriptionPage)
        
        self.setCurrentIndex(consts.E_TAB_LIBRARY_NO_ITEM)

        self.setNoItemsWidget()

        self.loadLibraryLayout()

        self.parent.launchDone = True
        self.testDataForTamper()
        if len(Settings.libraryMetadata) != 0:
            # self.parent.tabWidget.setCurrentIndex(consts.E_TAB_LIBRARY_INDEX)
            self.setCurrentIndex(consts.E_TAB_LIBRARY_SHELF)

    def refresh(self) -> None:
        self.testDataForTamper()    
        if self.currentIndex() != consts.E_TAB_LIBRARY_NO_ITEM:
            self.switchLayout()
        if self.currentIndex() == consts.E_TAB_LIBRARY_DESCRIPTION_PAGE:
                self.reloadManhuaData(self.descriptionPage.currentManhua)
                # print(self.descriptionPage.dataDict)

    def fetchStatus(self, key: str):
        if key == consts.E_STATUS_OFFLINE_TEXT:
            return consts.E_STATUS_OFFLINE
        elif key == consts.E_STATUS_ONLINE_TEXT:
            return consts.E_STATUS_ONLINE
        elif key == consts.E_STATUS_ARCHIVE_TEXT:
            return consts.E_STATUS_ARCHIVE 

    def testDataForTamper(self) -> None:
        alt = dict()

        for x in list(Settings.libraryMetadata.values()):
            if os.path.exists(x["ManhuaPath"]):
                v = utilities.addToMetaData(x["ManhuaPath"], self.fetchStatus(x["Status"]))
                v["IsFav"] = x["IsFav"]
                alt.update({x["ManhuaTitle"] : v})
        temp = alt
        if not Settings.libraryMetadata == alt:
            for x in list(Settings.libraryMetadata.values()):
                if os.path.exists(x["ManhuaCover"]):
                    temp[x["ManhuaTitle"]]["ManhuaCover"] = x["ManhuaCover"]
        Settings.libraryMetadata = temp
            
    def setNoItemsWidget(self) -> None:
        self.noItemsLabel = QLabel()
        self.noItemsPixmap = QPixmap(resources.lib_no_item)
        self.noItemsLabel.setPixmap(self.noItemsPixmap.scaled(256, 256, Qt.AspectRatioMode.KeepAspectRatio))
        self.noItemsLayout = QVBoxLayout()
        self.noItemsLayout.addWidget(self.noItemsLabel, alignment=Qt.AlignmentFlag.AlignCenter)

        self.noItems.setLayout(self.noItemsLayout)

    def loadLibraryItems(self) -> None:
        self.libraryScrollAreaWidget = QWidget()
        
        if Settings.viewIsGrid:
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
        
        if Settings.viewIsGrid:
            test = self.parent.parent.parent.windowState()
            if test == Qt.WindowState.WindowMaximized or test == Qt.WindowState.WindowFullScreen:
                self.libraryMaximized()
            elif test == Qt.WindowState.WindowNoState or test == Qt.WindowState.WindowActive:
                self.libraryResized()
        else:
            self.libraryListReDisplay()

        self.libraryShelfLayout.addWidget(self.libraryScrollArea)

        
    def loadLibraryLayout(self) -> None:
        self.libraryShelfLayout = QVBoxLayout(self.libraryShelf)
        self.libraryShelfLayout.setContentsMargins(0, 0, 0, 0)

        self.libraryScrollArea = QScrollArea(self.libraryShelf)
        self.libraryScrollArea.setWidgetResizable(True)
        self.libraryScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.loadLibraryItems()
        self.libraryShelfLayout.setStretch(0, 1)
        self.libraryShelf.setLayout(self.libraryShelfLayout)

    def addToLibraryAction(self, manhuaObj: QWidget) -> None:
        self.calculateLibraryDimension()
        spacing = self.calculateLibrarySpacing()
        if Settings.viewIsGrid:
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
        Link.callBack(consts.OBJ_MW_NAME, "setTabIndex", consts.E_TAB_LIBRARY_INDEX)
        self.setCurrentIndex(consts.E_TAB_LIBRARY_SHELF)
        

    def libraryMaximized(self) -> None:
        dimension = self.calculateLibraryDimension()
        spacing = self.calculateLibrarySpacing()
        self.libraryDisplayChangeAction(dimension, spacing)
        
    def libraryResized(self) -> None:
        dimension = self.calculateLibraryDimension()
        spacing = self.calculateLibrarySpacing()
        self.libraryDisplayChangeAction(dimension, spacing)

    def libraryDisplayChangeAction(self, limit: int, spacing: int) -> None:
        self.gridYLimit = limit
        self.libraryItemLength = len(self.libraryListdata)
        
        self.libraryShelfGridLayout.setSpacing(spacing)

        if self.libraryItemLength != consts.EMPTY:
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

    def libraryListReDisplay(self) -> None:
        self.libraryItemLength = len(self.libraryListdata)
        if self.libraryItemLength != consts.EMPTY:
            for x in range(self.libraryItemLength):
                # self.libraryListdata[x].switchVariant("grid")
                self.libraryShelfListLayout.addWidget(self.libraryListdata[x])


    def addToLibrary(self, path: str, status: str) -> None:
        try:
            manhuaMetaDict = utilities.addToMetaData(path, status)
            if manhuaMetaDict != {} and manhuaMetaDict != None:
                manhuaMetaDict["IsFav"] = False

                if not((manhuaMetaDict["ManhuaTitle"]) in Settings.libraryMetadata):
                    Settings.libraryMetadata.update({manhuaMetaDict["ManhuaTitle"] : manhuaMetaDict})
                    self.manhuaObj = Manhua(Settings.libraryMetadata[manhuaMetaDict["ManhuaTitle"]], self)
                    self.libraryListdata.append(self.manhuaObj)
                    self.addToLibraryAction(self.manhuaObj)
                else:
                    utilities.popDialog(consts.E_DIALOG_DUPLICATE)
        except IndexError:
            utilities.popDialog(consts.E_DIALOG_STRUCTURE)


    def recreateManhuas(self) -> None:
        self.libraryListdata.clear()
        for k in list(Settings.libraryMetadata.keys()):
            self.manhuaObj = Manhua(Settings.libraryMetadata[k], self)            
            self.libraryListdata.append(self.manhuaObj)

    def switchLayout(self) -> None:
        self.libraryScrollAreaWidget.deleteLater()
        self.loadLibraryItems()

    def openDescription(self, dataDictInfo: str, dataDictInfoPath: str, index: int = 0) -> None:
        if os.path.exists(dataDictInfoPath):
            #if dataDict["ManhuaTitle"] != self.previousOpen:
            self.reloadManhuaData(dataDictInfo, index)
            #self.descriptionPage.setData(dataDict)
            #self.descriptionPage.resetChapters()
            #self.win_dow.objReader.setData(dataDict["ManhuaTitle"])
            Link.modifyAttribute(parent=consts.OBJ_READER_NAME, attr="manhuaChanged", value=True)
            Link.modifyAttribute(parent=consts.OBJ_READER_NAME, attr="previousManhuaName", value=self.previousOpen)
            self.previousOpen = dataDictInfo
            self.setCurrentIndex(2)
        else:
            utilities.popDialog(consts.E_DIALOG_DELETED_MANHUA)
            self.deleteManhua(dataDictInfo)

    def calculateLibraryDimension(self) -> int:
        dimensionV = self.geometry().width()
        if dimensionV < 600:
            dimensionV = consts.LIB_DIMENSION

        dimension = int(dimensionV / Manhua.manhuaSize.width()) - 2
        self.gridYLimit = dimension
        return dimension

    def calculateLibrarySpacing(self) -> int:
        spacingV = self.geometry().width()
        if spacingV < 600:
            spacingV = consts.LIB_DIMENSION
        dimension = int(spacingV / Manhua.manhuaSize.width()) - 1
        spacing = spacingV - (Manhua.manhuaSize.width() * dimension)
        spacing = int(spacing / dimension)
        return spacing

    def launchReader(self, mtitle: str, ctitle: str, index: int, path: str, page:int = 1) -> None:
        if os.path.exists(path) and len(os.listdir(path)) != consts.EMPTY and any(Path(os.path.join(str(path), filename)).suffix in consts.IMG_EXT_LIST for filename in os.listdir(path)):
            if(Settings.fsState) == True and Link.fetchAttribute(consts.OBJ_APP, "windowState", True) != Qt.WindowState.WindowMaximized:
                Link.callBackDeep(consts.OBJ_APP, "customTitleBar", "toggleRestore")
            self.setHistory(mtitle, ctitle, path, index, page)
            Link.callBack(consts.OBJ_READER_NAME, "loadChapterPages", index, page)
            Link.callBack(consts.OBJ_READER_NAME, "setFocus")
            Link.callBack(consts.OBJ_WINDOW, "setCurrentIndex", 1)
        else:
            utilities.popDialog(consts.E_DIALOG_DELETED_CHAPTER)
            self.reloadManhuaData(self.descriptionPage.currentManhua, index)

    def setHistory(self, mtitle: str, ctitle: str, path: str, index: int, page: int = 1) -> None:
        dict_ = {"mName": mtitle}
        try:
            dictSetting = {"mName": Settings.historyData[0]["manhuaTitle"]}
            if dictSetting != dict_:
                historyWidget = History()
                historyWidget.initData(mtitle, ctitle, path, index, page)
                Link.callBackDeep(consts.OBJ_MW_NAME, "historyScrollL", "insertWidget", 0, historyWidget)
                dictD = historyWidget.getData()
                Settings.historyData.insert(0, dictD)
            else:
                l = Link.fetchAttribute(consts.OBJ_MW_NAME, "historyScrollL").layout().itemAt(0).widget()
                l.updateTime()
                l.bindData()
        except IndexError:
            historyWidget = History()
            historyWidget.initData(mtitle, ctitle, path, index, page)
            Link.callBackDeep(consts.OBJ_MW_NAME, "historyScrollL", "insertWidget", 0, historyWidget)
            dictD = historyWidget.getData()
            Settings.historyData.insert(0, dictD)

    def setCover(self, path: str, manhuaName: str) -> None:
        if os.path.exists(path):
            Settings.libraryMetadata[manhuaName]["ManhuaCover"] = str(path)
            manhuasData = list(Settings.libraryMetadata.keys())
            index = manhuasData.index(manhuaName)
            self.libraryListdata[index].manhuaCoverPixmap = QPixmap(str(path)).scaled(90, 120, Qt.AspectRatioMode.KeepAspectRatioByExpanding)
            self.libraryListdata[index].manhuaCoverDisplayLabel.setPixmap(self.libraryListdata[index].manhuaCoverPixmap)
        else:
            utilities.popDialog(consts.E_DIALOG_DELETED_IMAGE)
            Settings.libraryMetadata[manhuaName]["ManhuaCover"] = str(resources.default_cover_image)
            manhuasData = list(Settings.libraryMetadata.keys())
            index = manhuasData.index(manhuaName)
            self.libraryListdata[index].manhuaCoverPixmap = QPixmap(resources.default_cover_image).scaled(90, 120, Qt.AspectRatioMode.KeepAspectRatioByExpanding)
            self.libraryListdata[index].manhuaCoverDisplayLabel.setPixmap(self.libraryListdata[index].manhuaCoverPixmap)
            
    def deleteManhua(self, manhuaKey: str) -> None:
        temp = list(Settings.libraryMetadata.keys())
        index =  temp.index(manhuaKey)
        self.deleteManhuaData(manhuaKey, index)
        print(Settings.libraryMetadata.keys())
        print(self.libraryListdata)
        self.libraryScrollAreaWidget.layout().itemAt(index).widget().deleteLater()
        if self.libraryItemLength == consts.EMPTY:
            self.setCurrentIndex(consts.E_TAB_LIBRARY_NO_ITEM)
        else:
            self.setCurrentIndex(consts.E_TAB_LIBRARY_SHELF)
            self.switchLayout()

    def deleteManhuaData(self, manhuaKey: str, index: int) -> None:
        del Settings.libraryMetadata[manhuaKey]
        self.libraryListdata.pop(index)
        self.libraryItemLength = len(self.libraryListdata)

    def reloadManhuaData(self, manhuaKey: str, index: int = 0) -> None:
        if os.path.exists(Settings.libraryMetadata[manhuaKey]["ManhuaPath"]):
            st = self.fetchStatus(Settings.libraryMetadata[manhuaKey]["Status"])
            dic = utilities.addToMetaData(Settings.libraryMetadata[manhuaKey]["ManhuaPath"], st)
            Settings.libraryMetadata[manhuaKey]["ManhuaTitle"] = dic["ManhuaTitle"]
            if not os.path.exists(Settings.libraryMetadata[manhuaKey]["ManhuaCover"]):
                Settings.libraryMetadata[manhuaKey]["ManhuaCover"] = dic["ManhuaCover"]
            Settings.libraryMetadata[manhuaKey]["Chapters"] = dic["Chapters"]
            Settings.libraryMetadata[manhuaKey]["Status"] = dic["Status"]
            Settings.libraryMetadata[manhuaKey]["Description"] = dic["Description"]
            
            self.resetSomeDescData(Settings.libraryMetadata[manhuaKey], index)
            
        else:
            utilities.popDialog(consts.E_DIALOG_DELETED_MANHUA)
            self.deleteManhua(manhuaKey)
            self.setCurrentIndex(consts.E_TAB_LIBRARY_SHELF)

    def resetSomeDescData(self, manhuaKey: dict, index: int = 0) -> None:
        self.descriptionPage.setData(manhuaKey)
        self.descriptionPage.redisplayChapters()
        Link.callBack(consts.OBJ_READER_NAME, "setData", manhuaKey["ManhuaTitle"], index)

    @staticmethod
    def launchArchiveReader(info):
        
        ...


class Chapter(QPushButton):
    def __init__(self, mtitle: str, sTitle: str, pTitlePath: str | Path, index: int) -> None:
        super().__init__()
        self.mtitle = mtitle
        self.title = sTitle
        self.titlePath = pTitlePath
        self.index = index

        self.fm = self.fontMetrics()
        self.elided = self.fm.elidedText(self.title, Qt.TextElideMode.ElideRight, 200)
        
        self.pathText = self.titlePath
        self.elidedText = self.fm.elidedText(self.pathText, Qt.TextElideMode.ElideMiddle, 250)

        self.labelString = f"{self.elided} \n{self.elidedText}"
        self.setText(self.labelString)
        self.setStyleSheet("QPushButton{ text-align:  left; border-radius: 5px; padding-left: 10px;} QPushButton:hover { color: white; }") #---Theme---
        self.setMinimumHeight(50)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.setToolTip(self.pathText)
        self.setToolTipDuration(consts.TOOLTIP_DURATION)

        self.clicked.connect(lambda: Link.callBack(consts.OBJ_LIB_NAME, "launchReader", self.mtitle, self.title, self.index, self.titlePath))


class Manhua(QPushButton):
    manhuaSize = QSize(120, 170)
    
    def __init__(self, metadata: dict, parent) -> None:
        super(Manhua, self).__init__()
        self.parent = parent
        self.metadata: dict = metadata
        self.setCheckable(True)
        self.manhuaName = metadata["ManhuaTitle"]
        self.manhuaPath = Path(metadata["ManhuaPath"])
        self.manhuaCover = Path(metadata["ManhuaCover"])
        self.manhuaChapters = metadata["Chapters"]
        self.isFavorite = metadata["IsFav"]
        self.size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setObjectName(self.manhuaName)

        self.setToolTip(self.manhuaName)
        self.setToolTipDuration(consts.TOOLTIP_DURATION)

        self.recreateObjectWidgets()

        if Settings.viewIsGrid:
            self.manhuaBgLayoutGrid = QVBoxLayout()
            self.displayGridVariant()
        else:
            self.manhuaBgLayoutList = QHBoxLayout()
            self.displayListVariant()

        self.clicked.connect(lambda: Link.callBackDeep(consts.OBJ_MW_NAME, "library", "openDescription", self.metadata["ManhuaTitle"], self.metadata["ManhuaPath"]))
        
    def recreateObjectWidgets(self) -> None:
        self.manhuaCoverDisplayLabel = QLabel()
        self.manhuaCoverDisplayLabel.setObjectName(consts.OBJ_MW_MANHUA_LABEL)
        self.manhuaCoverDisplayLabel.setSizePolicy(self.size_policy)
        self.manhuaCoverLayout = QVBoxLayout()
        self.manhuaDetailsLayout = QHBoxLayout()
        self.manhuaDetailsLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # self.manhuaDetailsWidget = QWidget()
        self.manhuaNameLabel = QLabel()
        self.manhuaNameLabel.setObjectName(consts.OBJ_MW_MANHUA_NAME_LABEL)
        self.manhuaFavoriteButton = QPushButton()
        self.manhuaFavoriteButton.setSizePolicy(self.size_policy)
        self.manhuaFavoriteButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.manhuaFavoriteButtonIcon = QIcon()
        
        if not os.path.exists(self.manhuaCover):
            self.manhuaCoverPixmap = QPixmap(resources.default_cover_image).scaled(90, 120, Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        else:
            self.manhuaCoverPixmap = QPixmap(str(self.manhuaCover)).scaled(90, 120, Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.manhuaCoverDisplayLabel.setPixmap(self.manhuaCoverPixmap)
        self.manhuaCoverLayout.addWidget(self.manhuaCoverDisplayLabel)
        self.manhuaCoverLayout.setSpacing(0)
        self.manhuaCoverLayout.setContentsMargins(0, 0, 0, 0)

        self.fm = self.fontMetrics()
        self.elided = self.fm.elidedText(self.manhuaName, Qt.TextElideMode.ElideRight, 110)
        self.manhuaNameLabel.setText(self.elided)
        self.manhuaNameLabel.setSizePolicy(self.size_policy)
        self.manhuaNameLabelFont = QFont()
        self.manhuaNameLabelFont.setPointSize(7)
        self.manhuaNameLabelFont.setBold(True)
        self.manhuaNameLabel.setFont(self.manhuaNameLabelFont)
        self.manhuaNameLabel.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        self.manhuaNameLabel.setMaximumHeight(20)

        self.manhuaFavoriteButtonIcon.addPixmap(QPixmap(resources.favorite_btn), QIcon.Mode.Normal, QIcon.State.Off)
        self.manhuaFavoriteButton.setIcon(self.manhuaFavoriteButtonIcon)
        self.manhuaFavoriteButton.setFixedSize(QSize(20, 20))
        self.manhuaFavoriteButton.setObjectName("fav")

        # self.manhuaDetailsWidget.setLayout(self.manhuaDetailsLayout)
        self.manhuaDetailsLayout.addWidget(self.manhuaNameLabel)
        self.manhuaDetailsLayout.addWidget(self.manhuaFavoriteButton)

        self.manhuaCoverDisplayLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.checkFav(self.isFavorite)

        Themes.setManhuaObjStyle(self)

        self.manhuaFavoriteButton.clicked.connect(lambda: self.favorite(self.isFavorite))

    def displayGridVariant(self) -> None:
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
    
    def displayListVariant(self) -> None:
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

    def checkFav(self, isFavorite: bool) -> None:
        if isFavorite == False:
            self.removeFavorite()
        else:
            self.addToFavorite()

    def favorite(self, isFavorite: bool) -> None:
        if isFavorite == False:
            self.addToFavorite()
            self.isFavorite = True
        else:
            self.removeFavorite()
            self.isFavorite = False

    def addToFavorite(self) -> None:
        self.manhuaFavoriteButtonIcon.addPixmap(QPixmap(resources.favorite_btn_checked))
        self.manhuaFavoriteButton.setIcon(self.manhuaFavoriteButtonIcon)
        dict_ = Settings.libraryMetadata
        dict_[self.manhuaName]["IsFav"] = True
    
    def removeFavorite(self) -> None:
        self.manhuaFavoriteButtonIcon.addPixmap(QPixmap(resources.favorite_btn))
        self.manhuaFavoriteButton.setIcon(self.manhuaFavoriteButtonIcon)
        dict_ = Settings.libraryMetadata
        dict_[self.manhuaName]["IsFav"] = False
    

class Description(QWidget):
    def __init__(self) -> None:
        super(Description, self).__init__()
        self.size_policy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.max_button_size = QSize(36, 36)
        self.min_button_size = QSize(16, 16)
        self.icon_size = QSize(20, 20)
        self.launchDone = False
        self.dataDict = dict()
        self.descChapters: dict = dict()
        self.chapterLen = int()
        self.createDescriptionWidget()
        self.launchDone = True

        self.exitButton.clicked.connect(lambda: self.exitPage())
        self.deleteButton.clicked.connect(lambda: Link.callBack(consts.OBJ_LIB_NAME, "deleteManhua", self.dataDict["ManhuaTitle"]))

        self.setObjectName(consts.OBJ_MW_LIBRARY_DESC)
        
    def createDescriptionWidget(self) -> None:
        self.mainLayout = QHBoxLayout(self)
        
        self.infoLayout = QVBoxLayout()
        
        self.infoHeaderLayout = QHBoxLayout()
        self.exitButton = QPushButton()
        self.exitButton.setObjectName("backDescButton")

        self.exitButton.setSizePolicy(self.size_policy)
        self.exitButton.setMinimumSize(self.min_button_size)
        self.exitButton.setMaximumSize(self.max_button_size)
        self.exitButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.exitButton.setGeometry(0, 0, 36, 36)
        self.exitButton.setToolTip("Return to Home")
        self.exitButton.setToolTipDuration(consts.TOOLTIP_DURATION)
        self.exitButtonIcon = QIcon()
        self.exitButton.setIconSize(self.icon_size)
        self.exitButton.setCheckable(True)

        self.modeTag = QLabel()
        self.deleteButton = QPushButton()
        self.deleteButton.setObjectName(consts.OBJ_MW_LIBRARY_DESC_DELETE_MANHUA_BTN)

        self.deleteButton.setSizePolicy(self.size_policy)
        self.deleteButton.setMinimumSize(self.min_button_size)
        self.deleteButton.setMaximumSize(self.max_button_size)
        self.deleteButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.deleteButton.setGeometry(0, 0, 36, 36)
        self.deleteButton.setToolTip("Delete Manhua")
        self.deleteButton.setToolTipDuration(consts.TOOLTIP_DURATION)
        self.deleteButtonIcon = QIcon()
        self.deleteButton.setIconSize(self.icon_size)
        self.deleteButton.setCheckable(True)

        self.infoHeaderLayout.addWidget(self.exitButton)
        self.infoHeaderLayout.addWidget(self.modeTag)
        self.infoHeaderLayout.addWidget(self.deleteButton)

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

    def loadDescriptionItems(self) -> None:
        self.scrollAreaWidget = QWidget()

        self.chapterDescListLayout = QVBoxLayout(self.scrollAreaWidget)
        self.chapterDescListLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.scrollArea.setWidget(self.scrollAreaWidget)
        self.chapterDescListLayout.setContentsMargins(5, 10, 5, 10)

        self.chapterDescListDisplay()

        self.selectionLayout.addWidget(self.scrollArea)

    def setData(self, dataDict: dict) -> None:
        self.dataDict = dataDict
        self.setName(dataDict["ManhuaTitle"])
        self.setCover(dataDict["ManhuaCover"])
        self.setChapters(dataDict["Chapters"])
        self.setStatus(dataDict["Status"])
        self.setDesc(dataDict["Description"])
        self.chapterLen = len(self.descChapters)

    def setName(self, name: str) -> None:
        self.fm = self.fontMetrics()
        self.elided = self.fm.elidedText(name, Qt.TextElideMode.ElideMiddle, 140)
        self.nameLabel.setText(self.elided)
        self.nameLabel.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.nameLabelFont = QFont()
        self.nameLabelFont.setBold(True)
        self.nameLabelFont.setPointSize(16)
        self.nameLabel.setFont(self.nameLabelFont)
        self.currentManhua = self.dataDict["ManhuaTitle"]

    def setCover(self, cover: str | Path) -> None:
        w, h = self.coverLabel.width(), self.coverLabel.height()
        if not os.path.exists(cover):
            self.coverPixmap = QPixmap(resources.default_cover_image).scaled(w, h, Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        else:
            self.coverPixmap = QPixmap(str(cover)).scaled(w, h, Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        self.coverLabel.setPixmap(self.coverPixmap)
        self.coverLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def setDesc(self, desc: str) -> None:
        self.synopsisLabel.setText(desc)
        self.synopsisLabel.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        self.synopsisLabel.setWordWrap(True)

    def setChapters(self, chapters: dict) -> None:
        self.descChapters = chapters

    def setStatus(self, status: str) -> None:
        self.modeTag.setText(status)

    def setPath(self, pPath: str | Path, path: str | Path) -> str:
        path = str(pPath) + '\\' + str(path) + '\\'
        return path

    def resetChapters(self) -> None:
        self.scrollAreaWidget.deleteLater()
        self.loadDescriptionItems()

    def redisplayChapters(self) -> None:
        if os.path.exists(self.dataDict["ManhuaPath"]) and self.chapterLen != consts.EMPTY:
            self.resetChapters()
        else:
            utilities.popDialog(consts.E_DIALOG_DELETED_MANHUA)
            Link.callBack(consts.OBJ_LIB_NAME, "deleteManhua", self.dataDict["ManhuaTitle"])
            Link.callBack(consts.OBJ_LIB_NAME, "setCurrentIndex", consts.E_TAB_LIBRARY_SHELF)

    def chapterDescListDisplay(self) -> None:
        for x in range(len(self.descChapters)):
            key = list(self.descChapters.keys())[x]
            iPath = self.descChapters.get(key)
            path = self.setPath(self.dataDict["ManhuaPath"], iPath)
            chap = Chapter(self.dataDict["ManhuaTitle"], key, path, x)
            self.chapterDescListLayout.addWidget(chap)

    def exitPage(self) -> None:
        Link.callBack(consts.OBJ_LIB_NAME, "setCurrentIndex", consts.E_TAB_LIBRARY_SHELF)
