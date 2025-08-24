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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QLabel,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)

class Ui_typingGame(object):
    def setupUi(self, typingGame):
        if not typingGame.objectName():
            typingGame.setObjectName(u"typingGame")
        typingGame.resize(800, 600)
        self.centralwidget = QWidget(typingGame)
        self.centralwidget.setObjectName(u"centralwidget")
        self.settings = QGroupBox(self.centralwidget)
        self.settings.setObjectName(u"settings")
        self.settings.setEnabled(True)
        self.settings.setGeometry(QRect(0, 0, 801, 535))
        self.settings.setMinimumSize(QSize(455, 535))
        self.settings.setStyleSheet(u"background-color: #e2fbff;\n"
"border-radius: 30px")
        self.settings.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.label = QLabel(self.settings)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 80, 601, 201))
        font = QFont()
        font.setFamilies([u"Baloo Chettan 2"])
        font.setPointSize(36)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:rgb(0, 116, 132)")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)
        self.textEdit = QTextEdit(self.settings)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(70, 250, 641, 151))
        font1 = QFont()
        font1.setFamilies([u"Baloo Chettan 2"])
        font1.setPointSize(24)
        font1.setBold(True)
        self.textEdit.setFont(font1)
        self.textEdit.viewport().setProperty("cursor", QCursor(Qt.CursorShape.IBeamCursor))
        self.textEdit.setStyleSheet(u"color:rgb(114, 178, 187)")
        self.textEdit.setFrameShape(QFrame.Shape.HLine)
        self.textEdit.setFrameShadow(QFrame.Shadow.Raised)
        self.textEdit.setLineWidth(3)
        self.textEdit.setMidLineWidth(-1)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit.setAcceptRichText(False)
        typingGame.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(typingGame)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        typingGame.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(typingGame)
        self.statusbar.setObjectName(u"statusbar")
        typingGame.setStatusBar(self.statusbar)

        self.retranslateUi(typingGame)

        QMetaObject.connectSlotsByName(typingGame)
    # setupUi

    def retranslateUi(self, typingGame):
        typingGame.setWindowTitle(QCoreApplication.translate("typingGame", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("typingGame", u"Fetching the test sentences....", None))
        self.textEdit.setHtml(QCoreApplication.translate("typingGame", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Baloo Chettan 2'; font-size:24pt; font-weight:700; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Start typing here!</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("typingGame", u"Start typing here", None))
    # retranslateUi

