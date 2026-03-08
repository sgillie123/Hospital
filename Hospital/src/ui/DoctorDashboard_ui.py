# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DoctorDashboard.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCalendarWidget, QDateEdit,
    QDialog, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1200, 700)
        Dialog.setStyleSheet(u"background-color: rgb(226, 241, 255);")
        self.titleLabel = QLabel(Dialog)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(0, 20, 1000, 40))
        self.titleLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 20pt; font-weight: bold;")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.docGreeting = QLabel(Dialog)
        self.docGreeting.setObjectName(u"docGreeting")
        self.docGreeting.setGeometry(QRect(30, 70, 600, 31))
        self.docGreeting.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 12pt;")
        self.docSub = QLabel(Dialog)
        self.docSub.setObjectName(u"docSub")
        self.docSub.setGeometry(QRect(30, 100, 600, 31))
        self.docSub.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 10pt;")
        self.LogoutButton = QPushButton(Dialog)
        self.LogoutButton.setObjectName(u"LogoutButton")
        self.LogoutButton.setGeometry(QRect(880, 78, 90, 32))
        self.LogoutButton.setStyleSheet(u"background-color: rgb(57, 60, 255); color: white; font-size: 10pt; border-radius: 4px;")
        self.calendarGroup = QGroupBox(Dialog)
        self.calendarGroup.setObjectName(u"calendarGroup")
        self.calendarGroup.setGeometry(QRect(30, 140, 400, 280))
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
        self.doctorCalendar = QCalendarWidget(self.calendarGroup)
        self.doctorCalendar.setObjectName(u"doctorCalendar")
        self.doctorCalendar.setStyleSheet(u"        QCalendarWidget {\n"
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
        self.doctorCalendar.setMinimumDate(QDate(2024, 1, 1))
        self.doctorCalendar.setGridVisible(True)

        self.calendarLayout.addWidget(self.doctorCalendar)

        self.apptCountLabel = QLabel(self.calendarGroup)
        self.apptCountLabel.setObjectName(u"apptCountLabel")
        self.apptCountLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 10pt; padding: 5px; background-color: #f0f6ff; border-radius: 4px;")
        self.apptCountLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.calendarLayout.addWidget(self.apptCountLabel)

        self.apptLabel = QLabel(Dialog)
        self.apptLabel.setObjectName(u"apptLabel")
        self.apptLabel.setGeometry(QRect(450, 140, 401, 31))
        self.apptLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 12pt; font-weight: bold;")
        self.AppointmentsTable = QTableWidget(Dialog)
        if (self.AppointmentsTable.columnCount() < 4):
            self.AppointmentsTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.AppointmentsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.AppointmentsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.AppointmentsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.AppointmentsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.AppointmentsTable.setObjectName(u"AppointmentsTable")
        self.AppointmentsTable.setGeometry(QRect(450, 175, 591, 245))
        self.AppointmentsTable.setStyleSheet(u"background-color: white; font-size: 10pt; color: rgb(0,0,0);")
        self.AppointmentsTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.AppointmentsTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.AppointmentsTable.setRowCount(0)
        self.AppointmentsTable.setColumnCount(4)
        self.AppointmentsTable.horizontalHeader().setStretchLastSection(True)
        self.diagLabel = QLabel(Dialog)
        self.diagLabel.setObjectName(u"diagLabel")
        self.diagLabel.setGeometry(QRect(30, 430, 300, 31))
        self.diagLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 12pt; font-weight: bold;")
        self.lPatient = QLabel(Dialog)
        self.lPatient.setObjectName(u"lPatient")
        self.lPatient.setGeometry(QRect(30, 470, 151, 22))
        self.lPatient.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 11pt;")
        self.DiagPatientID = QLineEdit(Dialog)
        self.DiagPatientID.setObjectName(u"DiagPatientID")
        self.DiagPatientID.setGeometry(QRect(180, 467, 300, 35))
        self.DiagPatientID.setStyleSheet(u"font-size: 11pt; color: rgb(0,0,0); background-color: white;")
        self.lDiagDate = QLabel(Dialog)
        self.lDiagDate.setObjectName(u"lDiagDate")
        self.lDiagDate.setGeometry(QRect(500, 470, 60, 22))
        self.lDiagDate.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 11pt;")
        self.DiagDate = QDateEdit(Dialog)
        self.DiagDate.setObjectName(u"DiagDate")
        self.DiagDate.setGeometry(QRect(570, 467, 167, 32))
        self.DiagDate.setStyleSheet(u"font-size: 11pt; color: rgb(120, 120, 120); background-color: white; border-radius: 4px;")
        self.lDiagnosis = QLabel(Dialog)
        self.lDiagnosis.setObjectName(u"lDiagnosis")
        self.lDiagnosis.setGeometry(QRect(30, 515, 130, 22))
        self.lDiagnosis.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 11pt;")
        self.DiagnosisField = QLineEdit(Dialog)
        self.DiagnosisField.setObjectName(u"DiagnosisField")
        self.DiagnosisField.setGeometry(QRect(170, 512, 700, 35))
        self.DiagnosisField.setStyleSheet(u"font-size: 11pt; color: rgb(0,0,0); background-color: white;")
        self.lNotes = QLabel(Dialog)
        self.lNotes.setObjectName(u"lNotes")
        self.lNotes.setGeometry(QRect(30, 560, 130, 22))
        self.lNotes.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 11pt;")
        self.NotesField = QLineEdit(Dialog)
        self.NotesField.setObjectName(u"NotesField")
        self.NotesField.setGeometry(QRect(170, 557, 700, 35))
        self.NotesField.setStyleSheet(u"font-size: 11pt; color: rgb(0,0,0); background-color: white;")
        self.SaveDiagButton = QPushButton(Dialog)
        self.SaveDiagButton.setObjectName(u"SaveDiagButton")
        self.SaveDiagButton.setGeometry(QRect(380, 610, 240, 45))
        self.SaveDiagButton.setStyleSheet(u"background-color: rgb(57, 60, 255); color: white; font-size: 13pt; border-radius: 5px;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Doctor Portal", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"Doctor Portal", None))
        self.docGreeting.setText(QCoreApplication.translate("Dialog", u"Good Morning, Dr. Smith", None))
        self.docSub.setText(QCoreApplication.translate("Dialog", u"You have 0 appointments today", None))
        self.LogoutButton.setText(QCoreApplication.translate("Dialog", u"Logout", None))
        self.calendarGroup.setTitle(QCoreApplication.translate("Dialog", u"Appointment Calendar", None))
        self.apptCountLabel.setText(QCoreApplication.translate("Dialog", u"Select a date to view appointments", None))
        self.apptLabel.setText(QCoreApplication.translate("Dialog", u"Appointments for Selected Date", None))
        ___qtablewidgetitem = self.AppointmentsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Time", None));
        ___qtablewidgetitem1 = self.AppointmentsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Patient", None));
        ___qtablewidgetitem2 = self.AppointmentsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Reason", None));
        ___qtablewidgetitem3 = self.AppointmentsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Status", None));
        self.diagLabel.setText(QCoreApplication.translate("Dialog", u"Add Patient Diagnosis", None))
        self.lPatient.setText(QCoreApplication.translate("Dialog", u"Patient Name *", None))
        self.DiagPatientID.setPlaceholderText(QCoreApplication.translate("Dialog", u"Patient name...", None))
        self.lDiagDate.setText(QCoreApplication.translate("Dialog", u"Date *", None))
        self.lDiagnosis.setText(QCoreApplication.translate("Dialog", u"Diagnosis *", None))
        self.DiagnosisField.setPlaceholderText(QCoreApplication.translate("Dialog", u"Enter diagnosis...", None))
        self.lNotes.setText(QCoreApplication.translate("Dialog", u"Notes / Rx", None))
        self.NotesField.setPlaceholderText(QCoreApplication.translate("Dialog", u"Prescription, notes, follow-up...", None))
        self.SaveDiagButton.setText(QCoreApplication.translate("Dialog", u"Save Diagnosis", None))
    # retranslateUi

