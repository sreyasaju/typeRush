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
    QLabel, QLineEdit, QMainWindow, QSizePolicy,
    QWidget)

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
        self.record_parameter_groupBox = QGroupBox(self.settings)
        self.record_parameter_groupBox.setObjectName(u"record_parameter_groupBox")
        self.record_parameter_groupBox.setGeometry(QRect(30, 50, 251, 121))
        self.save_voice_label = QLabel(self.record_parameter_groupBox)
        self.save_voice_label.setObjectName(u"save_voice_label")
        self.save_voice_label.setGeometry(QRect(0, 50, 121, 41))
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        font1.setPointSize(15)
        self.save_voice_label.setFont(font1)
        self.save_voice_label.setStyleSheet(u"border-radius:5px;\n"
"background-color: #45259b")
        self.save_voice_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.save_voice_label.setMargin(10)
        self.save_voice_field = QLineEdit(self.record_parameter_groupBox)
        self.save_voice_field.setObjectName(u"save_voice_field")
        self.save_voice_field.setGeometry(QRect(110, 50, 141, 41))
        self.save_voice_field.setFont(font1)
        self.save_voice_field.setStyleSheet(u"border: 3px solid #45259b;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.record_parameters_header = QLabel(self.record_parameter_groupBox)
        self.record_parameters_header.setObjectName(u"record_parameters_header")
        self.record_parameters_header.setGeometry(QRect(0, 10, 251, 21))
        font2 = QFont()
        font2.setFamilies([u"Ubuntu"])
        font2.setPointSize(16)
        font2.setBold(True)
        self.record_parameters_header.setFont(font2)
        self.record_parameters_header.setStyleSheet(u"color: rgb(56, 59, 94)")
        self.midi_parameters_groupBox = QGroupBox(self.settings)
        self.midi_parameters_groupBox.setObjectName(u"midi_parameters_groupBox")
        self.midi_parameters_groupBox.setGeometry(QRect(40, 180, 271, 81))
        self.midi_header = QLabel(self.midi_parameters_groupBox)
        self.midi_header.setObjectName(u"midi_header")
        self.midi_header.setGeometry(QRect(0, 0, 251, 21))
        self.midi_header.setFont(font2)
        self.midi_header.setStyleSheet(u"color: rgb(56, 59, 94)")
        self.save_midi_label = QLabel(self.midi_parameters_groupBox)
        self.save_midi_label.setObjectName(u"save_midi_label")
        self.save_midi_label.setGeometry(QRect(0, 30, 131, 41))
        self.save_midi_label.setFont(font1)
        self.save_midi_label.setStyleSheet(u"border-radius:5px;\n"
"background-color: #45259b")
        self.save_midi_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.save_midi_label.setMargin(10)
        self.save_midi_field = QLineEdit(self.midi_parameters_groupBox)
        self.save_midi_field.setObjectName(u"save_midi_field")
        self.save_midi_field.setGeometry(QRect(110, 30, 141, 41))
        self.save_midi_field.setFont(font1)
        self.save_midi_field.setStyleSheet(u"border: 3px solid #45259b;\n"
"border-radius: 5px;\n"
"\n"
"")
        self.save_midi_field.setFrame(True)
        self.save_midi_field.setClearButtonEnabled(False)
        self.midi_parameters_groupBox.raise_()
        self.record_parameter_groupBox.raise_()
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(-10, 10, 341, 581))

        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"typeRush", None))
#if QT_CONFIG(whatsthis)
        MainWindow.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>harmonize</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.save_voice_label.setText(QCoreApplication.translate("MainWindow", u"Save Voice As:", None))
#if QT_CONFIG(tooltip)
        self.save_voice_field.setToolTip(QCoreApplication.translate("MainWindow", u"Enter the filename to save your voice recording, don't forget the extension! e.g., voice.wav", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.save_voice_field.setStatusTip(QCoreApplication.translate("MainWindow", u"Enter filename to save recording, with \".wav\" extension", None))
#endif // QT_CONFIG(statustip)
        self.save_voice_field.setText("")
        self.save_voice_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"voice.wav", None))
        self.record_parameters_header.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.midi_header.setText(QCoreApplication.translate("MainWindow", u"Register: ", None))
        self.save_midi_label.setText(QCoreApplication.translate("MainWindow", u"Save MIDI As:", None))
#if QT_CONFIG(tooltip)
        self.save_midi_field.setToolTip(QCoreApplication.translate("MainWindow", u"Enter the filename to save the MIDI output, and don't forget the extension! e.g., output.midi", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.save_midi_field.setStatusTip(QCoreApplication.translate("MainWindow", u"Enter filename to save the midi file, with \".midi\" extension", None))
#endif // QT_CONFIG(statustip)
        self.save_midi_field.setText("")
        self.save_midi_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"output.midi", None))
    # retranslateUi

