# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QGroupBox,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(835, 605)
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: #00444d\n"
"")
        MainWindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        MainWindow.setDocumentMode(True)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.settings = QGroupBox(self.widget)
        self.settings.setObjectName(u"settings")
        self.settings.setEnabled(True)
        self.settings.setGeometry(QRect(370, 10, 500, 571))
        self.settings.setMinimumSize(QSize(500, 535))
        self.settings.setStyleSheet(u"background-color: #e2fffc;\n"
"border-radius: 30px")
        self.groupBox = QGroupBox(self.settings)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(70, 150, 311, 301))
        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(30, 170, 261, 71))
        font1 = QFont()
        font1.setFamilies([u"Baloo Chettan 2"])
        font1.setPointSize(25)
        font1.setBold(True)
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"background-color: #00798a;\n"
"border-radius: 15px")
        self.pushButton_3.setFlat(False)
        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(30, 50, 261, 71))
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"background-color: #00798a;\n"
"border-radius: 15px")
        self.pushButton_4.setFlat(False)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(-10, 10, 331, 581))

        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pushButton_3.setDefault(False)
        self.pushButton_4.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"typeRush", None))
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>harmonize</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBox.setTitle("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Register", None))
    # retranslateUi

