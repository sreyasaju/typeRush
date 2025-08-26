# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
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

class Ui_settings(object):
    def setupUi(self, settings):
        if not settings.objectName():
            settings.setObjectName(u"settings")
        settings.resize(420, 350)
        settings.setMinimumSize(QSize(420, 350))
        settings.setMaximumSize(QSize(420, 350))
        settings.setStyleSheet(u"background-color: #e2fbff;\n"
"border-radius: 30px;\n"
"\n"
"QMessageBox {\n"
"    color: rgb(11, 68, 77);\n"
"    font-size: 14px;\n"
"}\n"
"")
        self.groupBox = QGroupBox(settings)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 420, 350))
        self.groupBox.setMinimumSize(QSize(420, 350))
        self.groupBox.setMaximumSize(QSize(420, 350))
        self.durationField = QLineEdit(self.groupBox)
        self.durationField.setObjectName(u"durationField")
        self.durationField.setGeometry(QRect(60, 150, 291, 61))
        font = QFont()
        font.setFamilies([u"Baloo Chettan 2"])
        font.setPointSize(16)
        self.durationField.setFont(font)
        self.durationField.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;\n"
"border-width: 10px;\n"
"border-style: medium;\n"
"border-color: rgb(0, 207, 230);\n"
"padding: 12px;\n"
"color:rgb(10, 24, 25);")
        self.durationField.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.durationField.setMaxLength(12)
        self.setting_title = QLabel(self.groupBox)
        self.setting_title.setObjectName(u"setting_title")
        self.setting_title.setGeometry(QRect(170, 70, 81, 21))
        font1 = QFont()
        font1.setFamilies([u"Baloo Chettan 2"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.setting_title.setFont(font1)
        self.setting_title.setStyleSheet(u"color: #00cbbc")
        self.settings_cancelbutton = QPushButton(self.groupBox)
        self.settings_cancelbutton.setObjectName(u"settings_cancelbutton")
        self.settings_cancelbutton.setGeometry(QRect(80, 250, 111, 41))
        font2 = QFont()
        font2.setFamilies([u"Baloo Chettan 2"])
        font2.setPointSize(18)
        font2.setBold(True)
        self.settings_cancelbutton.setFont(font2)
        self.settings_cancelbutton.setStyleSheet(u"background-color: #00dacc;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.settings_cancelbutton.setFlat(False)
        self.settings_readybutton = QPushButton(self.groupBox)
        self.settings_readybutton.setObjectName(u"settings_readybutton")
        self.settings_readybutton.setGeometry(QRect(220, 250, 111, 41))
        self.settings_readybutton.setFont(font2)
        self.settings_readybutton.setStyleSheet(u"background-color: #00dacc;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.settings_readybutton.setFlat(False)
        self.settings_instruction = QLabel(self.groupBox)
        self.settings_instruction.setObjectName(u"settings_instruction")
        self.settings_instruction.setGeometry(QRect(40, 110, 361, 21))
        self.settings_instruction.setFont(font2)
        self.settings_instruction.setStyleSheet(u"color: rgb(0, 145, 134)")

        self.retranslateUi(settings)

        self.settings_cancelbutton.setDefault(False)
        self.settings_readybutton.setDefault(False)


        QMetaObject.connectSlotsByName(settings)
    # setupUi

    def retranslateUi(self, settings):
        settings.setWindowTitle(QCoreApplication.translate("settings", u"Settings", None))
        self.groupBox.setTitle("")
        self.durationField.setPlaceholderText(QCoreApplication.translate("settings", u"60", None))
        self.setting_title.setText(QCoreApplication.translate("settings", u"Settings", None))
        self.settings_cancelbutton.setText(QCoreApplication.translate("settings", u"Cancel", None))
        self.settings_readybutton.setText(QCoreApplication.translate("settings", u"Ready!", None))
        self.settings_instruction.setText(QCoreApplication.translate("settings", u"Enter the duration of the test in seconds!", None))
    # retranslateUi

