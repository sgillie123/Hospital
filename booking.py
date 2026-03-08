# booking popup dialog
# i made this as a separate file

from PyQt6 import QtCore
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel,
                              QComboBox, QPushButton, QTextEdit, QCalendarWidget, QMessageBox)
import data

# calender style i copied and edited
CAL_STYLE = """
QCalendarWidget QWidget#qt_calendar_navigationbar {
    background-color: rgb(57, 60, 255);
}
QCalendarWidget QToolButton {
    color: white;
    background-color: transparent;
    font-size: 11pt;
    font-weight: bold;
}
QCalendarWidget QTableView {
    background-color: white;
    selection-background-color: rgb(57, 60, 255);
    selection-color: white;
}
QCalendarWidget QAbstractItemView:enabled {
    color: rgb(0, 0, 0);
    background-color: white;
    selection-background-color: rgb(57, 60, 255);
    selection-color: white;
}
"""

# the booking popup window
class BookingDialog(QDialog):
    def __init__(self, parent, patient_name):
        super().__init__(parent)
        self._name = patient_name
        self.setWindowTitle("Book Appointment")
        self.setFixedSize(500, 560)
        # setting style for the dialog
        self.setStyleSheet("QDialog{background:#f0f6ff} QLabel{font-size:11pt;color:#374151} "
                           "QComboBox,QTextEdit{background:white;border:2px solid #e2e8f0;border-radius:8px;padding:6px;font-size:11pt}")
        L = QVBoxLayout(self)
        L.setSpacing(8)
        L.setContentsMargins(24, 20, 24, 20)
        # title label
        L.addWidget(QLabel("<b style='font-size:14pt;color:#1e293b'>Book Appointment</b>"))
        # doctor dropdown
        L.addWidget(QLabel("Doctor"))
        self.doctor = QComboBox()
        # get doctors from users
        self.doctor.addItems([f"{u['name']} — {u.get('specialty', 'General')}"
                               for u in data.users.values() if u["role"] == "Doctor"])
        L.addWidget(self.doctor)
        # making the calender widget
        L.addWidget(QLabel("Date"))
        self.cal = QCalendarWidget()
        self.cal.setGridVisible(True)
        # remove week numbers column
        self.cal.setVerticalHeaderFormat(QCalendarWidget.VerticalHeaderFormat.NoVerticalHeader)
        # show day names
        self.cal.setHorizontalHeaderFormat(QCalendarWidget.HorizontalHeaderFormat.ShortDayNames)
        self.cal.setMinimumDate(QtCore.QDate.currentDate())
        self.cal.setMaximumDate(QtCore.QDate.currentDate().addMonths(3))
        self.cal.setStyleSheet(CAL_STYLE)
        L.addWidget(self.cal)
        # time picker
        L.addWidget(QLabel("Time"))
        self.time = QComboBox()
        self.time.addItems(["09:00 AM", "09:30 AM", "10:00 AM", "10:30 AM", "11:00 AM",
                             "02:00 PM", "02:30 PM", "03:00 PM", "04:00 PM"])
        L.addWidget(self.time)
        # reason box
        L.addWidget(QLabel("Reason / Notes"))
        self.reason = QTextEdit()
        self.reason.setFixedHeight(55)
        self.reason.setPlaceholderText("Reason for visit...")
        L.addWidget(self.reason)
        # cancel and confirm buttons
        row = QHBoxLayout()
        cancel = QPushButton("Cancel")
        cancel.setStyleSheet("background:#e2e8f0;border-radius:8px;font-size:11pt;padding:8px")
        cancel.clicked.connect(self.reject)
        confirm = QPushButton("Confirm")
        confirm.setStyleSheet("background:#2563eb;color:white;border-radius:8px;font-size:11pt;font-weight:bold;padding:8px")
        confirm.clicked.connect(self._confirm)
        row.addWidget(cancel)
        row.addWidget(confirm)
        L.addLayout(row)

    def _confirm(self):
        # check doctor exists
        if not self.doctor.currentText():
            QMessageBox.warning(self, "Missing", "No doctor available."); return
        doc_name = self.doctor.currentText().split(" — ")[0]
        date = self.cal.selectedDate().toString("dd/MM/yyyy")
        time = self.time.currentText()
        notes = self.reason.toPlainText().strip() or "General consultation"
        # get patient id
        pid = next((p["id"] for p in data.patients if p["name"] == self._name), "")
        aid = f"A{len(data.appointments)+1:03d}"
        # add to appointments list
        data.appointments.append({
            "id": aid, "patient_id": pid, "patient": self._name,
            "doctor": doc_name, "date": date, "time": time,
            "reason": notes, "status": "Confirmed", "notes": notes
        })
        # make a bill for this appointment
        data.bills.append({
            "bill_id": f"B{len(data.bills)+1:03d}", "patient_id": pid,
            "appointment_id": aid, "amount_due": 0.0, "paid": False
        })
        QMessageBox.information(self, "Booked!", f"Confirmed with {doc_name}\n{date} at {time}.")
        self.accept()
