# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(900, 620)
        Dialog.setStyleSheet(u"background-color: rgb(226, 241, 255);")
        self.BackButton = QPushButton(Dialog)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setGeometry(QRect(30, 20, 90, 32))
        self.BackButton.setStyleSheet(u"background-color: rgb(57, 60, 255); color: white; font-size: 10pt; border-radius: 4px;")
        self.titleLabel = QLabel(Dialog)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(0, 80, 900, 50))
        self.titleLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 28pt; font-weight: bold;")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.roleDisplayLabel = QLabel(Dialog)
        self.roleDisplayLabel.setObjectName(u"roleDisplayLabel")
        self.roleDisplayLabel.setGeometry(QRect(0, 140, 900, 30))
        self.roleDisplayLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 16pt;")
        self.roleDisplayLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.signupLink = QLabel(Dialog)
        self.signupLink.setObjectName(u"signupLink")
        self.signupLink.setGeometry(QRect(0, 175, 900, 30))
        self.signupLink.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 11pt;")
        self.signupLink.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.signupLink.setOpenExternalLinks(False)
        self.lUsername = QLabel(Dialog)
        self.lUsername.setObjectName(u"lUsername")
        self.lUsername.setGeometry(QRect(100, 240, 700, 25))
        self.lUsername.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 12pt; font-weight: bold;")
        self.Username = QLineEdit(Dialog)
        self.Username.setObjectName(u"Username")
        self.Username.setGeometry(QRect(100, 265, 700, 45))
        self.Username.setStyleSheet(u"font-size: 12pt; color: rgb(0,0,0); background-color: white; border-radius: 8px; padding-left: 15px;")
        self.lPassword = QLabel(Dialog)
        self.lPassword.setObjectName(u"lPassword")
        self.lPassword.setGeometry(QRect(100, 330, 700, 25))
        self.lPassword.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 12pt; font-weight: bold;")
        self.Password = QLineEdit(Dialog)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(100, 355, 700, 45))
        self.Password.setStyleSheet(u"font-size: 12pt; color: rgb(0,0,0); background-color: white; border-radius: 8px; padding-left: 15px;")
        self.Password.setEchoMode(QLineEdit.EchoMode.Password)
        self.lEmployeeID = QLabel(Dialog)
        self.lEmployeeID.setObjectName(u"lEmployeeID")
        self.lEmployeeID.setGeometry(QRect(100, 420, 700, 25))
        self.lEmployeeID.setVisible(False)
        self.lEmployeeID.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 12pt; font-weight: bold;")
        self.EmployeeID = QLineEdit(Dialog)
        self.EmployeeID.setObjectName(u"EmployeeID")
        self.EmployeeID.setGeometry(QRect(100, 445, 700, 45))
        self.EmployeeID.setVisible(False)
        self.EmployeeID.setStyleSheet(u"font-size: 12pt; color: rgb(0,0,0); background-color: white; border-radius: 8px; padding-left: 15px;")
        self.errorLabel = QLabel(Dialog)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setGeometry(QRect(100, 505, 700, 25))
        self.errorLabel.setStyleSheet(u"color: #dc2626; font-size: 11pt;")
        self.errorLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.LoginButton = QPushButton(Dialog)
        self.LoginButton.setObjectName(u"LoginButton")
        self.LoginButton.setGeometry(QRect(300, 550, 300, 50))
        self.LoginButton.setStyleSheet(u"background-color: rgb(57, 60, 255); color: white; font-size: 14pt; font-weight: bold; border-radius: 8px;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Login", None))
        self.BackButton.setText(QCoreApplication.translate("Dialog", u"\u2190 Back", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"Login", None))
        self.roleDisplayLabel.setText(QCoreApplication.translate("Dialog", u"Patient Login", None))
        self.signupLink.setText(QCoreApplication.translate("Dialog", u"Don't have an account? <a href='signup' style='color:rgb(57,60,255);'>Create one</a>", None))
        self.lUsername.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.Username.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter your username", None))
        self.lPassword.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.Password.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter your password", None))
        self.lEmployeeID.setText(QCoreApplication.translate("Dialog", u"Employee ID", None))
        self.EmployeeID.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter your employee ID", None))
        self.errorLabel.setText("")
        self.LoginButton.setText(QCoreApplication.translate("Dialog", u"Login", None))
    # retranslateUi

