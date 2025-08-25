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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGroupBox, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_registerDialog(object):
    def setupUi(self, registerDialog):
        if not registerDialog.objectName():
            registerDialog.setObjectName(u"registerDialog")
        registerDialog.resize(420, 350)
        registerDialog.setMinimumSize(QSize(420, 350))
        registerDialog.setMaximumSize(QSize(420, 350))
        registerDialog.setStyleSheet(u"background-color: #e2fbff;\n"
"border-radius: 30px")
        self.groupBox = QGroupBox(registerDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 420, 350))
        self.groupBox.setMinimumSize(QSize(420, 350))
        self.groupBox.setMaximumSize(QSize(420, 350))
        self.reg_passwordField = QLineEdit(self.groupBox)
        self.reg_passwordField.setObjectName(u"reg_passwordField")
        self.reg_passwordField.setGeometry(QRect(30, 160, 341, 61))
        font = QFont()
        font.setFamilies([u"Baloo Chettan 2"])
        font.setPointSize(16)
        self.reg_passwordField.setFont(font)
        self.reg_passwordField.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border-width: 10px;\n"
"border-style: medium;\n"
"border-color: rgb(0, 207, 230);\n"
"padding: 12px;\n"
"color:rgb(10, 24, 25);")
        self.reg_pass_usernameField = QLineEdit(self.groupBox)
        self.reg_pass_usernameField.setObjectName(u"reg_pass_usernameField")
        self.reg_pass_usernameField.setGeometry(QRect(30, 90, 341, 61))
        self.reg_pass_usernameField.setFont(font)
        self.reg_pass_usernameField.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border-width: 10px;\n"
"border-style: medium;\n"
"border-color: rgb(0, 207, 230);\n"
"padding: 12px;\n"
"color:rgb(10, 24, 25);")
        self.reg_pass_usernameField.setReadOnly(False)
        self.regr_cancelok = QDialogButtonBox(self.groupBox)
        self.regr_cancelok.setObjectName(u"regr_cancelok")
        self.regr_cancelok.setGeometry(QRect(10, 240, 361, 61))
        font1 = QFont()
        font1.setFamilies([u"Baloo Chettan 2"])
        font1.setPointSize(18)
        font1.setWeight(QFont.ExtraBold)
        self.regr_cancelok.setFont(font1)
        self.regr_cancelok.setStyleSheet(u"background-color: #00dacc;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"padding: 15px;\n"
"")
        self.regr_cancelok.setOrientation(Qt.Orientation.Horizontal)
        self.regr_cancelok.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.regr_cancelok.setCenterButtons(False)
        self.reg_label = QLabel(self.groupBox)
        self.reg_label.setObjectName(u"reg_label")
        self.reg_label.setGeometry(QRect(40, 50, 81, 21))
        font2 = QFont()
        font2.setFamilies([u"Baloo Chettan 2"])
        font2.setPointSize(20)
        font2.setBold(True)
        self.reg_label.setFont(font2)
        self.reg_label.setStyleSheet(u"color: #00cbbc")

        self.retranslateUi(registerDialog)

        QMetaObject.connectSlotsByName(registerDialog)
    # setupUi

    def retranslateUi(self, registerDialog):
        registerDialog.setWindowTitle(QCoreApplication.translate("registerDialog", u"Register", None))
        self.groupBox.setTitle("")
        self.reg_passwordField.setPlaceholderText(QCoreApplication.translate("registerDialog", u"Password", None))
        self.reg_pass_usernameField.setPlaceholderText(QCoreApplication.translate("registerDialog", u"Username", None))
        self.reg_label.setText(QCoreApplication.translate("registerDialog", u"Register", None))
    # retranslateUi

