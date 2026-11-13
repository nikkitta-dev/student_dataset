# Fictional Student Dataset

A Python script that generates a fictional student dataset for CUL-CYB 371 (Data Mining and Data Warehousing).

## Fields
- Student_ID (format `YY/DDNNN`, e.g. `25/17762`)
  - `YY`: year of enrolment (25 = 2025)
  - `DD`: department ID (17 Computer Science, 18 Software Engineering, 19 Information Systems, 20 Artificial Intelligence, 21 Cyber Security)
  - `NNN`: admission number within that year and department
- Department
- Level
- Attendance_Percentage
- Average_Exam_Score

## Run
```
python generate_students.py
```
This creates `students.csv` with 100 records.
