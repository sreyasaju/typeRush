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
    QSizePolicy, QTextEdit, QWidget)

class Ui_typingGame(object):
    def setupUi(self, typingGame):
        if not typingGame.objectName():
            typingGame.setObjectName(u"typingGame")
        typingGame.resize(850, 605)
        typingGame.setMaximumSize(QSize(850, 605))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(14)
        typingGame.setFont(font)
        typingGame.setStyleSheet(u"background-color: rgb(39, 43, 140);")
        typingGame.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        typingGame.setDocumentMode(True)
        typingGame.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(typingGame)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(850, 605))
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
        self.textfield.setGeometry(QRect(50, 340, 761, 171))
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
        self.sentencelabel.setGeometry(QRect(50, 120, 751, 191))
        font3 = QFont()
        font3.setFamilies([u"Baloo Chettan 2"])
        font3.setPointSize(32)
        font3.setBold(True)
        self.sentencelabel.setFont(font3)
        self.sentencelabel.setStyleSheet(u"color:rgb(0, 116, 132)")
        self.sentencelabel.setWordWrap(True)
        typingGame.setCentralWidget(self.centralwidget)

        self.retranslateUi(typingGame)

        QMetaObject.connectSlotsByName(typingGame)
    # setupUi

    def retranslateUi(self, typingGame):
        typingGame.setWindowTitle(QCoreApplication.translate("typingGame", u"typeRush", None))
#if QT_CONFIG(whatsthis)
        typingGame.setWhatsThis(QCoreApplication.translate("typingGame", u"<html><head/><body><p>harmonize</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.timer.setText(QCoreApplication.translate("typingGame", u"60", None))
        self.textfield.setPlaceholderText(QCoreApplication.translate("typingGame", u"Start typing!", None))
        self.sentencelabel.setText(QCoreApplication.translate("typingGame", u"Fetching the sentences.....", None))
    # retranslateUi

