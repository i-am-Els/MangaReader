from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QTabWidget,
    QWidget,
    QLineEdit,
    QLabel,
    QListView,
    QPushButton,
)

from PyQt6.QtCore import QSize, Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.screen_width = 1366
        self.screen_height = 768
        self.min_screen_width = 1092
        self.min_screen_height = 614
        self.appWindowTitle = "Manhua Reader"
        self.setMinimumSize(QSize(self.min_screen_width, self.min_screen_height))
        self.setWindowTitle(self.appWindowTitle)
        #------------------------------------------------
        self.centralwidget = QWidget()
        #------------------------------------------------
        self.gridLayout = QGridLayout(self.centralwidget)
        #------------------------------------------------
        # Create a centralLayout to hold all other layouts
        self.centralLayout = QVBoxLayout()
        #------------------------------------------------
        # Create an horizontal layout to hold all search functions
        self.searchLayout = QHBoxLayout()
        # Create search function widgets
        # Menu/Option button 
        self.menuButton = QPushButton()
        # TextBox
        self.lineEdit = QLineEdit()
        # Search Button
        self.searchButton = QPushButton()
        # Local Search
        self.localSearchButton = QPushButton()
        # Add Widgets to searchLayout
        self.searchLayout.addWidget(self.menuButton)
        self.searchLayout.addWidget(self.lineEdit)
        self.searchLayout.addWidget(self.searchButton)
        self.searchLayout.addWidget(self.localSearchButton)
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
        self.historyListView = QListView()
        # Add widgets to the historyLayout
        self.historyLayout.addWidget(self.historyLabel)    
        self.historyLayout.addWidget(self.historyListView)    
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
        #------------------------------------------------
        self.gridLayout.addLayout(self.centralLayout, 0, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)

    def create_home_widgets(self):
        self.tabWidget = QTabWidget()
        self.home = QWidget()
        self.library = QWidget()
        self.tabWidget.addTab(self.home, "Home")
        self.tabWidget.addTab(self.library, "library")

        self.tabWidget.setCurrentIndex(0)
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)

        self.homeLayout.addWidget(self.tabWidget)
        

    def create_library_widgets(self):
        pass
     
            
    def create_stack_widget_home(self):
        #create_home_widgets()
        pass


    def create_stack_widget_library(self):
        #create_library_widgets()
        pass