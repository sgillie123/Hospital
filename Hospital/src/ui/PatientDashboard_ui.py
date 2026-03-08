# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PatientDashboard.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCalendarWidget, QDialog,
    QGroupBox, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1000, 700)
        Dialog.setStyleSheet(u"background-color: rgb(226, 241, 255);")
        self.titleLabel = QLabel(Dialog)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(0, 20, 1000, 50))
        self.titleLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 24pt; font-weight: bold;")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.patientNameLabel = QLabel(Dialog)
        self.patientNameLabel.setObjectName(u"patientNameLabel")
        self.patientNameLabel.setGeometry(QRect(30, 80, 700, 30))
        self.patientNameLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 16pt; font-weight: bold;")
        self.patientInfoLabel = QLabel(Dialog)
        self.patientInfoLabel.setObjectName(u"patientInfoLabel")
        self.patientInfoLabel.setGeometry(QRect(30, 110, 700, 25))
        self.patientInfoLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 11pt;")
        self.BookAppointmentButton = QPushButton(Dialog)
        self.BookAppointmentButton.setObjectName(u"BookAppointmentButton")
        self.BookAppointmentButton.setGeometry(QRect(800, 85, 170, 45))
        self.BookAppointmentButton.setStyleSheet(u"background-color: rgb(57, 60, 255); color: white; font-size: 12pt; font-weight: bold; border-radius: 8px;")
        self.LogoutButton = QPushButton(Dialog)
        self.LogoutButton.setObjectName(u"LogoutButton")
        self.LogoutButton.setGeometry(QRect(30, 650, 100, 35))
        self.LogoutButton.setStyleSheet(u"background-color: rgb(57, 60, 255); color: white; font-size: 11pt; border-radius: 6px;")
        self.calendarGroup = QGroupBox(Dialog)
        self.calendarGroup.setObjectName(u"calendarGroup")
        self.calendarGroup.setGeometry(QRect(30, 150, 400, 260))
        self.calendarGroup.setStyleSheet(u"\n"
"     QGroupBox {\n"
"      font-size: 14pt;\n"
"      font-weight: bold;\n"
"      color: rgb(57, 60, 255);\n"
"      border: 2px solid rgb(57, 60, 255);\n"
"      border-radius: 10px;\n"
"      margin-top: 15px;\n"
"      padding-top: 15px;\n"
"      background-color: white;\n"
"     }\n"
"     QGroupBox::title {\n"
"      subcontrol-origin: margin;\n"
"      left: 15px;\n"
"      padding: 0 10px 0 10px;\n"
"     }\n"
"    ")
        self.calendarLayout = QVBoxLayout(self.calendarGroup)
        self.calendarLayout.setObjectName(u"calendarLayout")
        self.patientCalendar = QCalendarWidget(self.calendarGroup)
        self.patientCalendar.setObjectName(u"patientCalendar")
        self.patientCalendar.setStyleSheet(u"        QCalendarWidget {\n"
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
        self.patientCalendar.setGridVisible(True)
        self.patientCalendar.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)

        self.calendarLayout.addWidget(self.patientCalendar)

        self.apptLabel = QLabel(Dialog)
        self.apptLabel.setObjectName(u"apptLabel")
        self.apptLabel.setGeometry(QRect(450, 150, 520, 30))
        self.apptLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 16pt; font-weight: bold;")
        self.AppointmentsTable = QTableWidget(Dialog)
        if (self.AppointmentsTable.columnCount() < 5):
            self.AppointmentsTable.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.AppointmentsTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.AppointmentsTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.AppointmentsTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.AppointmentsTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.AppointmentsTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.AppointmentsTable.setObjectName(u"AppointmentsTable")
        self.AppointmentsTable.setGeometry(QRect(450, 185, 520, 225))
        self.AppointmentsTable.setStyleSheet(u"\n"
"     QTableWidget {\n"
"      background-color: white;\n"
"      font-size: 11pt;\n"
"      color: rgb(0,0,0);\n"
"      border: 2px solid rgb(57, 60, 255);\n"
"      border-radius: 8px;\n"
"      gridline-color: #e2e8f0;\n"
"     }\n"
"     QHeaderView::section {\n"
"      background-color: rgb(57, 60, 255);\n"
"      color: white;\n"
"      font-size: 11pt;\n"
"      font-weight: bold;\n"
"      padding: 8px;\n"
"      border: none;\n"
"     }\n"
"     QTableWidget::item {\n"
"      padding: 5px;\n"
"      border-bottom: 1px solid #e2e8f0;\n"
"     }\n"
"    ")
        self.AppointmentsTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.AppointmentsTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.AppointmentsTable.setRowCount(0)
        self.AppointmentsTable.setColumnCount(5)
        self.AppointmentsTable.horizontalHeader().setMinimumSectionSize(80)
        self.AppointmentsTable.horizontalHeader().setStretchLastSection(True)
        self.recordsLabel = QLabel(Dialog)
        self.recordsLabel.setObjectName(u"recordsLabel")
        self.recordsLabel.setGeometry(QRect(30, 430, 940, 30))
        self.recordsLabel.setStyleSheet(u"color: rgb(57, 60, 255); font-size: 16pt; font-weight: bold;")
        self.RecordsTable = QTableWidget(Dialog)
        if (self.RecordsTable.columnCount() < 4):
            self.RecordsTable.setColumnCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.RecordsTable.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.RecordsTable.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.RecordsTable.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.RecordsTable.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        self.RecordsTable.setObjectName(u"RecordsTable")
        self.RecordsTable.setGeometry(QRect(30, 465, 940, 170))
        self.RecordsTable.setStyleSheet(u"\n"
"     QTableWidget {\n"
"      background-color: white;\n"
"      font-size: 11pt;\n"
"      color: rgb(0,0,0);\n"
"      border: 2px solid rgb(57, 60, 255);\n"
"      border-radius: 8px;\n"
"      gridline-color: #e2e8f0;\n"
"     }\n"
"     QHeaderView::section {\n"
"      background-color: rgb(57, 60, 255);\n"
"      color: white;\n"
"      font-size: 11pt;\n"
"      font-weight: bold;\n"
"      padding: 8px;\n"
"      border: none;\n"
"     }\n"
"     QTableWidget::item {\n"
"      padding: 5px;\n"
"      border-bottom: 1px solid #e2e8f0;\n"
"     }\n"
"    ")
        self.RecordsTable.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.RecordsTable.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.RecordsTable.setRowCount(0)
        self.RecordsTable.setColumnCount(4)
        self.RecordsTable.horizontalHeader().setStretchLastSection(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Patient Portal", None))
        self.titleLabel.setText(QCoreApplication.translate("Dialog", u"Patient Portal", None))
        self.patientNameLabel.setText(QCoreApplication.translate("Dialog", u"Welcome, Patient Name", None))
        self.patientInfoLabel.setText(QCoreApplication.translate("Dialog", u"email@email.com  |  DOB: 01/01/1990", None))
        self.BookAppointmentButton.setText(QCoreApplication.translate("Dialog", u"+ Book Appointment", None))
        self.LogoutButton.setText(QCoreApplication.translate("Dialog", u"Logout", None))
        self.calendarGroup.setTitle(QCoreApplication.translate("Dialog", u"Calendar", None))
        self.apptLabel.setText(QCoreApplication.translate("Dialog", u"My Appointments", None))
        ___qtablewidgetitem = self.AppointmentsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Date", None));
        ___qtablewidgetitem1 = self.AppointmentsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Time", None));
        ___qtablewidgetitem2 = self.AppointmentsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Doctor", None));
        ___qtablewidgetitem3 = self.AppointmentsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Reason", None));
        ___qtablewidgetitem4 = self.AppointmentsTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Status", None));
        self.recordsLabel.setText(QCoreApplication.translate("Dialog", u"Medical Records", None))
        ___qtablewidgetitem5 = self.RecordsTable.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Date", None));
        ___qtablewidgetitem6 = self.RecordsTable.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"Doctor", None));
        ___qtablewidgetitem7 = self.RecordsTable.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"Diagnosis", None));
        ___qtablewidgetitem8 = self.RecordsTable.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dialog", u"Notes", None));
    # retranslateUi

