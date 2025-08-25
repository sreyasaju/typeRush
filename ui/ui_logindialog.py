# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logindialog.ui'
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

class Ui_loginDialog(object):
    def setupUi(self, loginDialog):
        if not loginDialog.objectName():
            loginDialog.setObjectName(u"loginDialog")
        loginDialog.resize(420, 350)
        loginDialog.setMinimumSize(QSize(420, 350))
        loginDialog.setMaximumSize(QSize(420, 350))
        loginDialog.setStyleSheet(u"background-color: #e2fbff;\n"
"border-radius: 30px;\n"
"\n"
"QMessageBox {\n"
"    color: rgb(11, 68, 77);\n"
"    font-size: 14px;\n"
"}\n"
"")
        self.groupBox = QGroupBox(loginDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 420, 350))
        self.groupBox.setMinimumSize(QSize(420, 350))
        self.groupBox.setMaximumSize(QSize(420, 350))
        self.log_passwordField = QLineEdit(self.groupBox)
        self.log_passwordField.setObjectName(u"log_passwordField")
        self.log_passwordField.setGeometry(QRect(30, 160, 341, 61))
        font = QFont()
        font.setFamilies([u"Baloo Chettan 2"])
        font.setPointSize(16)
        self.log_passwordField.setFont(font)
        self.log_passwordField.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border-width: 10px;\n"
"border-style: medium;\n"
"border-color: rgb(0, 207, 230);\n"
"padding: 12px;\n"
"color:rgb(10, 24, 25);")
        self.log_usernameField = QLineEdit(self.groupBox)
        self.log_usernameField.setObjectName(u"log_usernameField")
        self.log_usernameField.setGeometry(QRect(30, 90, 341, 61))
        self.log_usernameField.setFont(font)
        self.log_usernameField.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border-width: 10px;\n"
"border-style: medium;\n"
"border-color: rgb(0, 207, 230);\n"
"padding: 12px;\n"
"color:rgb(10, 24, 25);")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 50, 81, 21))
        font1 = QFont()
        font1.setFamilies([u"Baloo Chettan 2"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: #00cbbc")
        self.log_cancel = QPushButton(self.groupBox)
        self.log_cancel.setObjectName(u"log_cancel")
        self.log_cancel.setGeometry(QRect(80, 260, 111, 41))
        font2 = QFont()
        font2.setFamilies([u"Baloo Chettan 2"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.log_cancel.setFont(font2)
        self.log_cancel.setStyleSheet(u"background-color: #00dacc;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.log_cancel.setFlat(False)
        self.log_ok = QPushButton(self.groupBox)
        self.log_ok.setObjectName(u"log_ok")
        self.log_ok.setGeometry(QRect(210, 260, 111, 41))
        self.log_ok.setFont(font2)
        self.log_ok.setStyleSheet(u"background-color: #00dacc;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.log_ok.setFlat(False)

        self.retranslateUi(loginDialog)

        self.log_cancel.setDefault(False)
        self.log_ok.setDefault(False)


        QMetaObject.connectSlotsByName(loginDialog)
    # setupUi

    def retranslateUi(self, loginDialog):
        loginDialog.setWindowTitle(QCoreApplication.translate("loginDialog", u"Dialog", None))
        self.groupBox.setTitle("")
        self.log_passwordField.setPlaceholderText(QCoreApplication.translate("loginDialog", u"Password", None))
        self.log_usernameField.setPlaceholderText(QCoreApplication.translate("loginDialog", u"Username", None))
        self.label.setText(QCoreApplication.translate("loginDialog", u"Login", None))
        self.log_cancel.setText(QCoreApplication.translate("loginDialog", u"Cancel", None))
        self.log_ok.setText(QCoreApplication.translate("loginDialog", u"OK", None))
    # retranslateUi

