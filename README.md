# Dont Drop Dead — Hospital Management System

Part 1 to a hospital management system built with Python and PyQt6 for managing patients, doctors, and staff.

## How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the app:
```
python app.py
```

## Test Logins

| Role | Username | Password | Employee ID |
|------|----------|----------|-------------|
| Patient | patient1 | pass | — |
| Doctor | drsmith | pass | DOC001 |
| Staff | receptionist1 | pass | STF001 |

## Files

- `app.py` — entry point
- `auth.py` — login, signup, welcome screens
- `base.py` — base screen class with responsive scaling
- `dashboards.py` — patient, doctor, staff dashboards
- `booking.py` — book appointment popup
- `data.py` — in-memory data (patients, appointments, records)
- `*.ui` — Qt Designer UI files

## Features

- Patient portal with appointment booking and medical records
- Doctor portal with appointment calendar and diagnosis entry
- Staff portal with patient registration and search
