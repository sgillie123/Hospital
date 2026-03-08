# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StaffDashboard.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCalendarWidget, QComboBox,
    QDateEdit, QDialog, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1200, 700)
        Dialog.setStyleSheet(u"background-color: rgb(226, 241, 255);")
        self.titleLabel = QLabel(Dialog)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(0, 20, 1000, 51))
        self.titleLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 20pt; font-weight: bold;")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.staffGreeting = QLabel(Dialog)
        self.staffGreeting.setObjectName(u"staffGreeting")
        self.staffGreeting.setGeometry(QRect(30, 80, 600, 26))
        self.staffGreeting.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 12pt;")
        self.LogoutButton = QPushButton(Dialog)
        self.LogoutButton.setObjectName(u"LogoutButton")
        self.LogoutButton.setGeometry(QRect(880, 80, 90, 32))
        self.LogoutButton.setStyleSheet(u"background-color: rgb(57, 60, 255); color: white; font-size: 10pt; border-radius: 4px;")
        self.regLabel = QLabel(Dialog)
        self.regLabel.setObjectName(u"regLabel")
        self.regLabel.setGeometry(QRect(30, 115, 300, 41))
        self.regLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 12pt; font-weight: bold;")
        self.lPatName = QLabel(Dialog)
        self.lPatName.setObjectName(u"lPatName")
        self.lPatName.setGeometry(QRect(30, 160, 101, 22))
        self.lPatName.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 11pt;")
        self.PatName = QLineEdit(Dialog)
        self.PatName.setObjectName(u"PatName")
        self.PatName.setGeometry(QRect(130, 157, 270, 34))
        self.PatName.setStyleSheet(u"font-size: 11pt; color: rgb(0,0,0); background-color: white;")
        self.lPatDOB = QLabel(Dialog)
        self.lPatDOB.setObjectName(u"lPatDOB")
        self.lPatDOB.setGeometry(QRect(400, 157, 131, 22))
        self.lPatDOB.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 11pt;")
        self.PatDOB = QDateEdit(Dialog)
        self.PatDOB.setObjectName(u"PatDOB")
        self.PatDOB.setGeometry(QRect(530, 157, 167, 32))
        self.PatDOB.setStyleSheet(u"font-size: 11pt; color: rgb(120, 120, 120); background-color: white; border-radius: 4px;")
        self.lPatGender = QLabel(Dialog)
        self.lPatGender.setObjectName(u"lPatGender")
        self.lPatGender.setGeometry(QRect(700, 160, 81, 22))
        self.lPatGender.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 11pt;")
        self.PatGender = QComboBox(Dialog)
        self.PatGender.addItem("")
        self.PatGender.addItem("")
        self.PatGender.addItem("")
        self.PatGender.setObjectName(u"PatGender")
        self.PatGender.setGeometry(QRect(780, 157, 100, 34))
        self.PatGender.setStyleSheet(u"font-size: 11pt; background-color: white; color: rgb(0,0,0);")
        self.lPatEmail = QLabel(Dialog)
        self.lPatEmail.setObjectName(u"lPatEmail")
        self.lPatEmail.setGeometry(QRect(30, 205, 90, 22))
        self.lPatEmail.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 11pt;")
        self.PatEmail = QLineEdit(Dialog)
        self.PatEmail.setObjectName(u"PatEmail")
        self.PatEmail.setGeometry(QRect(125, 202, 270, 34))
        self.PatEmail.setStyleSheet(u"font-size: 11pt; color: rgb(0,0,0); background-color: white;")
        self.lPatPhone = QLabel(Dialog)
        self.lPatPhone.setObjectName(u"lPatPhone")
        self.lPatPhone.setGeometry(QRect(415, 205, 90, 22))
        self.lPatPhone.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 11pt;")
        self.PatPhone = QLineEdit(Dialog)
        self.PatPhone.setObjectName(u"PatPhone")
        self.PatPhone.setGeometry(QRect(515, 202, 355, 34))
        self.PatPhone.setStyleSheet(u"font-size: 11pt; color: rgb(0,0,0); background-color: white;")
        self.lBloodType = QLabel(Dialog)
        self.lBloodType.setObjectName(u"lBloodType")
        self.lBloodType.setGeometry(QRect(30, 250, 111, 21))
        self.lBloodType.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 11pt;")
        self.BloodType = QComboBox(Dialog)
        self.BloodType.addItem("")
        self.BloodType.addItem("")
        self.BloodType.addItem("")
        self.BloodType.addItem("")
        self.BloodType.addItem("")
        self.BloodType.addItem("")
        self.BloodType.addItem("")
        self.BloodType.addItem("")
        self.BloodType.addItem("")
        self.BloodType.setObjectName(u"BloodType")
        self.BloodType.setGeometry(QRect(150, 247, 101, 34))
        self.BloodType.setStyleSheet(u"font-size: 11pt; background-color: white; color: rgb(0,0,0);")
        self.lEmergContact = QLabel(Dialog)
        self.lEmergContact.setObjectName(u"lEmergContact")
        self.lEmergContact.setGeometry(QRect(260, 247, 201, 31))
        self.lEmergContact.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 11pt;")
        self.EmergContact = QLineEdit(Dialog)
        self.EmergContact.setObjectName(u"EmergContact")
        self.EmergContact.setGeometry(QRect(459, 247, 411, 34))
        self.EmergContact.setStyleSheet(u"font-size: 11pt; color: rgb(0,0,0); background-color: white;")
        self.RegisterPatientButton = QPushButton(Dialog)
        self.RegisterPatientButton.setObjectName(u"RegisterPatientButton")
        self.RegisterPatientButton.setGeometry(QRect(380, 295, 240, 45))
        self.RegisterPatientButton.setStyleSheet(u"background-color: rgb(57, 60, 255); color: white; font-size: 13pt; border-radius: 5px;")
        self.calendarGroup = QGroupBox(Dialog)
        self.calendarGroup.setObjectName(u"calendarGroup")
        self.calendarGroup.setGeometry(QRect(30, 350, 400, 300))
        self.calendarGroup.setStyleSheet(u"\n"
"     QGroupBox {\n"
"      font-size: 12pt;\n"
"      font-weight: bold;\n"
"      color: rgb(57, 60, 255);\n"
"      border: 2px solid rgb(57, 60, 255);\n"
"      border-radius: 8px;\n"
"      margin-top: 10px;\n"
"      padding-top: 10px;\n"
"      background-color: white;\n"
"     }\n"
"     QGroupBox::title {\n"
"      subcontrol-origin: margin;\n"
"      left: 10px;\n"
"      padding: 0 5px 0 5px;\n"
"     }\n"
"    ")
        self.calendarLayout = QVBoxLayout(self.calendarGroup)
        self.calendarLayout.setObjectName(u"calendarLayout")
        self.staffCalendar = QCalendarWidget(self.calendarGroup)
        self.staffCalendar.setObjectName(u"staffCalendar")
        self.staffCalendar.setStyleSheet(u"        QCalendarWidget {\n"
"         background-color: white;\n"
"         border-radius: 5px;\n"
"        }\n"
"        QCalendarWidget QToolButton {\n"
"         color: rgb(57, 60, 255);\n"
"         font-size: 10pt;\n"
"         font-weight: bold;\n"
"        }\n"
"        QCalendarWidget QMenu {\n"
"         width: 150px;\n"
"         color: white;\n"
"         background-color: rgb(57, 60, 255);\n"
"        }\n"
"        QCalendarWidget QSpinBox {\n"
"         width: 100px;\n"
"         font-size: 10pt;\n"
"         color: rgb(57, 60, 255);\n"
"         background-color: white;\n"
"        }\n"
"        QCalendarWidget QTableView {\n"
"         background-color: white;\n"
"         selection-background-color: rgb(57, 60, 255);\n"
"         selection-color: white;\n"
"        }\n"
"        QCalendarWidget QAbstractItemView:enabled {\n"
"         color: rgb(0, 0, 0);\n"
"         background-color: white;\n"
"         selection-background-color: rgb(57, 60, 255);\n"
"         selection-color: white;\n"
"  "
                        "      }\n"
"        QCalendarWidget QWidget#qt_calendar_navigationbar {\n"
"         background-color: rgb(57, 60, 255);\n"
"        }\n"
"        QCalendarWidget QToolButton {\n"
"         color: white;\n"
"         background-color: transparent;\n"
"         font-size: 11pt;\n"
"         font-weight: bold;\n"
"        }\n"
"       ")
        self.staffCalendar.setGridVisible(True)

        self.calendarLayout.addWidget(self.staffCalendar)

        self.statsLabel = QLabel(self.calendarGroup)
        self.statsLabel.setObjectName(u"statsLabel")
        self.statsLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 10pt; padding: 8px; background-color: #f0f6ff; border-radius: 4px;")
        self.statsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.statsLabel.setWordWrap(True)

        self.calendarLayout.addWidget(self.statsLabel)

        self.listLabel = QLabel(Dialog)
        self.listLabel.setObjectName(u"listLabel")
        self.listLabel.setGeometry(QRect(450, 350, 241, 24))
        self.listLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 12pt; font-weight: bold;")
        self.SearchPatient = QLineEdit(Dialog)
        self.SearchPatient.setObjectName(u"SearchPatient")
        self.SearchPatient.setGeometry(QRect(700, 350, 270, 32))
        self.SearchPatient.setStyleSheet(u"font-size: 11pt; color: rgb(0,0,0); background-color: white; border-radius: 4px;")
        self.PatientsTable = QTableWidget(Dialog)
        if (self.PatientsTable.columnCount() < 6):
            self.PatientsTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.PatientsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.PatientsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.PatientsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.PatientsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.PatientsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.PatientsTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.PatientsTable.setObjectName(u"PatientsTable")
        self.PatientsTable.setGeometry(QRect(450, 390, 520, 260))
        self.PatientsTable.setStyleSheet(u"background-color: white; font-size: 10pt; color: rgb(0,0,0);")
        self.PatientsTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.PatientsTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.PatientsTable.setRowCount(0)
        self.PatientsTable.setColumnCount(6)
        self.PatientsTable.horizontalHeader().setStretchLastSection(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Staff Portal", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"Staff / Receptionist Portal", None))
        self.staffGreeting.setText(QCoreApplication.translate("Dialog", u"Welcome, Staff Member", None))
        self.LogoutButton.setText(QCoreApplication.translate("Dialog", u"Logout", None))
        self.regLabel.setText(QCoreApplication.translate("Dialog", u"Register New Patient", None))
        self.lPatName.setText(QCoreApplication.translate("Dialog", u"Full Name *", None))
        self.lPatDOB.setText(QCoreApplication.translate("Dialog", u"Date of Birth *", None))
        self.lPatGender.setText(QCoreApplication.translate("Dialog", u"Gender", None))
        self.PatGender.setItemText(0, QCoreApplication.translate("Dialog", u"Male", None))
        self.PatGender.setItemText(1, QCoreApplication.translate("Dialog", u"Female", None))
        self.PatGender.setItemText(2, QCoreApplication.translate("Dialog", u"Other", None))

        self.lPatEmail.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.lPatPhone.setText(QCoreApplication.translate("Dialog", u"Phone #", None))
        self.lBloodType.setText(QCoreApplication.translate("Dialog", u"Blood Type", None))
        self.BloodType.setItemText(0, QCoreApplication.translate("Dialog", u"A+", None))
        self.BloodType.setItemText(1, QCoreApplication.translate("Dialog", u"A-", None))
        self.BloodType.setItemText(2, QCoreApplication.translate("Dialog", u"B+", None))
        self.BloodType.setItemText(3, QCoreApplication.translate("Dialog", u"B-", None))
        self.BloodType.setItemText(4, QCoreApplication.translate("Dialog", u"AB+", None))
        self.BloodType.setItemText(5, QCoreApplication.translate("Dialog", u"AB-", None))
        self.BloodType.setItemText(6, QCoreApplication.translate("Dialog", u"O+", None))
        self.BloodType.setItemText(7, QCoreApplication.translate("Dialog", u"O-", None))
        self.BloodType.setItemText(8, QCoreApplication.translate("Dialog", u"Unknown", None))

        self.lEmergContact.setText(QCoreApplication.translate("Dialog", u"Emergency Contact", None))
        self.EmergContact.setPlaceholderText(QCoreApplication.translate("Dialog", u"Name \u2014 Phone", None))
        self.RegisterPatientButton.setText(QCoreApplication.translate("Dialog", u"Register Patient", None))
        self.calendarGroup.setTitle(QCoreApplication.translate("Dialog", u"Appointment Overview", None))
        self.statsLabel.setText(QCoreApplication.translate("Dialog", u"Click a date to see appointments", None))
        self.listLabel.setText(QCoreApplication.translate("Dialog", u"Registered Patients", None))
        self.SearchPatient.setPlaceholderText(QCoreApplication.translate("Dialog", u"\U0001f50d Search patients...", None))
        ___qtablewidgetitem = self.PatientsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"ID", None));
        ___qtablewidgetitem1 = self.PatientsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Name", None));
        ___qtablewidgetitem2 = self.PatientsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"DOB", None));
        ___qtablewidgetitem3 = self.PatientsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Phone", None));
        ___qtablewidgetitem4 = self.PatientsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Blood Type", None));
        ___qtablewidgetitem5 = self.PatientsTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Registered", None));
    # retranslateUi

