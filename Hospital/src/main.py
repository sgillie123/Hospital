# main file that runs everything
# i made this to start the app

import sys
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QStackedWidget
import base
from auth import WelcomeScreen, LoginScreen, SignScreen
from dashboards import PatientDashboard, DoctorDashboard, StaffDashboard

# making the app
app = QApplication(sys.argv)
app.setFont(QtGui.QFont("Segoe UI", 10))

# main window with all screens stacked
widget = QStackedWidget()
widget.setWindowTitle("Dont Drop Dead — Hospital Management System")

# create all the screens
welcome, login, signup, patient, doctor, staff = (
    WelcomeScreen(), LoginScreen(), SignScreen(),
    PatientDashboard(), DoctorDashboard(), StaffDashboard()
)

# add screens to the stack
for s in [welcome, login, signup, patient, doctor, staff]:
    widget.addWidget(s)

# put screens in state so other files can access them
base.state.update({"widget": widget, "login": login, "signup": signup,
                   "patient": patient, "doctor": doctor, "staff": staff})

# show welcome screen first
widget.setCurrentIndex(0)
widget.showMaximized()
sys.exit(app.exec())
