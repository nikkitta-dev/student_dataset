"""
Generates a fictional student dataset and saves it as students.csv

Columns:
    Student_ID, Department, Level, Attendance_Percentage, Average_Exam_Score

Student_ID format:  YY/DDNNN
    YY  = last two digits of the year the student enrolled (e.g. 25 for 2025)
    DD  = department ID (17-21)
    NNN = admission number within that year and department (e.g. 762 means
          the 762nd student admitted that year into that department)

Usage:
    python generate_students.py
"""

import csv
import random

random.seed(42)  # makes the output reproducible

NUM_STUDENTS = 100
CURRENT_YEAR = 2026

# Department ID -> Department name
DEPARTMENTS = {
    17: "Computer Science",
    18: "Software Engineering",
    19: "Information Systems",
    20: "Artificial Intelligence",
    21: "Cyber Security",
}
LEVELS = [100, 200, 300, 400]

# Tracks admission numbers already used per (year, department)
used_numbers = {}


def make_student():
    dept_id = random.choice(list(DEPARTMENTS))
    level = random.choice(LEVELS)

    enrol_year = CURRENT_YEAR - level // 100          # 100L -> 2025, 400L -> 2022
    yy = enrol_year % 100

    taken = used_numbers.setdefault((yy, dept_id), set())
    admission_no = random.randint(1, 999)
    while admission_no in taken:
        admission_no = random.randint(1, 999)
    taken.add(admission_no)

    student_id = f"{yy}/{dept_id}{admission_no:03d}"   # e.g. 25/17762

    attendance = round(random.uniform(40, 100), 1)

    # Make scores loosely follow attendance so the data is realistic
    base = 20 + attendance * 0.6
    score = round(min(100, max(0, random.gauss(base, 10))), 1)

    return [student_id, DEPARTMENTS[dept_id], level, attendance, score]


def main():
    header = [
        "Student_ID",
        "Department",
        "Level",
        "Attendance_Percentage",
        "Average_Exam_Score",
    ]
    rows = [make_student() for _ in range(NUM_STUDENTS)]

    with open("students.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

    print(f"Created students.csv with {len(rows)} records.")


if __name__ == "__main__":
    main()
