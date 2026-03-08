# dashboards file has all 3 dashboards
# patient doctor and staff
# took ages lol

from datetime import datetime
from PyQt6 import QtCore
from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QMessageBox, QHeaderView
from PyQt6.QtCore import Qt
from base import Screen, go
import data

# helper function to fill a table with rows
def _fill(table, rows, cols):
    table.setRowCount(len(rows))
    for r, row in enumerate(rows):
        for c, v in enumerate(cols(row)):
            item = QTableWidgetItem(str(v))
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            table.setItem(r, c, item)

# get patient id from name
def _patient_id(name):
    p = next((p for p in data.patients if p["name"] == name), None)
    return p["id"] if p else ""

# patient dashboard screen
class PatientDashboard(Screen):
    def __init__(self):
        super().__init__("PatientDashboard.ui")
        # connect buttons
        self.BookAppointmentButton.clicked.connect(self._book)
        self.LogoutButton.clicked.connect(lambda: [setattr(data, 'current_user', None), go(0)])
        # make columns stretch
        for t in [self.AppointmentsTable, self.RecordsTable]:
            t.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # calender click
        self.patientCalendar.selectionChanged.connect(self._on_date_selected)

    def load(self, user):
        # set name and info labels
        self.patientNameLabel.setText(f"Welcome, {user['name']}")
        self.patientInfoLabel.setText(f"{user.get('email','')}  •  DOB: {user.get('dob','')}  •  Patient Portal")
        self._name = user["name"]
        self._refresh()

    def _refresh(self):
        # fill appointments table
        _fill(self.AppointmentsTable, [a for a in data.appointments if a["patient"] == self._name],
              lambda a: [a["date"], a["time"], a["doctor"], a["reason"], a["status"]])
        # fill records table
        _fill(self.RecordsTable, [r for r in data.medical_records if r["patient"] == self._name],
              lambda r: [r["date"], r["doctor"], r["diagnosis"], r["notes"]])

    def _on_date_selected(self):
        # filter appointments by selected date
        date = self.patientCalendar.selectedDate().toString("dd/MM/yyyy")
        appts = [a for a in data.appointments if a["patient"] == self._name and a["date"] == date]
        _fill(self.AppointmentsTable, appts,
              lambda a: [a["date"], a["time"], a["doctor"], a["reason"], a["status"]])
        if not appts:
            self._refresh()

    def _book(self):
        # open booking popup
        from booking import BookingDialog
        if BookingDialog(self, self._name).exec() == QDialog.DialogCode.Accepted:
            self._refresh()

# doctor dashboard
class DoctorDashboard(Screen):
    def __init__(self):
        super().__init__("DoctorDashboard.ui")
        # buttons
        self.SaveDiagButton.clicked.connect(self._save)
        self.LogoutButton.clicked.connect(lambda: [setattr(data, 'current_user', None), go(0)])
        self.AppointmentsTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # calender
        self.doctorCalendar.selectionChanged.connect(self._on_date_selected)

    def load(self, user):
        # greeting message based on time of day
        h = datetime.now().hour
        self.docGreeting.setText(f"{'Good Morning' if h<12 else 'Good Afternoon' if h<17 else 'Good Evening'}, {user['name']}")
        today = datetime.now().strftime("%d/%m/%Y")
        count = len([a for a in data.appointments if a["date"] == today])
        self.docSub.setText(f"{count} appointment(s) today  •  {today}")
        self.apptCountLabel.setText(f"{count} appointment(s) on {today}")
        self._name = user["name"]
        # load todays appointments
        self._load_appointments(today)
        self.DiagDate.setDate(QtCore.QDate.currentDate())

    def _load_appointments(self, date=None):
        # get all appointments for this doctor
        appts = [a for a in data.appointments if self._name in a["doctor"] or a["doctor"] in self._name]
        # filter by date if given
        if date:
            appts = [a for a in appts if a["date"] == date]
        _fill(self.AppointmentsTable, appts,
              lambda a: [a["time"], a["patient"], a["reason"], a["status"]])

    def _on_date_selected(self):
        # update label and filter by date
        date = self.doctorCalendar.selectedDate().toString("dd/MM/yyyy")
        self.apptCountLabel.setText(f"Appointments on {date}")
        self._load_appointments(date)

    def _save(self):
        # save a diagnosis / medical record
        patient_name = self.DiagPatientID.text().strip()
        diag = self.DiagnosisField.text().strip()
        if not all([patient_name, diag]):
            QMessageBox.warning(self, "Missing", "Fill in patient and diagnosis."); return
        pid = _patient_id(patient_name)
        # try to find matching appointment
        appt = next((a for a in data.appointments if a["patient"] == patient_name), None)
        aid = appt["id"] if appt else ""
        lab_id = self.LabIDField.text().strip()
        rid = f"R{len(data.medical_records)+1:03d}"
        # append to medical records
        data.medical_records.append({
            "record_id": rid, "patient_id": pid, "appointment_id": aid,
            "patient": patient_name, "doctor": data.current_user["name"],
            "date": self.DiagDate.date().toString("dd/MM/yyyy"),
            "diagnosis": diag, "notes": self.NotesField.text().strip(), "lab_id": lab_id
        })
        # also add lab result if lab id given
        if lab_id:
            data.lab_results.append({
                "lab_id": lab_id, "patient_id": pid, "appointment_id": aid, "results": ""
            })
        QMessageBox.information(self, "Saved", f"Record {rid} saved for {patient_name}.")
        # clear fields
        for f in [self.DiagPatientID, self.DiagnosisField, self.NotesField, self.LabIDField]:
            f.clear()

# staff / receptionist dashboard
class StaffDashboard(Screen):
    def __init__(self):
        super().__init__("StaffDashboard.ui")
        # connect all the buttons
        self.RegisterPatientButton.clicked.connect(self._register)
        self.LogoutButton.clicked.connect(lambda: [setattr(data, 'current_user', None), go(0)])
        self.SearchPatient.textChanged.connect(self._refresh)
        # stretch columns
        self.PatientsTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        # calender
        self.staffCalendar.selectionChanged.connect(self._on_date_selected)

    def load(self, user):
        # set greeting and stats
        self.staffGreeting.setText(f"Welcome, {user['name']}")
        self.statsLabel.setText(f"{len(data.patients)} registered patients  •  {len(data.appointments)} total appointments")
        self._refresh()

    def _on_date_selected(self):
        # show appointments for selected date
        date = self.staffCalendar.selectedDate().toString("dd/MM/yyyy")
        count = len([a for a in data.appointments if a["date"] == date])
        self.statsLabel.setText(f"{count} appointment(s) on {date}  •  {len(data.patients)} total patients")

    def _refresh(self, text=""):
        # filter patients by search text
        ft = (text or self.SearchPatient.text()).lower()
        rows = [p for p in data.patients if ft in p["name"].lower() or ft in p["id"].lower()] if ft else data.patients
        _fill(self.PatientsTable, rows,
              lambda p: [p["id"], p["name"], p["dob"], p["phone"], p["blood"], p["registered"]])

    def _register(self):
        # get form data
        name = self.PatName.text().strip()
        if not name or len(name) < 3:
            QMessageBox.warning(self, "Invalid", "Please enter a full name (at least 3 characters)."); return
        dob = self.PatDOB.date().toString("dd/MM/yyyy")
        nid = f"P{len(data.patients)+1:03d}"
        email, phone = self.PatEmail.text().strip(), self.PatPhone.text().strip()
        # check if PatientType widget exists (only in new ui)
        patient_type = self.PatientType.currentText() if hasattr(self, 'PatientType') else 'Outpatient'
        # add patient to list
        data.patients.append({
            "id": nid, "name": name, "dob": dob, "gender": self.PatGender.currentText(),
            "email": email, "phone": phone, "address": "",
            "blood": self.BloodType.currentText(), "emergency": self.EmergContact.text().strip(),
            "registered": datetime.now().strftime("%d/%m/%Y"),
            "patient_type": patient_type, "prescription": "",
            "date_admitted": "", "date_discharged": "", "treatment": ""
        })
        # create login for the patient
        uname = name.lower().replace(" ", "") + nid
        data.users[uname] = {"password": dob.replace("/", ""), "role": "Patient",
                              "name": name, "email": email, "dob": dob, "phone": phone,
                              "gender": self.PatGender.currentText(), "address": ""}
        # create a blank bill
        data.bills.append({"bill_id": f"B{len(data.bills)+1:03d}", "patient_id": nid,
                            "appointment_id": "", "amount_due": 0.0, "paid": False})
        # show success popup
        msg = QMessageBox(self)
        msg.setWindowTitle("Patient Registered")
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Patient registered successfully!")
        msg.setInformativeText(f"Patient ID:   {nid}\nType:             {patient_type}\nUsername:   {uname}\nPassword:    {dob.replace('/', '')}")
        msg.setMinimumWidth(400)
        msg.exec()
        # clear the form
        for f in [self.PatName, self.PatEmail, self.PatPhone, self.EmergContact]:
            f.clear()
        self.PatDOB.setDate(QtCore.QDate.currentDate())
        # update stats
        self.statsLabel.setText(f"{len(data.patients)} registered patients  •  {len(data.appointments)} total appointments")
        self._refresh()
