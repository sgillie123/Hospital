# this is the data file i made it store all the info
# testing

# all the users go here i think
users = {
    "patient1":      {"password": "pass", "role": "Patient", "name": "Alice Johnson",
                      "email": "alice@email.com", "dob": "15/03/1990", "phone": "555-1001", "gender": "Female", "address": ""},
    "drsmith":       {"password": "pass", "role": "Doctor", "name": "Dr. James Smith",
                      "email": "james@hospital.com", "dob": "10/05/1975", "phone": "555-2000",
                      "gender": "Male", "address": "", "employee_id": "DOC001", "specialty": "General Practice"},
    # receptionist person
    "receptionist1": {"password": "pass", "role": "Staff / Receptionist",
                      "name": "Maria Lopez", "email": "maria@hospital.com",
                      "dob": "22/08/1985", "phone": "555-3000", "gender": "Female", "address": "",
                      "employee_id": "STF001", "specialty": ""},
}

# list of patients idk if this is right
patients = [
    {"id": "P001", "name": "Alice Johnson", "dob": "15/03/1990", "phone": "555-1001",
     "blood": "A+", "gender": "Female", "email": "alice@email.com", "address": "",
     "emergency": "Bob Johnson — 555-1002", "registered": "01/01/2024",
     # added these for the inpatient outpatient thing
     "patient_type": "Outpatient", "prescription": "", "date_admitted": "", "date_discharged": "", "treatment": ""},
    {"id": "P002", "name": "Carlos Rivera", "dob": "20/07/1985", "phone": "555-2002",
     "blood": "O+", "gender": "Male", "email": "carlos@email.com", "address": "",
     "emergency": "Ana Rivera — 555-2003", "registered": "15/02/2024",
     "patient_type": "Outpatient", "prescription": "", "date_admitted": "", "date_discharged": "", "treatment": ""},
]

# appointmets (appointments)
appointments = [
    {"id": "A001", "patient_id": "P001", "patient": "Alice Johnson", "doctor": "Dr. James Smith",
     "date": "07/03/2026", "time": "09:00 AM", "reason": "Annual Checkup", "status": "Confirmed", "notes": ""},
    {"id": "A002", "patient_id": "P002", "patient": "Carlos Rivera", "doctor": "Dr. James Smith",
     "date": "07/03/2026", "time": "10:30 AM", "reason": "Follow-up", "status": "Confirmed", "notes": ""},
]

# medical records i changed from diagnoses to this
medical_records = [
    {"record_id": "R001", "patient_id": "P001", "appointment_id": "A001", "patient": "Alice Johnson",
     "doctor": "Dr. James Smith", "date": "01/02/2026",
     "diagnosis": "Seasonal Allergy", "notes": "Cetirizine 10mg once daily", "lab_id": ""},
]

# lab stuff
lab_results = [
    {"lab_id": "L001", "patient_id": "P001", "appointment_id": "A001", "results": "Normal"},
]

# bills table for part 2 maybe
bills = [
    {"bill_id": "B001", "patient_id": "P001", "appointment_id": "A001", "amount_due": 0.0, "paid": False},
]

# current user thats logged in
current_user = None
current_login_role = "Patient"
