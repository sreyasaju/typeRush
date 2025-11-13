# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'typinggame.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_typingGame(object):
    def setupUi(self, typingGame):
        if not typingGame.objectName():
            typingGame.setObjectName(u"typingGame")
        typingGame.resize(850, 605)
        typingGame.setMaximumSize(QSize(850, 605))
        palette = QPalette()
        typingGame.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Baloo Chettan 2"])
        font.setPointSize(18)
        typingGame.setFont(font)
        typingGame.setStyleSheet(u"")
        typingGame.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        typingGame.setDocumentMode(True)
        typingGame.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(typingGame)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(850, 605))
        palette1 = QPalette()
        self.centralwidget.setPalette(palette1)
        self.centralwidget.setFont(font)
        self.settings = QGroupBox(self.centralwidget)
        self.settings.setObjectName(u"settings")
        self.settings.setEnabled(True)
        self.settings.setGeometry(QRect(-10, 0, 881, 605))
        self.settings.setMinimumSize(QSize(850, 605))
        self.settings.setStyleSheet(u"background-color: #e2fbff;\n"
"border-radius: 10px")
        self.settings.setAlignment(Qt.AlignmentFlag.AlignJustify|Qt.AlignmentFlag.AlignVCenter)
        self.timer = QLabel(self.settings)
        self.timer.setObjectName(u"timer")
        self.timer.setEnabled(False)
        self.timer.setGeometry(QRect(330, 50, 181, 61))
        font1 = QFont()
        font1.setFamilies([u"Baloo Chettan 2"])
        font1.setPointSize(36)
        font1.setBold(True)
        self.timer.setFont(font1)
        self.timer.setStyleSheet(u"color:rgb(0, 116, 132);\n"
"background-color: rgb(199, 235, 241);\n"
"border-radius: 30px;")
        self.timer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.timer.setWordWrap(True)
        self.textfield = QTextEdit(self.settings)
        self.textfield.setObjectName(u"textfield")
        self.textfield.setGeometry(QRect(50, 320, 761, 171))
        font2 = QFont()
        font2.setFamilies([u"Baloo Chettan 2"])
        font2.setPointSize(30)
        font2.setBold(True)
        self.textfield.setFont(font2)
        self.textfield.setStyleSheet(u"color:rgb(135, 175, 181);\n"
"background-color: rgb(232, 252, 255)")
        self.textfield.setInputMethodHints(Qt.InputMethodHint.ImhMultiLine|Qt.InputMethodHint.ImhNoPredictiveText)
        self.textfield.setLineWidth(7)
        self.textfield.setMidLineWidth(7)
        self.sentencelabel = QLabel(self.settings)
        self.sentencelabel.setObjectName(u"sentencelabel")
        self.sentencelabel.setGeometry(QRect(50, 120, 761, 191))
        font3 = QFont()
        font3.setFamilies([u"Baloo Chettan 2"])
        font3.setPointSize(32)
        font3.setBold(True)
        self.sentencelabel.setFont(font3)
        self.sentencelabel.setStyleSheet(u"color:rgb(0, 116, 132)")
        self.sentencelabel.setWordWrap(True)
        self.restartbutton = QPushButton(self.settings)
        self.restartbutton.setObjectName(u"restartbutton")
        self.restartbutton.setGeometry(QRect(460, 520, 131, 41))
        font4 = QFont()
        font4.setFamilies([u"Baloo Chettan 2"])
        font4.setPointSize(18)
        font4.setBold(True)
        self.restartbutton.setFont(font4)
        self.restartbutton.setStyleSheet(u"background-color: #00dacc;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.restartbutton.setFlat(False)
        self.homebutton = QPushButton(self.settings)
        self.homebutton.setObjectName(u"homebutton")
        self.homebutton.setGeometry(QRect(280, 520, 111, 41))
        self.homebutton.setFont(font4)
        self.homebutton.setStyleSheet(u"background-color: #00dacc;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.homebutton.setFlat(False)
        typingGame.setCentralWidget(self.centralwidget)

        self.retranslateUi(typingGame)

        self.restartbutton.setDefault(False)
        self.homebutton.setDefault(False)


        QMetaObject.connectSlotsByName(typingGame)
    # setupUi

    def retranslateUi(self, typingGame):
        typingGame.setWindowTitle(QCoreApplication.translate("typingGame", u"typeRush", None))
#if QT_CONFIG(whatsthis)
        typingGame.setWhatsThis(QCoreApplication.translate("typingGame", u"<html><head/><body><p>harmonize</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.timer.setText("")
        self.textfield.setPlaceholderText(QCoreApplication.translate("typingGame", u"Start typing!", None))
        self.sentencelabel.setText(QCoreApplication.translate("typingGame", u"Fetching the sentences.....", None))
        self.restartbutton.setText(QCoreApplication.translate("typingGame", u"Start over!", None))
        self.homebutton.setText(QCoreApplication.translate("typingGame", u"Home", None))
    # retranslateUi

