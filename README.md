# 🎓 Student Management CLI

<p align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=36BCF7&center=true&vCenter=true&width=700&lines=Student+Management+CLI;Manage+Student+Records+with+Python;Add+%E2%80%A2+Search+%E2%80%A2+Update+%E2%80%A2+Delete;JSON-Based+Persistent+Storage"
    alt="Typing SVG"
  />
</p>

<p align="center">
  A modular command-line application for managing student records
  using Python and JSON.
</p>



<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Storage-JSON-lightgrey" alt="JSON Storage">
  <img src="https://img.shields.io/badge/Interface-CLI-black" alt="CLI">
  <img src="https://img.shields.io/badge/Status-Learning%20Project-blue" alt="Learning Project">
</p>

---

## ✨ Features

| Feature | Description |
|---|---|
| ➕ Add Students | Create student records with essential details |
| 📋 View Students | Display all saved student records |
| 🔍 Search Students | Find a student using their unique ID |
| 📝 Update Marks | Modify a student's marks |
| 🗑️ Delete Students | Remove a student record |
| ✅ Input Validation | Validate student input and reject invalid values |
| 💾 JSON Storage | Persist records locally between application runs |
| 🧩 Modular Design | Separate application logic, student models, and storage |

## 🖥️ Preview

The application runs in your terminal and provides an interactive menu for managing student records.

```text
================================
     STUDENT MANAGEMENT CLI
================================

1. Add Student
2. View All Students
3. Search Student
4. Update Student Marks
5. Delete Student
6. Exit

Enter your choice:
```

*Illustrative menu preview. The actual display depends on your implementation.*

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or a compatible version
- Git (to clone the repository)

### 1. Clone the repository

```bash
git clone https://github.com/zohanaeem1513/student-management-cli.git
```

### 2. Navigate to the project

```bash
cd student-management-cli
```

### 3. Run the application

```bash
python main.py
```

On Windows, you can also run:

```powershell
py main.py
```

## 📂 Project Structure

```text
student-management-cli/
├── main.py          # Application entry point and menu
├── student.py       # Student model and validation
├── storage.py       # JSON loading and saving
├── students.json    # Local student data, created at runtime
├── .gitignore       # Excluded files and directories
└── README.md        # Project documentation
```

## ⚙️ How It Works

```text
       User
        |
        v
  Interactive CLI
        |
        v
  Input Validation
        |
        v
  Student Operations
   /    |    |    \
 Add  View  Update Delete
        |
        v
   Storage Module
        |
        v
   students.json
```

1. **User interaction:** The user selects an operation from the CLI menu.
2. **Validation:** The application checks the provided input.
3. **Student operations:** The application creates, searches, updates, displays, or deletes records.
4. **Persistence:** The storage module loads and saves student data in JSON format.

## 💾 Data Storage

Student records are stored in `students.json`.

- Existing records are loaded when the application starts.
- Changes are saved to the local JSON file.
- The data file is excluded from version control to help prevent accidental exposure of student information.

**Note:** Do not store real, sensitive student information in a public repository.

## 🧠 Concepts Demonstrated

This project demonstrates practical Python fundamentals:

- Object-oriented programming (OOP)
- Classes, objects, and constructors
- Functions and modular code organization
- Lists, dictionaries, and loops
- Input validation and exception handling
- File handling with `pathlib`
- JSON serialization and deserialization
- Git and GitHub version control

## 🛣️ Future Improvements

- [ ] Add automated tests with `pytest`
- [ ] Improve recovery from malformed JSON data
- [ ] Add sorting and filtering
- [ ] Calculate averages and identify top-performing students
- [ ] Introduce SQLite database support
- [ ] Add a REST API using FastAPI

## 👨‍💻 Author

**Zoha Naeem**

- GitHub: [@zohanaeem1513](https://github.com/zohanaeem1513)


⭐ **Star this repo if it helped you!** ⭐
