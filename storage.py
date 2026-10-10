import json

from student import Student



def load_students():
    try:
        with open("students.json", "r") as file:
            data = json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Warning: students.json is empty or invalid. Starting with an empty list.")
        return []

    students = []

    for item in data:
        student = Student(
            item["student_id"],
            item["name"],
            item["age"],
            item["marks"]
        )
        students.append(student)

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

    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Students saved successfully!")

