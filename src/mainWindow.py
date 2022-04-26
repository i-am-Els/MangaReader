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




from pathlib import Path
import os, re

from themes import Themes
# from settings import Settings

from PyQt6.QtWidgets import (
    QTabBar,
    QStackedWidget,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QTabWidget,
    QWidget,
    QLineEdit,
    QLabel,
    QSizePolicy,
    QListView,
    QMessageBox,
    QPushButton,
    QFileDialog,
    QComboBox
)

from PyQt6.QtCore import QSize, Qt, QRect
from PyQt6.QtGui import QCursor, QIcon, QPixmap, QFont

class MainWindow(QWidget):
    def __init__(self, obj, win_dow, window_Icon, parent=None):
        super(MainWindow, self).__init__(parent)
        self.obj = obj
        self.win_dow = win_dow
        self.window_Icon = window_Icon
        self.max_button_size = QSize(36, 36)
        self.min_button_size = QSize(16, 16)

        self.themeObj = object()
        self.setting = object()

        self.initPath = object()
        self.newPath = object()
        self.themeIndex = int()
        self.tabIndex = 0
        self.apiIndex = int()

        self.icon_size = QSize(20, 20)
        self.localDirImport = []
        self.localSingleImport = []

        self.apiName = []
        self.firstRun = True

        self.gridX = 0
        self.gridY = 0
        self.gridYLimit = 5

        self.localMangaTitleDict = dict()
        self.mangaObj = object()

        self.sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.create_widgets()

    def create_widgets(self):
        #------------------------------------------------
        self.gridLayout = QGridLayout()

        #------------------------------------------------
        # Create a centralLayout to hold all other layouts
        self.centralLayout = QVBoxLayout()
        self.centralLayout.setSpacing(9)

        #------------------------------------------------
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

        self.localSearchIcon = QIcon()
        self.localSearchButton.setIconSize(self.icon_size)
        self.localSearchButton.setObjectName("localSearchButton")


        self.localSearchButtonSingleFormat = QPushButton()
        self.localSearchButtonSingleFormat.setCheckable(True)
        self.localSearchButtonSingleFormat.setSizePolicy(self.sizePolicy)
        self.localSearchButtonSingleFormat.setMinimumSize(self.min_button_size)
        self.localSearchButtonSingleFormat.setMaximumSize(self.max_button_size)
        self.localSearchButtonSingleFormat.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.localSearchIconSingleFormat = QIcon()
        self.localSearchButtonSingleFormat.setIconSize(self.icon_size)
        self.localSearchButtonSingleFormat.setObjectName("localSearcButtonSingleFormat")


        self.refreshButton = QPushButton()
        self.refreshButton.setCheckable(True)
        self.refreshButton.setSizePolicy(self.sizePolicy)
        self.refreshButton.setMinimumSize(self.max_button_size)
        self.refreshButton.setMaximumSize(self.max_button_size)
        self.refreshButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        self.refreshIcon = QIcon()
        self.refreshButton.setIconSize(self.icon_size)
        self.refreshButton.setObjectName("refreshButton")

        
        self.apiButton = QPushButton()
        # self.apiButton.addItems(self.apiName)
        self.apiButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.apiButton.setToolTip("Manga plugin dropdown here...")

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

        #------------------------------------------------
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

        self.historyListView = QListView()
        # Add widgets to the historyLayout

        #---------------------------------------------------
        self.toggleLayout = QHBoxLayout()

        self.toggleGridView = QPushButton()
        self.toggleGridView.setCheckable(True)
        self.toggleGridView.setObjectName("toggleGridView")

        self.toggleListView = QPushButton()
        self.toggleListView.setCheckable(True)
        self.toggleListView.setObjectName("toggleListView")
        #---------------------------------------------------
        
        self.toggleGridView.setSizePolicy(self.sizePolicy)
        self.toggleGridView.setMinimumSize(self.min_button_size * 1.75)
        self.toggleGridView.setMaximumSize(self.min_button_size * 1.75)
        self.toggleGridView.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        #----------------------------------------------------
        
        self.toggleListView.setSizePolicy(self.sizePolicy)
        self.toggleListView.setMinimumSize(self.min_button_size * 1.75)
        self.toggleListView.setMaximumSize(self.min_button_size * 1.75)
        self.toggleListView.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        #--------------------------------------------------------

        self.toggleList = [self.toggleGridView, self.toggleListView]
        self.toggleViewValue = ["Grid View", "List View"]

        self.previousViewOptionIndex = 0
        self.viewOptionIndex = 0

        self.view = QLabel(self.toggleViewValue[self.viewOptionIndex])
        #----------------------------------------------------

        self.selectViewType(self.viewOptionIndex)

        #----------------------------------------------------

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

        #------------------------------------------------
        # Add homeLayout and historyLayout to containerLayout
        self.containerLayout.addLayout(self.homeLayout)
        self.containerLayout.addLayout(self.historyLayout)

        # Set Layout Stretch policy
        self.containerLayout.setStretch(0, 7)
        self.containerLayout.setStretch(1, 3)
        #------------------------------------------------
        #Add searchLayout and containerLayout to centralLayout
        self.centralLayout.addLayout(self.searchLayout)
        self.centralLayout.addLayout(self.containerLayout)
        self.centralLayout.setStretch(0, 2)
        self.centralLayout.setStretch(1, 12)
        #------------------------------------------------
        self.gridLayout.addLayout(self.centralLayout, 0, 0, 1, 1)

        self.setLayout(self.gridLayout)
        #-----------------------------------------------
        self.searchButton.clicked.connect(self.search)
        self.lineEdit.returnPressed.connect(self.searchButton.click)
        
        self.menuButton.clicked.connect(self.menuAction)
        self.refreshButton.clicked.connect(self.refreshAction)

        self.apiButton.clicked.connect(lambda:self.apiComboPopUp())

        self.apiCombo.currentIndexChanged.connect(self.setApiIndex)

        self.toggleGridView.clicked.connect( lambda: self.selectViewTypeByObj('toggleGrid'))

        self.toggleListView.clicked.connect(lambda: self.selectViewTypeByObj('toggleList'))

        self.localSearchButton.clicked.connect(self.localSearchAction)
        self.localSearchButtonSingleFormat.clicked.connect(self.localSearchSingleFormatAction)
        self.tabWidget.currentChanged.connect(lambda:self.changeTabBarIcon())

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
        # self.tabBar = QTabBar(self.tabWidget)
        #---------------------------------------------------

        self.home = QWidget()

        self.homeIcon = QIcon()

        self.homeTabStackLayout = QVBoxLayout()

        self.homeTabStack = QStackedWidget()

        # self.loadHomeTab()

        self.homeTabStackLayout.setContentsMargins(0, 0, 0, 0)

        #----------------------------------------------------
        self.homeTabStackLayout.addWidget(self.homeTabStack)

        self.home.setLayout(self.homeTabStackLayout)
        #---------------------------------------------------

        self.library = Library(self)
        self.libraryIcon = QIcon() 

        # self.loadLibraryTab()

        #---------------------------------------------------     
        # self.tabBar.addTab(self.homeIcon, "Home")
        # self.tabBar.addTab(self.libraryIcon, "Library")
        # self.tabWidget.setTabBar(self.tabBar)  
        self.tabWidget.addTab(self.home, self.homeIcon, "Home")
        self.tabWidget.addTab(self.library, self.libraryIcon, "Library")
        self.tabWidget.setCurrentIndex(0)
        if self.themeIndex == 0:
            Themes.changeTabBarIconLight(self) # Changes selected tabbar icon
        else:
            Themes.changeTabBarIconDark(self)
        #---------------------------------------------------

        self.tabWidget.setSizePolicy(self.sizePolicy)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setIconSize(QSize(64, 24))

        #---------------------------------------------------

        self.homeLayout.addWidget(self.tabWidget)

    def changeTabBarIcon(self):
        self.tabIndex = self.tabWidget.currentIndex()
        if self.themeIndex == 0:
            Themes.changeTabBarIconLight(self)
        else:
            Themes.changeTabBarIconDark(self)

    def loadApi(self, api_Index):
        print("Loading api", self.apiName[api_Index])

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
            print(refreshPgIndex)
            self.loadApi(self.apiIndex)

    def changeStackIndex(self, obj, w_index):
        obj.setCurrentIndex(w_index)

    def loadHomeTab(self):
        self.homeDisplay = QWidget()
        self.noInternetDisplay = QWidget()
        self.noSearchResult = QWidget()
        self.searchResultPage = QWidget()
        self.descriptionPage = QWidget()
        #---------------------------------------------------

        #----------------------------------------------------
        self.loadHomeDisplay()
        self.loadNoInternetDisplay()
        self.loadNoSearchResult()
        self.loadSearchResultPage()
        self.loadDescriptionPage()

        #---------------------------------------------------

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
            #--------------------------------------------
            self.toggleListDisabledIcon =QIcon()
            self.toggleListDisabledIcon.addPixmap(QPixmap("resources/icons/icons8-list-disabled-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.toggleListView.setIcon(self.toggleListDisabledIcon)
            self.toggleListView.setIconSize(self.icon_size * 1.1)

            self.view.setText("Grid View")
            self.viewOptionIndex = 0
            return self.viewOptionIndex, self.previousViewOptionIndex

        else:
            self.toggleListIcon = QIcon()
            self.toggleListIcon.addPixmap(QPixmap("resources/icons/icons8-list-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.toggleListView.setIcon(self.toggleListIcon)
            self.toggleListView.setIconSize(self.icon_size * 1.1)
            #--------------------------------------------
            self.toggleGridDisabledIcon = QIcon()
            self.toggleGridDisabledIcon.addPixmap(QPixmap("resources/icons/icons8-grid-disabled-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
            self.toggleGridView.setIcon(self.toggleGridDisabledIcon)
            self.toggleGridView.setIconSize(self.icon_size * 1.1)

            self.view.setText("List View")
            self.viewOptionIndex = 1
            return self.viewOptionIndex, self.previousViewOptionIndex

    def selectViewType(self, viewsIndex):
        self.selectView(viewsIndex)
        self.previousViewOptionIndex = viewsIndex
        return self.previousViewOptionIndex
    
    def selectViewTypeByObj(self, objName):
        self.previousViewOptionIndex = self.viewOptionIndex
        if objName == "toggleGrid":
            self.selectView(0)
        else:
            self.selectView(1)

    def selectView(self, view_index):
        if view_index == 0:
            self.viewIsGrid = True
            self.viewTypeAction(self.viewIsGrid)
        else:
            self.viewIsGrid = False
            self.viewTypeAction(self.viewIsGrid)

        if self.previousViewOptionIndex != view_index:
            self.changeViewType(self.viewOptionIndex)

    def changeViewType(self, newViewIndex): # More work
        print('Changing view to', self.toggleViewValue[newViewIndex])

    def loadLibraryTab(self):
        self.libraryGridLayout = QGridLayout()
        self.libraryListLayout = QVBoxLayout()
        # if self.viewIsGrid:
        #     self.library.setLayout(self.libraryGridLayout)   
        #     print("I am setting a Grid Layout")
        # else:
        #     self.library.setLayout(self.libraryListLayout)
        #     print("I am setting a List Layout")

        
    def popDialog(self, type):
        if type == 'empty':
            txt, t_txt = "Bundle is empty, Please select a filled directory", "Empty Bundle Error"
        elif type == 'structure':
            txt, t_txt = "There are 2 scenarios that raise this error: Bundle Structure Error or No Image Found\nTip 1: Select a Parent folder that has chapters arranged in sub-folders.\nTip 2: The chapter sub-folders MUST contain images.", "Structure or File Error"
        elif type == 'none':
            txt, t_txt = "Selected file is not a valid archive file. Select A readable archive file such as '.cbz', '.cbr' files.", "Not an Archive File"
        elif type == 'duplicate':
             txt, t_txt = "The manga title already exists in your library, select another title", "Duplicate Action"
        
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
        # print(dir, self.localDirDialog)
        

        if len(dir) == 0:
            self.popDialog('empty')
            self.localSearchAction()

        elif self.localDirDialog == '':
            pass

        elif self.localDirDialog != '' and len(dir) != 0:
            rightStructure = self.correctDirStructure(self.localDirPath)
            print(rightStructure)
            if rightStructure == True:
                # print(dir, self.localDirDialog)
                print("voila")
                self.newPath = self.extractParentFolderPath(self.localDirPath)
                self.setting.libraryNewPath = self.newPath

                self.addToLibrary(self.localDirPath)
            else:
                self.popDialog('structure')
                self.localSearchAction()

    def localSearchSingleFormatAction(self):
        self.localSingleDialog = QFileDialog().getOpenFileName(self, 'Open Archived Manhua File', self.newPath, 'Archived Files (*.cbz *.cbr)')
        self.localSinglePath = self.convertToPath(self.localSingleDialog[0])

        if os.path.isfile(self.localSinglePath) and Path(self.localSinglePath).suffix in ['.cbr', '.cbz']:  
            self.localFileName = self.extractFileName(self.localSinglePath)

            self.parentLocalSinglePath = self.extractParentFolderPath(self.localSinglePath)

            self.localSingleImport = [self.localSinglePath, self.localFileName, self.parentLocalSinglePath]
            self.newPath = self.parentLocalSinglePath

            self.setting.libraryNewPath = self.newPath

            # print(self.localSingleImport)
            print(self.localSingleDialog)

            return self.localSingleImport

        elif self.localSingleDialog == ('', ''):
            print("no file selected")
            pass

        elif not(os.path.isfile(self.localSinglePath)):
            self.popDialog('none')
            # print(self.localSingleDialog)
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

        manhuaMetaDict["MangaTitle"] = Path(path).stem
        manhuaMetaDict["MangaPath"] = str(path)
        emptyCover = True

        for x in os.listdir(path):
            xPath = os.path.join(path, x)
            if os.path.isdir(xPath):
                # sChapterName = str(Path(xPath).name)
                sChapterName = Path(xPath).name
                manhuaChapterList.append(sChapterName)
            elif Path(xPath).suffix in ['.jpeg', '.jpg', '.png'] and emptyCover == True:
                manhuaMetaDict["MangaCover"] = xPath
                emptyCover = False
        if emptyCover == True:
            manhuaMetaDict["MangaCover"] = self.themeObj.defaultCoverImage
        # print(manhuaChapterList)
        sortedManhuaChapterDict = self.sortChapters(manhuaChapterList)
        manhuaMetaDict["Chapters"] = sortedManhuaChapterDict

        if not((manhuaMetaDict["MangaTitle"]) in self.localMangaTitleDict):
            self.localMangaTitleDict.update({manhuaMetaDict["MangaTitle"] : manhuaMetaDict})
            self.mangaObj = Manga(self.localMangaTitleDict[manhuaMetaDict["MangaTitle"]], self.library)
            # self.addMangaWidgetsToLibrary(mangaObj)
            # self.btn = QPushButton("Hi me")
            if self.viewIsGrid:
                if self.gridYLimit >= self.gridY: 
                    self.libraryGridLayout.addWidget(self.mangaObj, self.gridX, self.gridY, 1, 1)
                    self.gridY += 1
                    ...
                else:
                    self.gridY = 0
                    self.gridX += 1
                    self.libraryGridLayout.addWidget(self.mangaObj, self.gridX, self.gridY, 1, 1)
                self.library.setLayout(self.libraryGridLayout)
                print(self.mangaObj.geometry(), self.library.geometry())
                print("I am setting a Grid Layout")
                print("display me in a Grid")

            else:
                self.libraryListLayout.addWidget(self.mangaObj)
                self.library.setLayout(self.libraryListLayout)
                print("I am setting a List Layout")
                print("display me in a List")

            # self.mangaObj.show()
            # self.mangaObj.activateWindow()
            # self.mangaObj.raise_()
            self.tabWidget.setCurrentIndex(1)
        else:
            self.popDialog('duplicate')

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

    def addMangaWidgetsToLibrary(self, obj):
        if self.viewIsGrid:
            self.libraryGridLayout.addWidget(obj)
            print("display me as Grid")
        else:
            self.libraryListLayout.addWidget(obj)
            print("display me as List")
        self.tabWidget.setCurrentIndex(1)



class Library(QWidget):
    def __init__(self, parent):
        super(Library, self).__init__(parent)
        ...


class Manga(QWidget):
    def __init__(self, metadata, parent):
        super(Manga, self).__init__(parent)
        self.metadata: dict = metadata
        
        self.mangaName = metadata["MangaTitle"]
        self.mangaPath = Path(metadata["MangaPath"])
        self.mangaCover = Path(metadata["MangaCover"])
        self.mangaChapters = metadata["Chapters"]
        self.mangaId = metadata["MangaTitle"]
        self.isFavorite = bool()
        self.bookmarkPosition = object()

        self.mangaBgLayout = QVBoxLayout()
        # self.mangaCoverLabel = QLabel()  #Holds the description page image
        self.mangaCoverDisplayLabel = QLabel()
        self.mangaCoverLayout = QVBoxLayout()
        self.mangaDetailsLayout = QHBoxLayout()
        # self.mangaDetailsWidget = QWidget()
        self.mangaNameLabel = QLabel()
        self.mangaFavoriteButton = QPushButton()
        self.mangaFavoriteButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.mangaFavoriteButtonIcon = QIcon()

        self.mangaCoverPixmap = QPixmap(str(self.mangaCover)).scaled(70, 100, Qt.AspectRatioMode.KeepAspectRatio)
        self.mangaCoverDisplayLabel.setPixmap(self.mangaCoverPixmap)
        self.mangaCoverLayout.addWidget(self.mangaCoverDisplayLabel)

        self.mangaNameLabel.setText(self.mangaName)
        
        self.mangaNameLabelFont = QFont()
        self.mangaNameLabelFont.setPointSize(7)
        self.mangaNameLabelFont.setBold(False)
        self.mangaNameLabel.setFont(self.mangaNameLabelFont)
        self.mangaNameLabel.setAlignment(Qt.AlignmentFlag.AlignLeft)


        self.mangaFavoriteButtonIcon.addPixmap(QPixmap("resources/icons/icons8-favourite-64.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.mangaFavoriteButton.setIcon(self.mangaFavoriteButtonIcon)

        # self.mangaDetailsWidget.setLayout(self.mangaDetailsLayout)
        self.mangaDetailsLayout.addWidget(self.mangaNameLabel)
        self.mangaDetailsLayout.addWidget(self.mangaFavoriteButton)
        
        self.mangaDetailsLayout.setStretch(0, 6)
        self.mangaDetailsLayout.setStretch(1, 1)
        self.mangaDetailsLayout.setSpacing(1)


        self.mangaBgLayout.addLayout(self.mangaCoverLayout)
        self.mangaBgLayout.addLayout(self.mangaDetailsLayout)

        self.mangaBgLayout.setStretch(0, 5)
        self.mangaBgLayout.setStretch(1, 1)


        self.setLayout(self.mangaBgLayout)
        self.setObjectName(self.mangaName)
        self.setFixedSize(QSize(120, 150))
        self.setStyleSheet("QWidget{ background-color: rgb(210, 211, 219); }")
        print("I am now a manga \nMy name is", self.mangaName, "\nMy Image is", self.mangaCover)
        # self.show()

        
    def addToFavorite(self):
        ...

    def deleteSelf(self):
        ...

    
        
        