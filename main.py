import sys
from datetime import datetime
from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import (
    QDialog, QApplication, QStackedWidget, QTableWidgetItem,
    QMessageBox, QLabel, QComboBox,
    QDateEdit, QPushButton, QVBoxLayout, QHBoxLayout,
    QFrame, QTextEdit, QHeaderView
)
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi

# ─── In-memory data store ────────────────────────────────────────────────────
users = {
    "patient1":      {"password": "pass", "role": "Patient",  "name": "Alice Johnson",
                      "email": "alice@email.com", "dob": "15/03/1990", "phone": "555-1001"},
    "drsmith":       {"password": "pass", "role": "Doctor",   "name": "Dr. James Smith",
                      "email": "james@hospital.com", "dob": "10/05/1975", "employee_id": "DOC001"},
    "receptionist1": {"password": "pass", "role": "Staff / Receptionist",
                      "name": "Maria Lopez", "email": "maria@hospital.com",
                      "dob": "22/08/1985", "employee_id": "STF001"},
}

patients = [
    {"id": "P001", "name": "Alice Johnson", "dob": "15/03/1990", "phone": "555-1001",
     "blood": "A+", "gender": "Female", "email": "alice@email.com",
     "emergency": "Bob Johnson — 555-1002", "registered": "01/01/2024"},
    {"id": "P002", "name": "Carlos Rivera", "dob": "20/07/1985", "phone": "555-2002",
     "blood": "O+", "gender": "Male", "email": "carlos@email.com",
     "emergency": "Ana Rivera — 555-2003", "registered": "15/02/2024"},
]

appointments = [
    {"id": "A001", "patient": "Alice Johnson", "doctor": "Dr. Smith", "date": "07/03/2026",
     "time": "09:00 AM", "reason": "Annual Checkup", "status": "Confirmed"},
    {"id": "A002", "patient": "Carlos Rivera", "doctor": "Dr. Smith", "date": "07/03/2026",
     "time": "10:30 AM", "reason": "Follow-up", "status": "Confirmed"},
]

diagnoses = [
    {"patient": "Alice Johnson", "doctor": "Dr. Smith", "date": "01/02/2026",
     "diagnosis": "Seasonal Allergy", "notes": "Cetirizine 10mg once daily"},
]

current_user = None


# ─── Appointment Booking Popup ────────────────────────────────────────────────
class BookAppointmentDialog(QDialog):
    def __init__(self, parent=None, patient_name=""):
        super().__init__(parent)
        self.setWindowTitle("Book Appointment")
        self.setFixedSize(500, 440)
        self.setStyleSheet("""
            QDialog { background-color: #f0f6ff; }
            QLabel  { font-size: 11pt; color: #374151; }
            QComboBox, QDateEdit, QTextEdit {
                background: white; border: 2px solid #e2e8f0;
                border-radius: 8px; padding: 6px 10px; font-size: 11pt;
            }
            QComboBox:focus, QDateEdit:focus, QTextEdit:focus {
                border: 2px solid #2563eb;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setSpacing(12)
        layout.setContentsMargins(30, 24, 30, 24)

        title = QLabel("📅  Book New Appointment")
        title.setStyleSheet("font-size: 15pt; font-weight: bold; color: #1e293b;")
        layout.addWidget(title)

        layout.addWidget(QLabel("Select Doctor"))
        self.doctorCombo = QComboBox()
        self.doctorCombo.addItems([
            "Dr. Smith — General Practice",
            "Dr. Patel — Cardiology",
            "Dr. Lee — Orthopedics",
            "Dr. Nguyen — Dermatology"
        ])
        layout.addWidget(self.doctorCombo)

        layout.addWidget(QLabel("Appointment Date"))
        self.dateEdit = QDateEdit(QtCore.QDate.currentDate().addDays(1))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat("dd/MM/yyyy")
        layout.addWidget(self.dateEdit)

        layout.addWidget(QLabel("Appointment Time"))
        self.timeCombo = QComboBox()
        self.timeCombo.addItems([
            "09:00 AM", "09:30 AM", "10:00 AM", "10:30 AM",
            "11:00 AM", "11:30 AM", "02:00 PM", "02:30 PM",
            "03:00 PM", "03:30 PM", "04:00 PM"
        ])
        layout.addWidget(self.timeCombo)

        layout.addWidget(QLabel("Reason for Visit"))
        self.reasonEdit = QTextEdit()
        self.reasonEdit.setFixedHeight(70)
        self.reasonEdit.setPlaceholderText("Describe the reason for your visit...")
        layout.addWidget(self.reasonEdit)

        btnRow = QHBoxLayout()
        cancelBtn = QPushButton("Cancel")
        cancelBtn.setFixedHeight(44)
        cancelBtn.setStyleSheet("""
            QPushButton { background: #e2e8f0; color: #374151; border-radius: 8px; font-size: 11pt; }
            QPushButton:hover { background: #cbd5e1; }
        """)
        cancelBtn.clicked.connect(self.reject)

        bookBtn = QPushButton("Confirm Booking")
        bookBtn.setFixedHeight(44)
        bookBtn.setStyleSheet("""
            QPushButton { background: #2563eb; color: white; border-radius: 8px;
                          font-size: 11pt; font-weight: bold; }
            QPushButton:hover { background: #1d4ed8; }
        """)
        bookBtn.clicked.connect(self.confirm)
        btnRow.addWidget(cancelBtn)
        btnRow.addWidget(bookBtn)
        layout.addLayout(btnRow)

        self.patient_name = patient_name

    def confirm(self):
        doctor = self.doctorCombo.currentText().split(" — ")[0]
        date   = self.dateEdit.date().toString("dd/MM/yyyy")
        time   = self.timeCombo.currentText()
        reason = self.reasonEdit.toPlainText().strip() or "General consultation"

        appointments.append({
            "id": f"A{len(appointments)+1:03d}",
            "patient": self.patient_name,
            "doctor": doctor,
            "date": date,
            "time": time,
            "reason": reason,
            "status": "Confirmed"
        })
        QMessageBox.information(self, "Booked!",
                                f"Appointment confirmed with {doctor}\non {date} at {time}.")
        self.accept()


# ─── Welcome Screen ───────────────────────────────────────────────────────────
class WelcomeScreen(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Welcome.ui", self)
        self.PatientButton.clicked.connect(lambda: self._go(LOGIN, "Patient"))
        self.StaffButton.clicked.connect(lambda: self._go(LOGIN, "Staff / Receptionist"))
        self.DoctorButton.clicked.connect(lambda: self._go(LOGIN, "Doctor"))
        self.CreateAccountButton.clicked.connect(self._go_signup)

    def _go_signup(self):
        sign_screen.reset()
        widget.setCurrentIndex(SIGNUP)

    def _go(self, index, role):
        login_screen.RoleCombo.setCurrentText(role)
        widget.setCurrentIndex(index)


# ─── Sign Up Screen ───────────────────────────────────────────────────────────
class SignScreen(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Sign.ui", self)
        self.CreateButton.clicked.connect(self.create_account)
        self.BackButton.clicked.connect(lambda: widget.setCurrentIndex(WELCOME))
        self.loginLink.linkActivated.connect(lambda _: widget.setCurrentIndex(LOGIN))

    def create_account(self):
        name     = self.Name.text().strip()
        username = self.Username.text().strip()
        email    = self.Email.text().strip()
        password = self.Password.text()
        dob      = self.DOB.text().strip()
        emp_id   = self.EmployeeID.text().strip()
        role     = self.RoleCombo.currentText()

        if not all([name, username, email, password, dob]):
            self.errorLabel.setText("⚠  Please fill in all required fields.")
            return
        if len(password) < 6:
            self.errorLabel.setText("⚠  Password must be at least 6 characters.")
            return
        if username in users:
            self.errorLabel.setText("⚠  Username already taken.")
            return

        users[username] = {
            "password": password, "role": role, "name": name,
            "email": email, "dob": dob, "employee_id": emp_id
        }
        self.errorLabel.setStyleSheet("color: #16a34a;")
        self.errorLabel.setText("✅  Account created! Redirecting to login…")
        QtCore.QTimer.singleShot(1200, lambda: widget.setCurrentIndex(LOGIN))

    def reset(self):
        self.errorLabel.setText("")
        self.errorLabel.setStyleSheet("color: #dc2626;")
        for field in [self.Name, self.Username, self.Email, self.Password,
                      self.DOB, self.EmployeeID]:
            field.clear()


# ─── Login Screen ─────────────────────────────────────────────────────────────
class LoginScreen(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("Login.ui", self)
        self.LoginButton.clicked.connect(self.login)
        self.BackButton.clicked.connect(lambda: widget.setCurrentIndex(WELCOME))
        self.signupLink.linkActivated.connect(self._go_signup)
        self.RoleCombo.currentTextChanged.connect(self._on_role_changed)

    def _on_role_changed(self, role):
        is_staff = role in ("Doctor", "Staff / Receptionist")
        self.lEmployeeID.setVisible(is_staff)
        self.EmployeeID.setVisible(is_staff)
        if not is_staff:
            self.EmployeeID.clear()

    def _go_signup(self):
        sign_screen.reset()
        widget.setCurrentIndex(SIGNUP)

    def login(self):
        global current_user
        username = self.Username.text().strip()
        password = self.Password.text()
        role     = self.RoleCombo.currentText()

        if username not in users:
            self.errorLabel.setText("⚠  Username not found.")
            return
        u = users[username]
        if u["password"] != password:
            self.errorLabel.setText("⚠  Incorrect password.")
            return
        if u["role"] != role:
            self.errorLabel.setText(
                f"⚠  This account is registered as '{u['role']}', not '{role}'.")
            return

        # Validate employee ID for Doctor/Staff
        if role in ("Doctor", "Staff / Receptionist"):
            entered_id = self.EmployeeID.text().strip()
            if not entered_id:
                self.errorLabel.setText("⚠  Please enter your Employee ID.")
                return
            if u.get("employee_id", "") != entered_id:
                self.errorLabel.setText("⚠  Employee ID does not match.")
                return

        current_user = u
        self.errorLabel.setText("")
        if role == "Patient":
            patient_dashboard.load_patient(u)
            widget.setCurrentIndex(PATIENT)
        elif role == "Doctor":
            doctor_dashboard.load_doctor(u)
            widget.setCurrentIndex(DOCTOR)
        else:
            staff_dashboard.load_staff(u)
            widget.setCurrentIndex(STAFF)


# ─── Patient Dashboard ─────────────────────────────────────────────────────────
class PatientDashboard(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("PatientDashboard.ui", self)
        self.BookAppointmentButton.clicked.connect(self.book_appointment)
        self.LogoutButton.clicked.connect(self.logout)
        for tbl in [self.AppointmentsTable, self.RecordsTable]:
            tbl.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
            tbl.setAlternatingRowColors(True)

    def load_patient(self, user):
        self.patientNameLabel.setText(user["name"])
        self.patientInfoLabel.setText(
            f"{user.get('email','')}  •  DOB: {user.get('dob','')}  •  Patient Portal"
        )
        self._refresh_appointments(user["name"])
        self._refresh_records(user["name"])

    def _refresh_appointments(self, name):
        my_appts = [a for a in appointments if a["patient"] == name]
        tbl = self.AppointmentsTable
        tbl.setRowCount(len(my_appts))
        for r, a in enumerate(my_appts):
            for c, val in enumerate([a["date"], a["time"], a["doctor"], a["reason"], a["status"]]):
                item = QTableWidgetItem(val)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                if c == 4:
                    item.setForeground(
                        QtGui.QColor("#16a34a") if val == "Confirmed"
                        else QtGui.QColor("#d97706")
                    )
                tbl.setItem(r, c, item)

    def _refresh_records(self, name):
        my_diag = [d for d in diagnoses if d["patient"] == name]
        tbl = self.RecordsTable
        tbl.setRowCount(len(my_diag))
        for r, d in enumerate(my_diag):
            for c, val in enumerate([d["date"], d["doctor"], d["diagnosis"], d["notes"]]):
                item = QTableWidgetItem(val)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                tbl.setItem(r, c, item)

    def book_appointment(self):
        dlg = BookAppointmentDialog(self, current_user["name"])
        if dlg.exec() == QDialog.DialogCode.Accepted:
            self._refresh_appointments(current_user["name"])

    def logout(self):
        global current_user
        current_user = None
        widget.setCurrentIndex(WELCOME)


# ─── Doctor Dashboard ──────────────────────────────────────────────────────────
class DoctorDashboard(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("DoctorDashboard.ui", self)
        self.SaveDiagButton.clicked.connect(self.save_diagnosis)
        self.LogoutButton.clicked.connect(self.logout)
        self.AppointmentsTable.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)
        self.AppointmentsTable.setAlternatingRowColors(True)

    def load_doctor(self, user):
        hour = datetime.now().hour
        greeting = ("Good Morning" if hour < 12
                    else "Good Afternoon" if hour < 17
                    else "Good Evening")
        self.docGreeting.setText(f"{greeting}, {user['name']}")
        today = datetime.now().strftime("%d/%m/%Y")
        count = len([a for a in appointments if a["date"] == today])
        self.docSub.setText(f"You have {count} appointment(s) today  •  {today}")
        self._refresh_appointments(user["name"])
        self.DiagDate.setText(today)

    def _refresh_appointments(self, doctor_name):
        my_appts = [a for a in appointments
                    if a["doctor"] in doctor_name or doctor_name in a["doctor"]]
        tbl = self.AppointmentsTable
        tbl.setRowCount(len(my_appts))
        for r, a in enumerate(my_appts):
            for c, val in enumerate([a["time"], a["patient"], a["reason"], a["status"], "View"]):
                item = QTableWidgetItem(val)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                tbl.setItem(r, c, item)

    def save_diagnosis(self):
        patient = self.DiagPatientID.text().strip()
        date    = self.DiagDate.text().strip()
        diag    = self.DiagnosisField.text().strip()
        notes   = self.NotesField.text().strip()

        if not all([patient, date, diag]):
            QMessageBox.warning(self, "Missing Info",
                                "Please fill in Patient, Date, and Diagnosis.")
            return

        diagnoses.append({
            "patient": patient,
            "doctor": current_user["name"],
            "date": date,
            "diagnosis": diag,
            "notes": notes
        })
        QMessageBox.information(self, "Saved", f"Diagnosis saved for {patient}.")
        for f in [self.DiagPatientID, self.DiagnosisField, self.NotesField]:
            f.clear()

    def logout(self):
        global current_user
        current_user = None
        widget.setCurrentIndex(WELCOME)


# ─── Staff Dashboard ───────────────────────────────────────────────────────────
class StaffDashboard(QDialog):
    def __init__(self):
        super().__init__()
        loadUi("StaffDashboard.ui", self)
        self.RegisterPatientButton.clicked.connect(self.register_patient)
        self.LogoutButton.clicked.connect(self.logout)
        self.SearchPatient.textChanged.connect(self.filter_patients)
        self.PatientsTable.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)
        self.PatientsTable.setAlternatingRowColors(True)

    def load_staff(self, user):
        self.staffGreeting.setText(f"Welcome, {user['name']}")
        self._refresh_patients()

    def _refresh_patients(self, filter_text=""):
        ft = filter_text.lower()
        filtered = (
            [p for p in patients if ft in p["name"].lower() or ft in p["id"].lower()]
            if ft else patients
        )
        tbl = self.PatientsTable
        tbl.setRowCount(len(filtered))
        for r, p in enumerate(filtered):
            for c, val in enumerate(
                    [p["id"], p["name"], p["dob"], p["phone"], p["blood"], p["registered"]]):
                item = QTableWidgetItem(val)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                tbl.setItem(r, c, item)

    def filter_patients(self, text):
        self._refresh_patients(text)

    def register_patient(self):
        name   = self.PatName.text().strip()
        dob    = self.PatDOB.text().strip()
        gender = self.PatGender.currentText()
        email  = self.PatEmail.text().strip()
        phone  = self.PatPhone.text().strip()
        addr   = self.PatAddress.text().strip()
        blood  = self.BloodType.currentText()
        emerg  = self.EmergContact.text().strip()

        if not name or not dob:
            QMessageBox.warning(self, "Missing Info",
                                "Name and Date of Birth are required.")
            return

        new_id = f"P{len(patients)+1:03d}"
        today  = datetime.now().strftime("%d/%m/%Y")
        patients.append({
            "id": new_id, "name": name, "dob": dob, "gender": gender,
            "email": email, "phone": phone, "address": addr,
            "blood": blood, "emergency": emerg, "registered": today
        })

        username = name.lower().replace(" ", "") + new_id
        users[username] = {
            "password": dob.replace("/", ""),
            "role": "Patient", "name": name,
            "email": email, "dob": dob, "phone": phone
        }

        QMessageBox.information(
            self, "Patient Registered",
            f"Patient registered successfully!\n\n"
            f"Patient ID : {new_id}\n"
            f"Username   : {username}\n"
            f"Password   : {dob.replace('/', '')}  (date of birth digits)\n\n"
            "Please share these credentials with the patient."
        )
        for f in [self.PatName, self.PatDOB, self.PatEmail,
                  self.PatPhone, self.PatAddress, self.EmergContact]:
            f.clear()
        self._refresh_patients()

    def logout(self):
        global current_user
        current_user = None
        widget.setCurrentIndex(WELCOME)


# ─── App bootstrap ─────────────────────────────────────────────────────────────
app = QApplication(sys.argv)
app.setFont(QtGui.QFont("Segoe UI", 10))

widget = QStackedWidget()
widget.setFixedSize(900, 620)
widget.setWindowTitle("MediCare — Hospital Management System")

WELCOME = 0
LOGIN   = 1
SIGNUP  = 2
PATIENT = 3
DOCTOR  = 4
STAFF   = 5

welcome_screen    = WelcomeScreen()
login_screen      = LoginScreen()
sign_screen       = SignScreen()
patient_dashboard = PatientDashboard()
doctor_dashboard  = DoctorDashboard()
staff_dashboard   = StaffDashboard()

for screen in [welcome_screen, login_screen, sign_screen,
               patient_dashboard, doctor_dashboard, staff_dashboard]:
    widget.addWidget(screen)

widget.setCurrentIndex(WELCOME)
widget.show()
sys.exit(app.exec())
