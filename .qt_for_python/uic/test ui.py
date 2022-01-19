# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test ui.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListView,
    QMainWindow, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(627, 484)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.centralLayout = QVBoxLayout()
        self.centralLayout.setSpacing(9)
        self.centralLayout.setObjectName(u"centralLayout")
        self.searchLayout = QHBoxLayout()
        self.searchLayout.setSpacing(4)
        self.searchLayout.setObjectName(u"searchLayout")
        self.searchLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.searchLayout.setContentsMargins(-1, 12, -1, 12)
        self.menuButton = QPushButton(self.centralwidget)
        self.menuButton.setObjectName(u"menuButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuButton.sizePolicy().hasHeightForWidth())
        self.menuButton.setSizePolicy(sizePolicy)
        self.menuButton.setMinimumSize(QSize(16, 16))
        self.menuButton.setMaximumSize(QSize(50, 50))
        self.menuButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuButton.setStyleSheet(u"QPushButton{\n"
"	border-radius: 25;\n"
"	border: 2px solid black;\n"
"}")
        icon = QIcon()
        icon.addFile(u"MangaReader/resources/icons/icons8-menu-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(45, 35))

        self.searchLayout.addWidget(self.menuButton)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(0, 50))
        self.lineEdit.setMaximumSize(QSize(1366, 50))
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	border: 2px solid gray;\n"
"	border-radius: 25px;\n"
"}")
        self.lineEdit.setInputMethodHints(Qt.ImhNone)
        self.lineEdit.setMaxLength(32767)
        self.lineEdit.setClearButtonEnabled(True)

        self.searchLayout.addWidget(self.lineEdit)

        self.searchButton = QPushButton(self.centralwidget)
        self.searchButton.setObjectName(u"searchButton")
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setMinimumSize(QSize(16, 16))
        self.searchButton.setMaximumSize(QSize(50, 50))
        self.searchButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.searchButton.setStyleSheet(u"QPushButton{\n"
"	border-radius: 25;\n"
"	border: 2px solid black;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"MangaReader/resources/icons/icons8-search-90.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon1)
        self.searchButton.setIconSize(QSize(43, 43))

        self.searchLayout.addWidget(self.searchButton)

        self.localSearchButton = QPushButton(self.centralwidget)
        self.localSearchButton.setObjectName(u"localSearchButton")
        sizePolicy.setHeightForWidth(self.localSearchButton.sizePolicy().hasHeightForWidth())
        self.localSearchButton.setSizePolicy(sizePolicy)
        self.localSearchButton.setMinimumSize(QSize(16, 16))
        self.localSearchButton.setMaximumSize(QSize(50, 50))
        self.localSearchButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.localSearchButton.setStyleSheet(u"QPushButton{\n"
"	border-radius: 25;\n"
"	border: 2px solid black;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"MangaReader/resources/icons/icons8-plus-math-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.localSearchButton.setIcon(icon2)
        self.localSearchButton.setIconSize(QSize(50, 50))

        self.searchLayout.addWidget(self.localSearchButton)

        self.searchLayout.setStretch(0, 1)
        self.searchLayout.setStretch(1, 7)
        self.searchLayout.setStretch(2, 1)
        self.searchLayout.setStretch(3, 1)

        self.centralLayout.addLayout(self.searchLayout)

        self.containerLayout = QHBoxLayout()
        self.containerLayout.setSpacing(1)
        self.containerLayout.setObjectName(u"containerLayout")
        self.homeLayout = QVBoxLayout()
        self.homeLayout.setObjectName(u"homeLayout")
        self.homeLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setCursor(QCursor(Qt.ArrowCursor))
        self.tabWidget.setFocusPolicy(Qt.TabFocus)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setIconSize(QSize(64, 24))
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.Home.setEnabled(True)
        icon3 = QIcon()
        icon3.addFile(u"MangaReader/resources/icons/icons8-home-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.Home, icon3, "")
        self.Library = QWidget()
        self.Library.setObjectName(u"Library")
        self.Library.setCursor(QCursor(Qt.ArrowCursor))
        icon4 = QIcon()
        icon4.addFile(u"MangaReader/resources/icons/icons8-library-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.Library, icon4, "")

        self.homeLayout.addWidget(self.tabWidget)


        self.containerLayout.addLayout(self.homeLayout)

        self.historyLayout = QVBoxLayout()
        self.historyLayout.setSpacing(4)
        self.historyLayout.setObjectName(u"historyLayout")
        self.historyLabel = QLabel(self.centralwidget)
        self.historyLabel.setObjectName(u"historyLabel")
        self.historyLabel.setStyleSheet(u"background-color: rgb(145, 145, 145);")
        self.historyLabel.setAlignment(Qt.AlignCenter)

        self.historyLayout.addWidget(self.historyLabel)

        self.historyListView = QListView(self.centralwidget)
        self.historyListView.setObjectName(u"historyListView")
        self.historyListView.setStyleSheet(u"QFrame{\n"
"	border: 2px solid gray;\n"
"	border-radius: 5px;\n"
"}\n"
"QListview{\n"
"	border: 2px solid gray;\n"
"	border-radius: 15px;\n"
"}\n"
"")
        self.historyListView.setFrameShape(QFrame.NoFrame)
        self.historyListView.setFrameShadow(QFrame.Plain)
        self.historyListView.setLineWidth(0)
        self.historyListView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

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
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setStyleSheet(u"background-color: rgb(196, 255, 215);")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuButton.setText("")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Enter Keyword here...", None))
        self.searchButton.setText("")
        self.localSearchButton.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home), QCoreApplication.translate("MainWindow", u"Home", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Library), QCoreApplication.translate("MainWindow", u"Library", None))
        self.historyLabel.setText(QCoreApplication.translate("MainWindow", u"Recent Manhuas", None))
    # retranslateUi

