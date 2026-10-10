
from storage import load_students, save_students
from student import Student

# Load saved students when the program starts
students = load_students()


def add_student(student):
    for existing_student in students:
        if existing_student.student_id == student.student_id:
            print("Error: Student ID already exists.")
            return

    students.append(student)
    save_students(students)
    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    for student in students:
        print(
            f"Student ID: {student.student_id} | "
            f"Name: {student.name} | "
            f"Age: {student.age} | "
            f"Marks: {student.marks}"
        )


def search_student(student_id):
    for student in students:
        if student.student_id == student_id:
            print(
                f"Student Found: {student.name} | "
                f"Age: {student.age} | "
                f"Marks: {student.marks}"
            )
            return student

    print("Student not found.")
    return None


def update_student(student_id, new_marks):
    for student in students:
        if student.student_id == student_id:
            if (
                not isinstance(new_marks, (int, float))
                or isinstance(new_marks, bool)
                or not 0 <= new_marks <= 100
            ):
                print("Invalid marks. Enter a value between 0 and 100.")
                return

            student.marks = new_marks
            save_students(students)
            print("Marks updated successfully!")
            return

    print("Student not found.")


def delete_student(student_id):
    for student in students:
        if student.student_id == student_id:
            students.remove(student)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found.")


def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                print("Please enter a positive integer.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_marks(prompt):
    while True:
        try:
            marks = float(input(prompt))

            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
                continue

            return marks

        except ValueError:
            print("Invalid input. Please enter a number.")


def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            student_id = get_positive_integer("Enter student ID: ")
            name = input("Enter student name: ").strip()
            age = get_positive_integer("Enter student age: ")
            marks = get_marks("Enter student marks (0-100): ")

            try:
                student = Student(student_id, name, age, marks)
                add_student(student)
            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            view_students()

        elif choice == "3":
            student_id = get_positive_integer("Enter student ID to search: ")
            search_student(student_id)

        elif choice == "4":
            student_id = get_positive_integer("Enter student ID to update: ")
            new_marks = get_marks("Enter new marks (0-100): ")
            update_student(student_id, new_marks)

        elif choice == "5":
            student_id = get_positive_integer("Enter student ID to delete: ")
            delete_student(student_id)

        elif choice == "6":
            save_students(students)
            print("Data saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()