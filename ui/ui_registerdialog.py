# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'registerdialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_registerDialog(object):
    def setupUi(self, registerDialog):
        if not registerDialog.objectName():
            registerDialog.setObjectName(u"registerDialog")
        registerDialog.resize(420, 350)
        registerDialog.setMinimumSize(QSize(420, 350))
        registerDialog.setMaximumSize(QSize(420, 350))
        palette = QPalette()
        brush = QBrush(QColor(0, 75, 87, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(226, 251, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush2)
        brush3 = QBrush(QColor(5, 59, 55, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        registerDialog.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Baloo Chettan 2"])
        font.setPointSize(18)
        registerDialog.setFont(font)
        registerDialog.setStyleSheet(u"background-color: #e2fbff;\n"
"border-radius: 30px;\n"
"\n"
"QMessageBox {\n"
"        background-color: #e6faff;\n"
"        font-size: 14px;\n"
"		font-family: /assets/font/BalooChettan2-VariableFont_wght.ttf\n"
"   };\n"
"    QMessageBox QLabel {\n"
"        color: rgb(0, 83, 60);\n"
"  };\n"
"  QMessageBox QPushButton {\n"
"        background-color: rgb(0, 218, 204);\n"
"        color: white;\n"
"        border-radius: 6px;\n"
"        padding: 4px 10px;\n"
"  };\n"
"   QMessageBox QPushButton:hover {\n"
"        background-color: #00b3a4;\n"
"    };")
        self.groupBox = QGroupBox(registerDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 420, 350))
        self.groupBox.setMinimumSize(QSize(420, 350))
        self.groupBox.setMaximumSize(QSize(420, 350))
        self.groupBox.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.reg_passwordField = QLineEdit(self.groupBox)
        self.reg_passwordField.setObjectName(u"reg_passwordField")
        self.reg_passwordField.setGeometry(QRect(30, 160, 341, 61))
        font1 = QFont()
        font1.setFamilies([u"Baloo Chettan 2"])
        font1.setPointSize(16)
        self.reg_passwordField.setFont(font1)
        self.reg_passwordField.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border-width: 10px;\n"
"border-style: medium;\n"
"border-color: rgb(0, 207, 230);\n"
"padding: 12px;\n"
"color:rgb(10, 24, 25);")
        self.reg_passwordField.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.reg_usernameField = QLineEdit(self.groupBox)
        self.reg_usernameField.setObjectName(u"reg_usernameField")
        self.reg_usernameField.setGeometry(QRect(30, 90, 341, 61))
        self.reg_usernameField.setFont(font1)
        self.reg_usernameField.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border-width: 10px;\n"
"border-style: medium;\n"
"border-color: rgb(0, 207, 230);\n"
"padding: 12px;\n"
"color:rgb(10, 24, 25);")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 50, 81, 21))
        font2 = QFont()
        font2.setFamilies([u"Baloo Chettan 2"])
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setKerning(False)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: #00cbbc")
        self.reg_cancel = QPushButton(self.groupBox)
        self.reg_cancel.setObjectName(u"reg_cancel")
        self.reg_cancel.setGeometry(QRect(80, 260, 111, 41))
        font3 = QFont()
        font3.setFamilies([u"Baloo Chettan 2"])
        font3.setPointSize(18)
        font3.setBold(True)
        self.reg_cancel.setFont(font3)
        self.reg_cancel.setStyleSheet(u"background-color: #00dacc;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.reg_cancel.setFlat(False)
        self.reg_ok = QPushButton(self.groupBox)
        self.reg_ok.setObjectName(u"reg_ok")
        self.reg_ok.setGeometry(QRect(210, 260, 111, 41))
        self.reg_ok.setFont(font3)
        self.reg_ok.setStyleSheet(u"background-color: #00dacc;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.reg_ok.setFlat(False)

        self.retranslateUi(registerDialog)

        self.reg_cancel.setDefault(False)
        self.reg_ok.setDefault(False)


        QMetaObject.connectSlotsByName(registerDialog)
    # setupUi

    def retranslateUi(self, registerDialog):
        registerDialog.setWindowTitle(QCoreApplication.translate("registerDialog", u"Register", None))
        self.groupBox.setTitle("")
        self.reg_passwordField.setPlaceholderText(QCoreApplication.translate("registerDialog", u"Password", None))
        self.reg_usernameField.setPlaceholderText(QCoreApplication.translate("registerDialog", u"Username", None))
        self.label.setText(QCoreApplication.translate("registerDialog", u"Register", None))
        self.reg_cancel.setText(QCoreApplication.translate("registerDialog", u"Cancel", None))
        self.reg_ok.setText(QCoreApplication.translate("registerDialog", u"OK", None))
    # retranslateUi

