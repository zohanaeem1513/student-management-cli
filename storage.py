import json
import os
from pathlib import Path

from student import Student

BASE_DIR = Path(__file__).resolve().parent
STUDENTS_FILE = BASE_DIR / "students.json"


def load_students():
    try:
        with open(STUDENTS_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Warning: students.json is empty or invalid. Starting with an empty list.")
        return []

    students = []

    for item in data:
        try:
            student = Student(
                item["student_id"],
                item["name"],
                item["age"],
                item["marks"]
            )
            students.append(student)
            try:
                save_students(students)
            except OSError:
                students.remove(student)
                print("Student was not saved. Please try again."  )  

        except (KeyError, TypeError, ValueError) as error:
            print(f"Warning: Skipping invalid student record: {error}")

    return students


def save_students(students):
    data = []

    for student in students:
        data.append({
            "student_id": student.student_id,
            "name": student.name,
            "age": student.age,
            "marks": student.marks
        })

    temp_file = STUDENTS_FILE.with_suffix(".json.tmp")

    try:
        with open(temp_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
            file.flush()
            os.fsync(file.fileno())

        os.replace(temp_file, STUDENTS_FILE)
        print("Students saved successfully!")

    except OSError as error:
        print(f"Error saving students: {error}")
        raise