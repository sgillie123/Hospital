# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Welcome.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(900, 620)
        Dialog.setStyleSheet(u"background-color: rgb(226, 241, 255);")
        self.titleLabel = QLabel(Dialog)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(0, 80, 900, 70))
        self.titleLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 26pt; font-weight: bold;")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subtitleLabel = QLabel(Dialog)
        self.subtitleLabel.setObjectName(u"subtitleLabel")
        self.subtitleLabel.setGeometry(QRect(0, 162, 900, 28))
        self.subtitleLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 12pt;")
        self.subtitleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.PatientButton = QPushButton(Dialog)
        self.PatientButton.setObjectName(u"PatientButton")
        self.PatientButton.setGeometry(QRect(300, 215, 300, 50))
        self.PatientButton.setStyleSheet(u"background-color: rgb(57, 60, 255); color: white; font-size: 13pt; border-radius: 5px;")
        self.DoctorButton = QPushButton(Dialog)
        self.DoctorButton.setObjectName(u"DoctorButton")
        self.DoctorButton.setGeometry(QRect(300, 285, 300, 50))
        self.DoctorButton.setStyleSheet(u"background-color: rgb(57, 60, 255); color: white; font-size: 13pt; border-radius: 5px;")
        self.StaffButton = QPushButton(Dialog)
        self.StaffButton.setObjectName(u"StaffButton")
        self.StaffButton.setGeometry(QRect(300, 355, 300, 50))
        self.StaffButton.setStyleSheet(u"background-color: rgb(57, 60, 255); color: white; font-size: 13pt; border-radius: 5px;")
        self.orLabel = QLabel(Dialog)
        self.orLabel.setObjectName(u"orLabel")
        self.orLabel.setGeometry(QRect(0, 428, 900, 24))
        self.orLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 11pt;")
        self.orLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.CreateAccountButton = QPushButton(Dialog)
        self.CreateAccountButton.setObjectName(u"CreateAccountButton")
        self.CreateAccountButton.setGeometry(QRect(330, 462, 240, 46))
        self.CreateAccountButton.setStyleSheet(u"background-color: white; color: rgb(57, 60, 255); font-size: 13pt; border-radius: 5px; border: 2px solid rgb(57, 60, 255);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Hospital System", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"Dont Drop Dead", None))
        self.subtitleLabel.setText(QCoreApplication.translate("Dialog", u"Welcome! Please select who you are to continue.", None))
        self.PatientButton.setText(QCoreApplication.translate("Dialog", u"I am a Patient", None))
        self.DoctorButton.setText(QCoreApplication.translate("Dialog", u"I am a Doctor", None))
        self.StaffButton.setText(QCoreApplication.translate("Dialog", u"I am Staff / Receptionist", None))
        self.orLabel.setText(QCoreApplication.translate("Dialog", u"\u2014 New here? \u2014", None))
        self.CreateAccountButton.setText(QCoreApplication.translate("Dialog", u"Create Account", None))
    # retranslateUi

