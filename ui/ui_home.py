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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QWidget)
import resource_rc

class Ui_home(object):
    def setupUi(self, home):
        if not home.objectName():
            home.setObjectName(u"home")
        home.resize(900, 630)
        home.setMaximumSize(QSize(900, 630))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(39, 43, 140, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(240, 253, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(113, 125, 127, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(151, 167, 170, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 127))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush8 = QBrush(QColor(226, 251, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush9 = QBrush(QColor(113, 125, 127, 127))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush2)
        home.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(14)
        home.setFont(font)
        home.setStyleSheet(u"background-color: rgb(39, 43, 140);")
        home.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        home.setDocumentMode(True)
        home.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(home)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(850, 605))
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
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
        self.whitebox = QGroupBox(self.groupBox_2)
        self.whitebox.setObjectName(u"whitebox")
        self.whitebox.setEnabled(True)
        self.whitebox.setGeometry(QRect(240, -50, 421, 701))
        self.whitebox.setMinimumSize(QSize(300, 542))
        self.whitebox.setStyleSheet(u"background-color: #e2fbff;\n"
"border-radius: 30px")
        self.whitebox.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.whitebox.setFlat(True)
        self.groupBox = QGroupBox(self.whitebox)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(50, 240, 321, 321))
        self.progressbutton = QPushButton(self.groupBox)
        self.progressbutton.setObjectName(u"progressbutton")
        self.progressbutton.setGeometry(QRect(30, 140, 261, 71))
        font2 = QFont()
        font2.setFamilies([u"Baloo Chettan 2"])
        font2.setPointSize(25)
        font2.setBold(True)
        self.progressbutton.setFont(font2)
        self.progressbutton.setStyleSheet(u"background-color: #00dacc;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.progressbutton.setFlat(False)
        self.startbutton = QPushButton(self.groupBox)
        self.startbutton.setObjectName(u"startbutton")
        self.startbutton.setGeometry(QRect(30, 40, 261, 71))
        self.startbutton.setFont(font2)
        self.startbutton.setStyleSheet(u"background-color: #00dacc;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.startbutton.setFlat(False)
        self.logoutbutton = QPushButton(self.groupBox)
        self.logoutbutton.setObjectName(u"logoutbutton")
        self.logoutbutton.setGeometry(QRect(30, 240, 261, 71))
        self.logoutbutton.setFont(font2)
        self.logoutbutton.setStyleSheet(u"background-color: #00dacc;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.logoutbutton.setFlat(False)
        self.typerush = QLabel(self.whitebox)
        self.typerush.setObjectName(u"typerush")
        self.typerush.setGeometry(QRect(0, 120, 421, 91))
        font3 = QFont()
        font3.setFamilies([u"Baloo Chettan 2"])
        font3.setPointSize(69)
        font3.setBold(True)
        self.typerush.setFont(font3)
        self.typerush.setStyleSheet(u"color: rgb(39, 43, 140)")
        self.typerush.setFrameShadow(QFrame.Shadow.Sunken)
        self.typerush.setMidLineWidth(0)
        self.typerush.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitle = QLabel(self.whitebox)
        self.subtitle.setObjectName(u"subtitle")
        self.subtitle.setGeometry(QRect(30, 210, 371, 31))
        font4 = QFont()
        font4.setFamilies([u"Baloo Chettan 2"])
        font4.setPointSize(24)
        self.subtitle.setFont(font4)
        self.subtitle.setStyleSheet(u"color: rgb(42, 47, 152)")
        self.subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bg_image = QLabel(self.groupBox_2)
        self.bg_image.setObjectName(u"bg_image")
        self.bg_image.setGeometry(QRect(-30, -20, 961, 671))
        self.bg_image.setAutoFillBackground(False)
        self.bg_image.setPixmap(QPixmap(u":/cool/assets/typinggame.png"))
        self.bg_image.setScaledContents(True)
        self.bg_image.setMargin(21)
        self.bg_image.raise_()
        self.whitebox.raise_()

        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        home.setCentralWidget(self.centralwidget)

        self.retranslateUi(home)

        self.progressbutton.setDefault(False)
        self.startbutton.setDefault(False)
        self.logoutbutton.setDefault(False)


        QMetaObject.connectSlotsByName(home)
    # setupUi

    def retranslateUi(self, home):
        home.setWindowTitle(QCoreApplication.translate("home", u"typeRush", None))
#if QT_CONFIG(whatsthis)
        home.setWhatsThis(QCoreApplication.translate("home", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.groupBox.setTitle("")
        self.progressbutton.setText(QCoreApplication.translate("home", u"View Progress", None))
        self.startbutton.setText(QCoreApplication.translate("home", u"Start test", None))
        self.logoutbutton.setText(QCoreApplication.translate("home", u"Logout", None))
        self.typerush.setText(QCoreApplication.translate("home", u"typeRush", None))
        self.subtitle.setText(QCoreApplication.translate("home", u"Type Fast. Think Future. ", None))
        self.bg_image.setText("")
    # retranslateUi

