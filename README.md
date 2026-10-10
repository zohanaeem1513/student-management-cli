# Student Management CLI

A command-line Student Management System built with Python and JSON for storing and managing student records.

## 📌 Overview

The Student Management CLI is a Python project that allows users to manage student information through a simple interactive terminal menu. It demonstrates Python fundamentals, object-oriented programming, input validation, exception handling, and file-based data persistence.

## ✨ Features

* **Add Students:** Store student ID, name, age, and marks.
* **View Students:** Display all saved student records.
* **Search Students:** Find a student using their ID.
* **Update Marks:** Modify a student's marks.
* **Delete Students:** Remove a student record.
* **Duplicate ID Prevention:** Prevent multiple students from using the same ID.
* **Input Validation:** Validate student IDs, ages, and marks.
* **JSON Storage:** Save student records in a JSON file.
* **Automatic Loading:** Load saved student records when the program starts.

## 🛠️ Technologies Used

* **Python 3.13+**
* **JSON** for data storage
* **Git and GitHub** for version control

No external Python packages are required for the core application.

## 📂 Project Structure

```text
student-management-cli/
├── main.py          # Main menu and application logic
├── student.py       # Student class and validation
├── storage.py       # Saving and loading student records
├── students.json    # Local student data (generated/used by the app)
├── .gitignore       # Files excluded from Git
└── README.md        # Project documentation
```

> Note: `students.json` is intended for local data storage and should not be committed if it contains personal student information.

## ⚙️ Requirements

* Python 3.13 or a compatible Python 3 version
* Git (optional, for cloning the repository)

Check your Python installation:

```bash
python --version
```

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/zohanaeem1513/student-management-cli.git
```

### 2. Navigate to the project directory

```bash
cd student-management-cli
```

### 3. Run the application

```bash
python main.py
```

## 💻 How to Use

When you run the program, an interactive menu allows you to select an operation.

| Option | Operation            |
| ------ | -------------------- |
| 1      | Add Student          |
| 2      | View All Students    |
| 3      | Search Student       |
| 4      | Update Student Marks |
| 5      | Delete Student       |
| 6      | Exit                 |

Follow the terminal prompts to enter the required information.

### Example Student Record

```text
Student ID: 2
Name: Zoha
Age: 23
Marks: 95.0
```

Student records are stored locally in `students.json` and loaded when the application starts.

## 🧠 Concepts Demonstrated

This project provides practical experience with:

* Classes and objects
* Functions and loops
* Lists and dictionaries
* Conditional statements
* Input validation
* Exception handling using `try` and `except`
* Reading and writing JSON files
* Modular programming using multiple Python files
* Version control with Git

## 🔒 Data and Privacy

Student records are stored in a local JSON file. The application does not require a database or an internet connection to manage local records.

Avoid uploading real student information or other sensitive data to a public repository.

## 🗺️ Future Improvements

* Add automated tests using `pytest`.
* Sort students by marks.
* Calculate average marks.
* Identify the highest-scoring student.
* Improve error handling for corrupted JSON files.
* Add a more detailed user guide.

## 👩‍💻 Author

**Zoha Naeem**

GitHub: [@zohanaeem1513](https://github.com/zohanaeem1513)


