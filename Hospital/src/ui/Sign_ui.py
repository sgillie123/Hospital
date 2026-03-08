# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sign.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(900, 720)
        Dialog.setStyleSheet(u"background-color: rgb(226, 241, 255);")
        self.BackButton = QPushButton(Dialog)
        self.BackButton.setObjectName(u"BackButton")
        self.BackButton.setGeometry(QRect(30, 20, 90, 32))
        self.BackButton.setStyleSheet(u"background-color: rgb(57, 60, 255); color: white; font-size: 10pt; border-radius: 4px;")
        self.titleLabel = QLabel(Dialog)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(0, 60, 900, 50))
        self.titleLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 28pt; font-weight: bold;")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loginLink = QLabel(Dialog)
        self.loginLink.setObjectName(u"loginLink")
        self.loginLink.setGeometry(QRect(0, 110, 900, 30))
        self.loginLink.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 11pt;")
        self.loginLink.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.loginLink.setOpenExternalLinks(False)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(100, 160, 700, 25))
        self.label_3.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 12pt; font-weight: bold;")
        self.Name = QLineEdit(Dialog)
        self.Name.setObjectName(u"Name")
        self.Name.setGeometry(QRect(100, 185, 700, 40))
        self.Name.setStyleSheet(u"font-size: 12pt; color: rgb(0,0,0); background-color: white; border-radius: 8px; padding-left: 15px;")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(100, 235, 700, 25))
        self.label_5.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 12pt; font-weight: bold;")
        self.Username = QLineEdit(Dialog)
        self.Username.setObjectName(u"Username")
        self.Username.setGeometry(QRect(100, 260, 700, 40))
        self.Username.setStyleSheet(u"font-size: 12pt; color: rgb(0,0,0); background-color: white; border-radius: 8px; padding-left: 15px;")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(100, 310, 700, 25))
        self.label_4.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 12pt; font-weight: bold;")
        self.Email = QLineEdit(Dialog)
        self.Email.setObjectName(u"Email")
        self.Email.setGeometry(QRect(100, 335, 700, 40))
        self.Email.setStyleSheet(u"font-size: 12pt; color: rgb(0,0,0); background-color: white; border-radius: 8px; padding-left: 15px;")
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(100, 385, 700, 25))
        self.label_6.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 12pt; font-weight: bold;")
        self.Password = QLineEdit(Dialog)
        self.Password.setObjectName(u"Password")
        self.Password.setGeometry(QRect(100, 410, 700, 40))
        self.Password.setStyleSheet(u"font-size: 12pt; color: rgb(0,0,0); background-color: white; border-radius: 8px; padding-left: 15px;")
        self.Password.setEchoMode(QLineEdit.EchoMode.Password)
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 460, 340, 25))
        self.label_7.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 12pt; font-weight: bold;")
        self.DOB = QDateEdit(Dialog)
        self.DOB.setObjectName(u"DOB")
        self.DOB.setGeometry(QRect(100, 485, 340, 40))
        self.DOB.setStyleSheet(u"font-size: 12pt; color: rgb(0,0,0); background-color: white; border-radius: 8px; padding-left: 15px;")
        self.DOB.setCalendarPopup(True)
        self.labelRole = QLabel(Dialog)
        self.labelRole.setObjectName(u"labelRole")
        self.labelRole.setGeometry(QRect(460, 460, 340, 25))
        self.labelRole.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 12pt; font-weight: bold;")
        self.RoleCombo = QComboBox(Dialog)
        self.RoleCombo.addItem("")
        self.RoleCombo.addItem("")
        self.RoleCombo.addItem("")
        self.RoleCombo.setObjectName(u"RoleCombo")
        self.RoleCombo.setGeometry(QRect(460, 485, 340, 40))
        self.RoleCombo.setStyleSheet(u"font-size: 12pt; background-color: white; color: rgb(0,0,0); border-radius: 8px; padding-left: 15px;")
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(100, 535, 700, 25))
        self.label_8.setVisible(False)
        self.label_8.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 12pt; font-weight: bold;")
        self.EmployeeID = QLineEdit(Dialog)
        self.EmployeeID.setObjectName(u"EmployeeID")
        self.EmployeeID.setGeometry(QRect(100, 560, 700, 40))
        self.EmployeeID.setVisible(False)
        self.EmployeeID.setStyleSheet(u"font-size: 12pt; color: rgb(0,0,0); background-color: white; border-radius: 8px; padding-left: 15px;")
        self.errorLabel = QLabel(Dialog)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setGeometry(QRect(100, 595, 700, 25))
        self.errorLabel.setStyleSheet(u"color: #dc2626; font-size: 11pt;")
        self.errorLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.CreateButton = QPushButton(Dialog)
        self.CreateButton.setObjectName(u"CreateButton")
        self.CreateButton.setGeometry(QRect(300, 635, 300, 50))
        self.CreateButton.setStyleSheet(u"background-color: rgb(57, 60, 255); color: white; font-size: 14pt; font-weight: bold; border-radius: 8px;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Create Account", None))
        self.BackButton.setText(QCoreApplication.translate("Dialog", u"\u2190 Back", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"Create Account", None))
        self.loginLink.setText(QCoreApplication.translate("Dialog", u"Already have an account? <a href='login' style='color:rgb(57,60,255);'>Login here</a>", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Full Name *", None))
        self.Name.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter your full name", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Username *", None))
        self.Username.setPlaceholderText(QCoreApplication.translate("Dialog", u"Choose a username", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Email *", None))
        self.Email.setPlaceholderText(QCoreApplication.translate("Dialog", u"email@example.com", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Password *", None))
        self.Password.setPlaceholderText(QCoreApplication.translate("Dialog", u"Minimum 6 characters", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Date of Birth *", None))
        self.DOB.setDisplayFormat(QCoreApplication.translate("Dialog", u"dd/MM/yyyy", None))
        self.labelRole.setText(QCoreApplication.translate("Dialog", u"Account Type *", None))
        self.RoleCombo.setItemText(0, QCoreApplication.translate("Dialog", u"Patient", None))
        self.RoleCombo.setItemText(1, QCoreApplication.translate("Dialog", u"Doctor", None))
        self.RoleCombo.setItemText(2, QCoreApplication.translate("Dialog", u"Staff / Receptionist", None))

        self.label_8.setText(QCoreApplication.translate("Dialog", u"Employee ID (required for staff/doctors)", None))
        self.EmployeeID.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter your employee ID", None))
        self.errorLabel.setText("")
        self.CreateButton.setText(QCoreApplication.translate("Dialog", u"Create Account", None))
    # retranslateUi

