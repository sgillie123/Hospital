# auth file handles login and signup
# look over again!!!!

import re
from PyQt6 import QtCore
from base import Screen, go, state
import data

# welcome screen with the 3 buttons
class WelcomeScreen(Screen):
    def __init__(self):
        super().__init__("Welcome.ui")
        # connect buttons to login with role
        self.PatientButton.clicked.connect(lambda: self._login("Patient"))
        self.DoctorButton.clicked.connect(lambda: self._login("Doctor"))
        self.StaffButton.clicked.connect(lambda: self._login("Staff / Receptionist"))
        self.CreateAccountButton.clicked.connect(lambda: [state["signup"].reset(), go(2)])

    def _login(self, role):
        # save role and go to login screen
        data.current_login_role = role
        state["login"].set_role(role)
        go(1)

# login screen
class LoginScreen(Screen):
    def __init__(self):
        super().__init__("Login.ui")
        # making the buttons work
        self.LoginButton.clicked.connect(self._login)
        self.BackButton.clicked.connect(lambda: go(0))
        self.signupLink.linkActivated.connect(lambda _: go(2))

    def set_role(self, role):
        # show employee id only for staff and doctor
        self.roleDisplayLabel.setText(f"{role} Login")
        staff = role in ("Doctor", "Staff / Receptionist")
        self.lEmployeeID.setVisible(staff)
        self.EmployeeID.setVisible(staff)
        if not staff: self.EmployeeID.clear()

    def _login(self):
        u_name, pwd, role = self.Username.text().strip(), self.Password.text(), data.current_login_role
        # check if username exists
        if u_name not in data.users: self.errorLabel.setText("⚠ Username not found."); return
        u = data.users[u_name]
        # check password
        if u["password"] != pwd: self.errorLabel.setText("⚠ Incorrect password."); return
        # check role matches
        if u["role"] != role: self.errorLabel.setText(f"⚠ Account is a '{u['role']}' account."); return
        # employee id check for doctors and staff
        if role in ("Doctor", "Staff / Receptionist"):
            eid = self.EmployeeID.text().strip()
            if not eid or u.get("employee_id") != eid: self.errorLabel.setText("⚠ Employee ID incorrect."); return
        data.current_user = u
        self.errorLabel.setText("")
        # clear fields after login
        self.Username.clear(); self.Password.clear(); self.EmployeeID.clear()
        # go to correct dashboard
        if role == "Patient":   state["patient"].load(u); go(3)
        elif role == "Doctor":  state["doctor"].load(u);  go(4)
        else:                   state["staff"].load(u);   go(5)

# signup screen
class SignScreen(Screen):
    def __init__(self):
        super().__init__("Sign.ui")
        # connect buttons
        self.CreateButton.clicked.connect(self._create)
        self.BackButton.clicked.connect(lambda: go(0))
        self.loginLink.linkActivated.connect(lambda _: go(1))
        self.RoleCombo.currentTextChanged.connect(self._role_changed)
        self._role_changed(self.RoleCombo.currentText())

    def _role_changed(self, role):
        # hide employee id if not staff or doctor
        staff = role in ("Doctor", "Staff / Receptionist")
        self.label_8.setVisible(staff)
        self.EmployeeID.setVisible(staff)
        if not staff: self.EmployeeID.clear()

    def _create(self):
        # get all the fields
        n, u, e = self.Name.text().strip(), self.Username.text().strip(), self.Email.text().strip()
        pw, eid, role = self.Password.text(), self.EmployeeID.text().strip(), self.RoleCombo.currentText()
        dob = self.DOB.date().toString("dd/MM/yyyy")
        # validations
        if not all([n, u, e, pw]): self.errorLabel.setText("⚠ Fill in all required fields."); return
        if not re.match(r'^[A-Za-z ]+$', n): self.errorLabel.setText("⚠ Name: letters only."); return
        if not re.match(r'^[\w\.-]+@[\w\.-]+\.com$', e): self.errorLabel.setText("⚠ Invalid email."); return
        if not re.match(r'^[A-Za-z0-9]+$', u): self.errorLabel.setText("⚠ Username: alphanumeric only."); return
        if role in ("Doctor", "Staff / Receptionist") and not eid: self.errorLabel.setText("⚠ Employee ID required."); return
        if len(pw) < 6: self.errorLabel.setText("⚠ Password min 6 chars."); return
        if u in data.users: self.errorLabel.setText("⚠ Username taken."); return
        # add user to dict
        data.users[u] = {"password": pw, "role": role, "name": n, "email": e, "dob": dob, "employee_id": eid or None}
        data.current_login_role = role
        # show success and redirect
        self.errorLabel.setStyleSheet("color:#16a34a")
        self.errorLabel.setText("Account created! Redirecting...")
        state["login"].set_role(role)
        QtCore.QTimer.singleShot(1200, lambda: go(1))

    def reset(self):
        # clear everything
        self.errorLabel.setText(""); self.errorLabel.setStyleSheet("color:#dc2626")
        for f in [self.Name, self.Username, self.Email, self.Password, self.EmployeeID]: f.clear()
        self.DOB.setDate(QtCore.QDate.currentDate())
        self.RoleCombo.setCurrentText("Patient"); self._role_changed("Patient")
