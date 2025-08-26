# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'progress.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_progresswindow(object):
    def setupUi(self, progresswindow):
        if not progresswindow.objectName():
            progresswindow.setObjectName(u"progresswindow")
        progresswindow.resize(850, 605)
        progresswindow.setMaximumSize(QSize(850, 605))
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        font.setPointSize(14)
        progresswindow.setFont(font)
        progresswindow.setStyleSheet(u"background-color: rgb(39, 43, 140);")
        progresswindow.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))
        progresswindow.setDocumentMode(True)
        progresswindow.setUnifiedTitleAndToolBarOnMac(True)
        self.centralwidget = QWidget(progresswindow)
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
        self.settings_2 = QGroupBox(self.settings)
        self.settings_2.setObjectName(u"settings_2")
        self.settings_2.setGeometry(QRect(50, 80, 315, 362))
        self.settings_2.setMinimumSize(QSize(315, 362))
        self.settings_2.setStyleSheet(u"background-color: rgb(205, 235, 239);\n"
"border-radius: 10px")
        self.record_parameter_groupBox = QGroupBox(self.settings_2)
        self.record_parameter_groupBox.setObjectName(u"record_parameter_groupBox")
        self.record_parameter_groupBox.setGeometry(QRect(30, 50, 251, 291))
        self.wpm_label = QLabel(self.record_parameter_groupBox)
        self.wpm_label.setObjectName(u"wpm_label")
        self.wpm_label.setGeometry(QRect(0, 50, 121, 41))
        font1 = QFont()
        font1.setFamilies([u"Baloo Chettan 2"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.wpm_label.setFont(font1)
        self.wpm_label.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color:#00dacc")
        self.wpm_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.wpm_label.setMargin(10)
        self.recent_stats_label = QLabel(self.record_parameter_groupBox)
        self.recent_stats_label.setObjectName(u"recent_stats_label")
        self.recent_stats_label.setGeometry(QRect(0, 10, 251, 21))
        font2 = QFont()
        font2.setFamilies([u"Baloo Chettan 2"])
        font2.setPointSize(24)
        font2.setBold(True)
        self.recent_stats_label.setFont(font2)
        self.recent_stats_label.setStyleSheet(u"color: rgb(0, 135, 126);")
        self.accuracy_label = QLabel(self.record_parameter_groupBox)
        self.accuracy_label.setObjectName(u"accuracy_label")
        self.accuracy_label.setGeometry(QRect(0, 110, 131, 41))
        self.accuracy_label.setFont(font1)
        self.accuracy_label.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color:#00dacc")
        self.accuracy_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.accuracy_label.setMargin(10)
        self.nchars_label = QLabel(self.record_parameter_groupBox)
        self.nchars_label.setObjectName(u"nchars_label")
        self.nchars_label.setGeometry(QRect(0, 170, 121, 41))
        self.nchars_label.setFont(font1)
        self.nchars_label.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color:#00dacc")
        self.nchars_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.nchars_label.setMargin(10)
        self.timestamp_label = QLabel(self.record_parameter_groupBox)
        self.timestamp_label.setObjectName(u"timestamp_label")
        self.timestamp_label.setGeometry(QRect(0, 230, 121, 61))
        self.timestamp_label.setFont(font1)
        self.timestamp_label.setStyleSheet(u"border-radius:5px;\n"
"color: rgb(255, 255, 255);\n"
"background-color:#00dacc")
        self.timestamp_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.timestamp_label.setMargin(10)
        self.wpm_field = QLabel(self.record_parameter_groupBox)
        self.wpm_field.setObjectName(u"wpm_field")
        self.wpm_field.setGeometry(QRect(110, 50, 141, 41))
        font3 = QFont()
        font3.setFamilies([u"Baloo Chettan 2"])
        font3.setPointSize(18)
        font3.setBold(False)
        self.wpm_field.setFont(font3)
        self.wpm_field.setStyleSheet(u"border-radius:8px;\n"
"border: 5px solid #00dacc;\n"
"color: rgb(56, 157, 150)\n"
"")
        self.wpm_field.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.wpm_field.setMargin(5)
        self.accuracy_field = QLabel(self.record_parameter_groupBox)
        self.accuracy_field.setObjectName(u"accuracy_field")
        self.accuracy_field.setGeometry(QRect(110, 110, 141, 41))
        self.accuracy_field.setFont(font3)
        self.accuracy_field.setStyleSheet(u"border-radius:8px;\n"
"border: 5px solid #00dacc;\n"
"color: rgb(56, 157, 150)")
        self.accuracy_field.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.accuracy_field.setMargin(5)
        self.nchar_field = QLabel(self.record_parameter_groupBox)
        self.nchar_field.setObjectName(u"nchar_field")
        self.nchar_field.setGeometry(QRect(110, 170, 141, 41))
        font4 = QFont()
        font4.setFamilies([u"Baloo Chettan 2"])
        font4.setPointSize(17)
        font4.setBold(False)
        font4.setKerning(True)
        self.nchar_field.setFont(font4)
        self.nchar_field.setStyleSheet(u"border-radius:8px;\n"
"border: 5px solid #00dacc;\n"
"color: rgb(56, 157, 150)")
        self.nchar_field.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.nchar_field.setMargin(5)
        self.timestamp_field = QLabel(self.record_parameter_groupBox)
        self.timestamp_field.setObjectName(u"timestamp_field")
        self.timestamp_field.setGeometry(QRect(110, 230, 141, 61))
        self.timestamp_field.setFont(font3)
        self.timestamp_field.setStyleSheet(u"border-radius:8px;\n"
"border: 5px solid #00dacc;\n"
"color: rgb(56, 157, 150)")
        self.timestamp_field.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.timestamp_field.setWordWrap(True)
        self.timestamp_field.setMargin(5)
        self.accuracy_label.raise_()
        self.wpm_label.raise_()
        self.recent_stats_label.raise_()
        self.nchars_label.raise_()
        self.timestamp_label.raise_()
        self.wpm_field.raise_()
        self.accuracy_field.raise_()
        self.nchar_field.raise_()
        self.timestamp_field.raise_()
        self.plotframe = QFrame(self.settings)
        self.plotframe.setObjectName(u"plotframe")
        self.plotframe.setGeometry(QRect(390, 70, 441, 381))
        self.plotframe.setMinimumSize(QSize(400, 210))
        self.plotframe.setStyleSheet(u"background-color: rgb(214, 245, 249)")
        self.plotframe.setFrameShape(QFrame.Shape.NoFrame)
        self.plotframe.setFrameShadow(QFrame.Shadow.Raised)
        self.homebutton = QPushButton(self.settings)
        self.homebutton.setObjectName(u"homebutton")
        self.homebutton.setGeometry(QRect(350, 500, 111, 41))
        self.homebutton.setFont(font1)
        self.homebutton.setStyleSheet(u"background-color: #00dacc;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"")
        self.homebutton.setFlat(False)
        progresswindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(progresswindow)

        self.homebutton.setDefault(False)


        QMetaObject.connectSlotsByName(progresswindow)
    # setupUi

    def retranslateUi(self, progresswindow):
        progresswindow.setWindowTitle(QCoreApplication.translate("progresswindow", u"typeRush", None))
#if QT_CONFIG(whatsthis)
        progresswindow.setWhatsThis(QCoreApplication.translate("progresswindow", u"<html><head/><body><p>harmonize</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.wpm_label.setText(QCoreApplication.translate("progresswindow", u"WPM", None))
        self.recent_stats_label.setText(QCoreApplication.translate("progresswindow", u"Recent stats", None))
        self.accuracy_label.setText(QCoreApplication.translate("progresswindow", u"Accuracy", None))
        self.nchars_label.setText(QCoreApplication.translate("progresswindow", u"No. of chars.", None))
        self.timestamp_label.setText(QCoreApplication.translate("progresswindow", u"Timestamp", None))
        self.wpm_field.setText("")
        self.accuracy_field.setText("")
        self.nchar_field.setText("")
        self.timestamp_field.setText("")
        self.homebutton.setText(QCoreApplication.translate("progresswindow", u"Home", None))
    # retranslateUi

