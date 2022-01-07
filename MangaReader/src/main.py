from PyQt6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QGridLayout,
    QTabWidget,
    QWidget,
    QLineEdit,
    QPushButton,
)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.screen_width = 1366
        self.screen_height = 768
        self.appWindowTitle = "Manhua Reader"
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

        # Create a vertical layout to hold the list of previously read manhuas
        self.historyLayout = QVBoxLayout()

                
        # Add homeLayout and historyLayout to containerLayout
        self.containerLayout.addLayout(self.homeLayout)
        self.containerLayout.addLayout(self.historyLayout)
        #------------------------------------------------

        #Add searchLayout and containerLayout to centralLayout
        self.centralLayout.addLayout(self.searchLayout)
        self.centralLayout.addLayout(self.containerLayout)




    def create_home_widgets(self):
        self.tabWidget = QTabWidget()
        self.tabWidget.setTabPosition(QTabWidget.TabPosition.West)
        self.tabWidget.setTabShape(QTabWidget.TabShape.Triangular)
        self.home = QWidget()
        self.library = QWidget()
        #self.homeLayout.addWidget(...)
        pass

    def create_library_widgets(self):
        pass
            
    def create_stack_widget_home(self):
        #create_home_widgets()
        pass

    def create_stack_widget_library(self):
        #create_library_widgets()
        pass