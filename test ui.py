# Form implementation generated from reading ui file 'test ui.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(627, 484)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.centralLayout = QtWidgets.QVBoxLayout()
        self.centralLayout.setSpacing(9)
        self.centralLayout.setObjectName("centralLayout")
        self.searchLayout = QtWidgets.QHBoxLayout()
        self.searchLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.searchLayout.setContentsMargins(-1, 12, -1, 12)
        self.searchLayout.setSpacing(4)
        self.searchLayout.setObjectName("searchLayout")
        self.menuButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuButton.sizePolicy().hasHeightForWidth())
        self.menuButton.setSizePolicy(sizePolicy)
        self.menuButton.setMinimumSize(QtCore.QSize(16, 16))
        self.menuButton.setMaximumSize(QtCore.QSize(50, 50))
        self.menuButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.menuButton.setStyleSheet("QPushButton{\n"
"    border-radius: 25;\n"
"    border: 2px solid black;\n"
"}")
        self.menuButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("MangaReader/resources/icons/icons8-menu-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QtCore.QSize(45, 35))
        self.menuButton.setObjectName("menuButton")
        self.searchLayout.addWidget(self.menuButton)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 50))
        self.lineEdit.setMaximumSize(QtCore.QSize(1366, 50))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    border-radius: 25px;\n"
"}")
        self.lineEdit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setObjectName("lineEdit")
        self.searchLayout.addWidget(self.lineEdit)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setMinimumSize(QtCore.QSize(16, 16))
        self.searchButton.setMaximumSize(QtCore.QSize(50, 50))
        self.searchButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.searchButton.setStyleSheet("QPushButton{\n"
"    border-radius: 25;\n"
"    border: 2px solid black;\n"
"}")
        self.searchButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("MangaReader/resources/icons/icons8-search-90.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.searchButton.setIcon(icon1)
        self.searchButton.setIconSize(QtCore.QSize(43, 43))
        self.searchButton.setObjectName("searchButton")
        self.searchLayout.addWidget(self.searchButton)
        self.localSearchButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.localSearchButton.sizePolicy().hasHeightForWidth())
        self.localSearchButton.setSizePolicy(sizePolicy)
        self.localSearchButton.setMinimumSize(QtCore.QSize(16, 16))
        self.localSearchButton.setMaximumSize(QtCore.QSize(50, 50))
        self.localSearchButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.localSearchButton.setStyleSheet("QPushButton{\n"
"    border-radius: 25;\n"
"    border: 2px solid black;\n"
"}")
        self.localSearchButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("MangaReader/resources/icons/icons8-plus-math-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.localSearchButton.setIcon(icon2)
        self.localSearchButton.setIconSize(QtCore.QSize(50, 50))
        self.localSearchButton.setObjectName("localSearchButton")
        self.searchLayout.addWidget(self.localSearchButton)
        self.searchLayout.setStretch(0, 1)
        self.searchLayout.setStretch(1, 7)
        self.searchLayout.setStretch(2, 1)
        self.searchLayout.setStretch(3, 1)
        self.centralLayout.addLayout(self.searchLayout)
        self.containerLayout = QtWidgets.QHBoxLayout()
        self.containerLayout.setSpacing(1)
        self.containerLayout.setObjectName("containerLayout")
        self.homeLayout = QtWidgets.QVBoxLayout()
        self.homeLayout.setObjectName("homeLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.tabWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.TabFocus)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.tabWidget.setIconSize(QtCore.QSize(64, 24))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.Home = QtWidgets.QWidget()
        self.Home.setEnabled(True)
        self.Home.setObjectName("Home")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("MangaReader/resources/icons/icons8-home-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.Home, icon3, "")
        self.Library = QtWidgets.QWidget()
        self.Library.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.Library.setObjectName("Library")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("MangaReader/resources/icons/icons8-library-96.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.tabWidget.addTab(self.Library, icon4, "")
        self.homeLayout.addWidget(self.tabWidget)
        self.containerLayout.addLayout(self.homeLayout)
        self.historyLayout = QtWidgets.QVBoxLayout()
        self.historyLayout.setSpacing(4)
        self.historyLayout.setObjectName("historyLayout")
        self.historyLabel = QtWidgets.QLabel(self.centralwidget)
        self.historyLabel.setStyleSheet("background-color: rgb(145, 145, 145);")
        self.historyLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.historyLabel.setObjectName("historyLabel")
        self.historyLayout.addWidget(self.historyLabel)
        self.historyListView = QtWidgets.QListView(self.centralwidget)
        self.historyListView.setStyleSheet("QFrame{\n"
"    border: 2px solid gray;\n"
"    border-radius: 5px;\n"
"}\n"
"QListview{\n"
"    border: 2px solid gray;\n"
"    border-radius: 15px;\n"
"}\n"
"")
        self.historyListView.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.historyListView.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.historyListView.setLineWidth(0)
        self.historyListView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.historyListView.setObjectName("historyListView")
        self.historyLayout.addWidget(self.historyListView)
        self.historyLayout.setStretch(0, 1)
        self.historyLayout.setStretch(1, 13)
        self.containerLayout.addLayout(self.historyLayout)
        self.containerLayout.setStretch(0, 7)
        self.containerLayout.setStretch(1, 3)
        self.centralLayout.addLayout(self.containerLayout)
        self.centralLayout.setStretch(0, 2)
        self.centralLayout.setStretch(1, 12)
        self.gridLayout.addLayout(self.centralLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("background-color: rgb(196, 255, 215);")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Enter Keyword here..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home), _translate("MainWindow", "Home"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Library), _translate("MainWindow", "Library"))
        self.historyLabel.setText(_translate("MainWindow", "Recent Manhuas"))