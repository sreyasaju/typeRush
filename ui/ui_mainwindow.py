# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(850, 605)
        MainWindow.setMaximumSize(QSize(850, 605))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(39, 43, 140);")
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MainWindow.setDocumentMode(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(850, 605))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, -1, 0)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font1 = QFont()
        font1.setKerning(True)
        self.groupBox_2.setFont(font1)
        self.groupBox_2.setAutoFillBackground(False)
        self.groupBox_2.setStyleSheet(u"background-color: rgb(39, 43, 140)\n"
"")
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 180, 291, 91))
        font2 = QFont()
        font2.setFamilies([u"Baloo Chettan 2"])
        font2.setPointSize(69)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"")
        self.label.setFrameShadow(QFrame.Shadow.Sunken)
        self.label.setMidLineWidth(0)
        self.settings = QGroupBox(self.groupBox_2)
        self.settings.setObjectName(u"settings")
        self.settings.setEnabled(True)
        self.settings.setGeometry(QRect(400, 30, 455, 551))
        self.settings.setMinimumSize(QSize(455, 535))
        self.settings.setStyleSheet(u"background-color: #e2fbff;\n"
"border-radius: 30px")
        self.settings.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.settings.setFlat(True)
        self.groupBox = QGroupBox(self.settings)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(60, 150, 321, 301))
        self.loginbutton = QPushButton(self.groupBox)
        self.loginbutton.setObjectName(u"loginbutton")
        self.loginbutton.setGeometry(QRect(30, 170, 261, 71))
        font3 = QFont()
        font3.setFamilies([u"Baloo Chettan 2"])
        font3.setPointSize(25)
        font3.setBold(True)
        self.loginbutton.setFont(font3)
        self.loginbutton.setStyleSheet(u"background-color: #00dacc;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.loginbutton.setFlat(False)
        self.registerbutton = QPushButton(self.groupBox)
        self.registerbutton.setObjectName(u"registerbutton")
        self.registerbutton.setGeometry(QRect(30, 50, 261, 71))
        self.registerbutton.setFont(font3)
        self.registerbutton.setStyleSheet(u"background-color: #00dacc;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.registerbutton.setFlat(False)
        self.bg_image = QLabel(self.groupBox_2)
        self.bg_image.setObjectName(u"bg_image")
        self.bg_image.setGeometry(QRect(-20, -60, 471, 691))
        self.bg_image.setAutoFillBackground(False)
        self.bg_image.setPixmap(QPixmap(u"assets/underwater2.png"))
        self.bg_image.setScaledContents(True)
        self.bg_image.setMargin(21)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(70, 270, 251, 31))
        font4 = QFont()
        font4.setFamilies([u"Baloo Chettan 2"])
        font4.setPointSize(24)
        self.label_2.setFont(font4)
        self.bg_image.raise_()
        self.settings.raise_()
        self.label.raise_()
        self.label_2.raise_()

        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.loginbutton.setDefault(False)
        self.registerbutton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"typeRush", None))
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>harmonize</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.label.setText(QCoreApplication.translate("MainWindow", u"typeRush", None))
        self.groupBox.setTitle("")
        self.loginbutton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.registerbutton.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.bg_image.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Type Fast. Think Future. ", None))
    # retranslateUi

