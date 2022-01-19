import sys
from PyQt6.QtWidgets import (
    QApplication,
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
    QPushButton,
)
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QCursor, QIcon, QPixmap, QFont

"""
from mainWindow import MainWindow 
from pref import Preference
from reader import Reader
"""

class Link(object):

    def talkToStackWidgetIndex(w_index, obj):
        obj.changeStackIndex(obj, w_index)


class MainWindow(QWidget, Link):
    def __init__(self):
        super().__init__()

        self.max_button_size = QSize(50, 50)
        self.min_button_size = QSize(16, 16)
        self.icon_size = QSize(35, 35)

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

        menuIcon = QIcon()
        menuIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-menu-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.menuButton.setIcon(menuIcon)
        self.menuButton.setIconSize(self.icon_size)

        # TextBox
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("Enter Search keyword here... e.g 'Shinkeji no Kyojin', 'Bleach', 'Kimetsu no yaiba' etc...")
        
        self.lineEdit.setSizePolicy(self.sizePolicy)
        self.lineEdit.setMinimumSize(QSize(0, 50))
        self.lineEdit.setMaximumSize(QSize(1366, 50))
        self.lineEdit.setMaxLength(36)
        self.lineEdit.setClearButtonEnabled(True)
     
        # Search Button
        self.searchButton = QPushButton()
        self.searchButton.setCheckable(True)
        
        self.searchButton.setSizePolicy(self.sizePolicy)
        self.searchButton.setMinimumSize(self.min_button_size)
        self.searchButton.setMaximumSize(self.max_button_size)
        self.searchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        searchIcon = QIcon()
        searchIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-search-90.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.searchButton.setIcon(searchIcon)
        self.searchButton.setIconSize(self.icon_size)

        # Local Search
        self.localSearchButton = QPushButton()
        self.localSearchButton.setCheckable(True)
        
        self.localSearchButton.setSizePolicy(self.sizePolicy)
        self.localSearchButton.setMinimumSize(self.min_button_size)
        self.localSearchButton.setMaximumSize(self.max_button_size)
        self.localSearchButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        localSearchIcon = QIcon()
        localSearchIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-plus-math-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.localSearchButton.setIcon(localSearchIcon)
        self.localSearchButton.setIconSize(self.icon_size)


        self.refreshButton = QPushButton()
        self.refreshButton.setCheckable(True)
        self.refreshButton.setSizePolicy(self.sizePolicy)
        self.refreshButton.setMinimumSize(self.max_button_size)
        self.refreshButton.setMaximumSize(self.max_button_size)
        self.refreshButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        
        refreshIcon = QIcon()
        refreshIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-refresh-90.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.refreshButton.setIcon(refreshIcon)
        self.refreshButton.setIconSize(self.icon_size)

        # Add Widgets to searchLayout
        self.searchLayout.addWidget(self.menuButton)
        self.searchLayout.addWidget(self.refreshButton)
        self.searchLayout.addWidget(self.lineEdit)
        self.searchLayout.addWidget(self.searchButton)
        self.searchLayout.addWidget(self.localSearchButton)
        
        self.searchLayout.setStretch(0, 1)
        self.searchLayout.setStretch(1, 1)
        self.searchLayout.setStretch(2, 7)
        self.searchLayout.setStretch(3, 1)
        self.searchLayout.setStretch(4, 1)

        #------------------------------------------------
        # Create another horizontal layout to hold objects of focus
        self.containerLayout = QHBoxLayout()
        # Create a Vetical layout to hold the tabwidget
        self.homeLayout = QVBoxLayout()
        self.create_home_widgets()

        # Create a vertical layout to hold the list of previously read manhuas
        self.historyLayout = QVBoxLayout()
        # Create widgets for the historyLayout
        self.historyLabel = QLabel()
        self.historyLabel.setText("Recent Manhua")
        self.historyLabel.setStyleSheet("background-color: rgb(145, 145, 145); font: 15px;")
        self.historyLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.historyListView = QListView()
        # Add widgets to the historyLayout

        #---------------------------------------------------
        self.toggleLayout = QHBoxLayout()

        self.toggleGridView = QPushButton()
        self.toggleGridView.setCheckable(True)
        self.toggleGridView.setObjectName("toggleGridView")

        #---------------------------------------------------
        
        self.toggleGridView.setSizePolicy(self.sizePolicy)
        self.toggleGridView.setMinimumSize(self.min_button_size * 1.5)
        self.toggleGridView.setMaximumSize(self.min_button_size * 1.5)
        self.toggleGridView.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))


        self.toggleGridIcon = QIcon()
        self.toggleGridIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-grid-96.png"), QIcon.Mode.Normal, QIcon.State.Off)

        self.toggleGridDisabledIcon =QIcon()
        self.toggleGridDisabledIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-grid-disabled-96.png"), QIcon.Mode.Normal, QIcon.State.Off)

        self.toggleGridView.setIcon(self.toggleGridIcon)
        self.toggleGridView.setIconSize(self.icon_size * 0.75)
 

        #----------------------------------------------------

        self.toggleListView = QPushButton()
        self.toggleListView.setCheckable(True)
        self.toggleListView.setObjectName("toggleListView")
        
        self.toggleListView.setSizePolicy(self.sizePolicy)
        self.toggleListView.setMinimumSize(self.min_button_size * 1.5)
        self.toggleListView.setMaximumSize(self.min_button_size * 1.5)
        self.toggleListView.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.toggleListIcon = QIcon()
        self.toggleListIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-list-96.png"), QIcon.Mode.Normal, QIcon.State.Off)

        self.toggleListDisabledIcon =QIcon()
        self.toggleListDisabledIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-list-disabled-96.png"), QIcon.Mode.Normal, QIcon.State.Off)

        self.toggleListView.setIcon(self.toggleListDisabledIcon)
        self.toggleListView.setIconSize(self.icon_size * 0.75)

        #--------------------------------------------------------

        self.toggleList = [self.toggleGridView, self.toggleListView]
        self.toggleViewValue = ["Grid View", "List View"]

        self.viewOptionIndex = 0

        self.view = QLabel(self.toggleViewValue[self.viewOptionIndex])

        self.toggleLayout.addWidget(self.view)
        self.toggleLayout.addWidget(self.toggleList[0])
        self.toggleLayout.addWidget(self.toggleList[1])

        self.toggleLayout.setStretch(0, 4)
        self.toggleLayout.setStretch(1, 1)
        self.toggleLayout.setStretch(2, 1)

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

        #------------------------------------------------
    
        self.style = """
                QPushButton{
                    border-radius:25px;
                }
                QPushButton:hover {
                    background-color: rgba(0,0,0,40);
                    color: white;
                }
                QLineEdit{
                    border: 1px solid rgba(0,0,0,40);
                    border-radius: 25px;
                    padding-left: 25px;
                    font: 13px;
                }
                QStatusBar{
                    background-color: rgba(0,0,0,40);
                }
                QLabel{
                    padding: 10px;
                    border-radius: 10px;
                }

                #toggleGridView, #toggleListView{
                    background-color: none;
                }
            """
        self.setStyleSheet(self.style)
        #-----------------------------------------------
        self.searchButton.clicked.connect(self.search)
        self.lineEdit.returnPressed.connect(self.searchButton.click)
        
        self.menuButton.clicked.connect(self.menuAction)
        self.refreshButton.clicked.connect(self.refreshAction)

        self.toggleGridView.clicked.connect(self.viewTypeGridAction)

        self.toggleListView.clicked.connect(self.viewTypeListAction)
        #-----------------------------------------------


    def create_home_widgets(self):
        self.tabWidget = QTabWidget()
        
        #---------------------------------------------------

        self.home = QWidget()

        homeIcon = QIcon()
        homeIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-home-96.png"), QIcon.Mode.Normal, QIcon.State.Off)

        self.homeTabStackLayout = QVBoxLayout()

        self.homeTabStack = QStackedWidget()

        self.loadHomeTab()

        self.homeTabStack.setCurrentIndex(0)

        #----------------------------------------------------
        self.homeTabStackLayout.addWidget(self.homeTabStack)

        self.home.setLayout(self.homeTabStackLayout)
        #---------------------------------------------------

        self.library = QWidget()
        libraryIcon = QIcon()
        libraryIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-library-96.png"), QIcon.Mode.Normal, QIcon.State.Off)   

        #---------------------------------------------------     
        
        self.tabWidget.addTab(self.home, homeIcon, "Home")
        self.tabWidget.addTab(self.library, libraryIcon, "Library")
        #---------------------------------------------------

        self.tabWidget.setSizePolicy(self.sizePolicy)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.South)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setIconSize(QSize(64, 24))
        #---------------------------------------------------

        self.homeLayout.addWidget(self.tabWidget)



    def loadHomeItems(self):
        pass

    def search(self):
        self.keyword = self.lineEdit.text()
        if self.keyword != "":
            print(self.keyword)


    def menuAction(self):
        Link.talkToStackWidgetIndex(2, Window)

    def refreshAction(self):
        if self.homeTabStack.currentIndex() == 0:
            print("Refused to change Index will refresh instead")
            print(self.homeTabStack.currentIndex())
        else:
            self.homeTabStack.setCurrentIndex(0)
            print(self.homeTabStack.currentIndex())


    def changeStackIndex(self, w_index):
        window.setCurrentIndex(w_index)


    def loadHomeTab(self):
        self.homeDisplay = QWidget()
        self.noInternetDisplay = QWidget()
        self.noSearchResult = QWidget()
        self.searchResultPage = QWidget()
        #---------------------------------------------------

        #----------------------------------------------------
        self.loadHomeDisplay()
        self.loadNoInternetDisplay()
        self.loadNoSearchResult()
        self.loadSearchResultPage()

        #---------------------------------------------------

        self.homeTabStack.addWidget(self.homeDisplay)
        self.homeTabStack.addWidget(self.noInternetDisplay)
        self.homeTabStack.addWidget(self.noSearchResult)
        self.homeTabStack.addWidget(self.searchResultPage)

    
    def loadHomeDisplay(self):
        self.homeDisplayLayout = QGridLayout()

        self.homeDisplay.setLayout(self.homeDisplayLayout)


    def loadNoInternetDisplay(self):
        self.noInternetDisplayLayout = QVBoxLayout()

        self.noInternetDisplayLabelpix = QLabel()
        self.noInternetDisplayLabeltxt = QLabel("No Internet Connection")


        self.noInternetDisplayLabelpix.setSizePolicy(self.sizePolicy) 
        pixPixmap = QPixmap('MangaReader/resources/icons/icons8-without-internet.png')
        self.noInternetDisplayLabelpix.setPixmap(pixPixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))
        self.noInternetDisplayLabelpix.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.noInternetDisplayLabeltxt.setSizePolicy(self.sizePolicy)
        #self.noInternetDisplayLabeltxt.setMaximumHeight(50)
        noInternetDisplayLabelFont = QFont()
        noInternetDisplayLabelFont.setPointSize(16)
        noInternetDisplayLabelFont.setBold(False)
        self.noInternetDisplayLabeltxt.setFont(noInternetDisplayLabelFont)
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
        pixPixmap = QPixmap('MangaReader/resources/icons/page-not-found.png')
        self.noSearchResultLabelpix.setPixmap(pixPixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio))
        self.noSearchResultLabelpix.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.noSearchResultLabeltxt.setSizePolicy(self.sizePolicy)
        #self.noInternetDisplayLabeltxt.setMaximumHeight(50)
        noSearchResultLabelFont = QFont()
        noSearchResultLabelFont.setPointSize(16)
        noSearchResultLabelFont.setBold(False)
        self.noSearchResultLabeltxt.setFont(noSearchResultLabelFont)
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

    def viewTypeGridAction(self):
        if self.toggleGridView.isChecked():
            self.toggleListView.setIcon(self.toggleListDisabledIcon)
            #self.toggleGridView.isChecked = True
        else:
            self.toggleGridView.setIcon(self.toggleGridIcon)
            self.toggleListView.setIcon(self.toggleListDisabledIcon)
            #self.toggleGridView.isChecked = False

        print(self.toggleGridView.isChecked())

    def viewTypeListAction(self):
        if self.toggleListView.isChecked():
            self.toggleListView.setIcon(self.toggleListIcon)
            self.toggleGridView.setIcon(self.toggleGridDisabledIcon)
            #self.toggleListView.isChecked = True
        else:
            self.toggleGridView.setIcon(self.toggleGridIcon)
            #self.toggleListView.isChecked = False

        print(self.toggleListView.isChecked())


    def loadSearchResultPage(self):
        self.resultLayout = QGridLayout()


class Preference(QWidget, Link):
    def __init__(self):
        super().__init__()

        self.max_button_size = QSize(50, 50)
        self.min_button_size = QSize(16, 16)
        self.icon_size = QSize(50, 50)

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
        self.backButton.setGeometry(0, 0, 50, 50)

        # Set backIcon to backButton
        backIcon = QIcon()
        backIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-go-back-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
        self.backButton.setIcon(backIcon)
        self.backButton.setIconSize(self.icon_size)
        self.backButton.setCheckable(True)

        #-----------------------------------------------
        self.headerLabel = QLabel("Preference | Settings")
        self.headerLabel.setSizePolicy(self.sizePolicy)
        self.headerLabel.setMaximumHeight(50)
        headerLabelFont = QFont()
        headerLabelFont.setPointSize(16)
        headerLabelFont.setBold(True)
        self.headerLabel.setFont(headerLabelFont)
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
        self.settingsButton.setSizePolicy(self.sizePolicy)
        self.settingsButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.settingsButton.setObjectName("settingsButton")

        self.downloadButton = QPushButton("Downloads")
        self.downloadButton.setSizePolicy(self.sizePolicy)
        self.downloadButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.downloadButton.setObjectName("downloadButton")

        self.themesButton = QPushButton("Themes")
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
        self.buttonsLayout.setStretch(3, 7)


        #-----------------------------------------------
        self.stackLayout = QVBoxLayout()
        self.stackedWidget = QStackedWidget()

        self.settingsWidget = QWidget()
        self.downloadsWidget = QWidget()
        self.themesWidget = QWidget()

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
        self.baseLayout.addLayout(self.headerLayout)
        self.baseLayout.addLayout(self.bodyLayout)

        self.baseLayout.setStretch(0, 2)
        self.baseLayout.setStretch(1, 12)
        #-----------------------------------------------

        self.gridLayout.addLayout(self.baseLayout, 0, 0, 1, 1)

        self.setLayout(self.gridLayout)

        self.style = """
                QPushButton{
                    border-radius: 25px;
                }
                QPushButton:hover {
                    background-color: rgba(0,0,0,40);
                    color: white;
                }
                QLabel{
                    padding: 1px;
                    background-color: rgba(0,0,0,40);
                    border-radius: 25px;
                }
                #settingsButton, #downloadButton, #themesButton{
                    border-radius: 15px;
                }
        """

        self.setStyleSheet(self.style)

        #-----------------------------------------------

        self.backButton.clicked.connect(self.backAction)

    def backAction(self):
        Link.talkToStackWidgetIndex(0, Window)

    def changeStackIndex(self, w_index):
        self.setCurrentIndex(w_index)


class Reader(QWidget, Link):
    def __init__(self):
        super().__init__()


class Window(QStackedWidget):
    def __init__(self):
        super().__init__()
        #self.screen_width = 1366
        #self.screen_height = 768
        self.min_screen_width = 915
        self.min_screen_height = 515
        self.resize_width = 1092
        self.resize_height = 614
        self.appWindowTitle = "Manhua Reader"
        self.resize(QSize(self.resize_width, self.resize_height))
        self.setMinimumSize(QSize(self.min_screen_width, self.min_screen_height))
        self.setWindowTitle(self.appWindowTitle)
        
        self.objMainWindow = MainWindow()
        self.objReader = Reader()
        self.objPref = Preference()

        self.addWidget(self.objMainWindow)
        self.addWidget(self.objReader)
        self.addWidget(self.objPref)
        print(self.count())

    def changeStackIndex(self, w_index):
        window.setCurrentIndex(w_index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.showMaximized()
    windowIcon = QIcon()
    windowIcon.addPixmap(QPixmap("MangaReader/resources/icons/icons8-library-96.png"), QIcon.Mode.Normal, QIcon.State.Off)
    window.setWindowIcon(windowIcon)
    sys.exit(app.exec())