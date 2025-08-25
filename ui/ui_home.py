# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_home(object):
    def setupUi(self, home):
        if not home.objectName():
            home.setObjectName(u"home")
        home.resize(800, 600)
        home.setMinimumSize(QSize(800, 600))
        home.setStyleSheet(u"background-color: #e2fbff;")
        self.centralwidget = QWidget(home)
        self.centralwidget.setObjectName(u"centralwidget")
        self.settings = QGroupBox(self.centralwidget)
        self.settings.setObjectName(u"settings")
        self.settings.setEnabled(True)
        self.settings.setGeometry(QRect(180, 0, 455, 535))
        self.settings.setMinimumSize(QSize(455, 535))
        self.settings.setStyleSheet(u"background-color: #e2fbff;\n"
"border-radius: 30px")
        self.settings.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.groupBox = QGroupBox(self.settings)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(60, 180, 321, 301))
        self.loginbutton = QPushButton(self.groupBox)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setGeometry(QRect(30, 110, 261, 61))
        font = QFont()
        font.setFamilies([u"Baloo Chettan 2"])
        font.setPointSize(25)
        font.setBold(True)
        self.loginbutton.setFont(font)
        self.loginbutton.setStyleSheet(u"background-color: #00dacc;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.loginbutton.setFlat(False)
        self.registerbutton = QPushButton(self.groupBox)
        self.registerbutton.setObjectName(u"registerbutton")
        self.registerbutton.setGeometry(QRect(30, 20, 261, 61))
        self.registerbutton.setFont(font)
        self.registerbutton.setStyleSheet(u"background-color: #00dacc;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.registerbutton.setFlat(False)
        self.loginbutton_2 = QPushButton(self.groupBox)
        self.loginbutton_2.setObjectName(u"loginbutton_2")
        self.loginbutton_2.setGeometry(QRect(30, 200, 261, 61))
        self.loginbutton_2.setFont(font)
        self.loginbutton_2.setStyleSheet(u"background-color: #00dacc;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.loginbutton_2.setFlat(False)
        self.subtitle = QLabel(self.settings)
        self.subtitle.setObjectName(u"subtitle")
        self.subtitle.setGeometry(QRect(100, 140, 251, 31))
        font1 = QFont()
        font1.setFamilies([u"Baloo Chettan 2"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.subtitle.setFont(font1)
        self.subtitle.setStyleSheet(u"color: #393fbf")
        self.typerush = QLabel(self.settings)
        self.typerush.setObjectName(u"typerush")
        self.typerush.setGeometry(QRect(80, 50, 301, 91))
        font2 = QFont()
        font2.setFamilies([u"Baloo Chettan 2"])
        font2.setPointSize(69)
        font2.setBold(True)
        self.typerush.setFont(font2)
        self.typerush.setStyleSheet(u"color: rgb(39, 43, 140);")
        self.typerush.setFrameShadow(QFrame.Shadow.Sunken)
        self.typerush.setMidLineWidth(0)
        home.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(home)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        home.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(home)
        self.statusbar.setObjectName(u"statusbar")
        home.setStatusBar(self.statusbar)

        self.retranslateUi(home)

        self.loginbutton.setDefault(False)
        self.registerbutton.setDefault(False)
        self.loginbutton_2.setDefault(False)


        QMetaObject.connectSlotsByName(home)
    # setupUi

    def retranslateUi(self, home):
        home.setWindowTitle(QCoreApplication.translate("home", u"typeRush", None))
        self.groupBox.setTitle("")
        self.loginbutton.setText(QCoreApplication.translate("home", u"View Progress", None))
        self.registerbutton.setText(QCoreApplication.translate("home", u"Start Test", None))
        self.loginbutton_2.setText(QCoreApplication.translate("home", u"Logout ", None))
        self.subtitle.setText(QCoreApplication.translate("home", u"Type Fast. Think Future. ", None))
        self.typerush.setText(QCoreApplication.translate("home", u"typeRush", None))
    # retranslateUi

