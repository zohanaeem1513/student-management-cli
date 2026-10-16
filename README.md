# Student Management CLI

A modular, command-line student management application built with Python and JSON-based data persistence.

## Overview

**Student Management CLI** is a Python application designed to manage student records through an interactive terminal interface. It demonstrates core programming concepts, object-oriented design, input validation, exception handling, and persistent data storage using JSON.

The project is designed to strengthen Python fundamentals while following a clean, modular approach to application development.

## Features

* **Add Students** — Create student records with essential details.
* **View Students** — Display all stored student records.
* **Search Students** — Find a student using their unique ID.
* **Update Marks** — Modify a student's marks.
* **Delete Students** — Remove student records.
* **Input Validation** — Validate student details and restrict invalid values.
* **JSON Persistence** — Store records locally in a JSON file.
* **Automatic Data Loading** — Load saved records when the application starts.
* **Modular Architecture** — Separate student models, storage operations, and application logic.

## Technology Stack

| Technology | Purpose                                    |
| ---------- | ------------------------------------------ |
| Python     | Application logic and core functionality   |
| JSON       | Local data storage                         |
| Git        | Version control                            |
| GitHub     | Source code hosting and project management |

**Dependencies:** The application uses Python's standard library and does not require external packages for its core functionality.

## Project Structure

```text
student-management-cli/
├── main.py          # Application entry point and menu
├── student.py       # Student model and validation
├── storage.py       # JSON loading and saving
├── students.json    # Local student data (not committed)
├── .gitignore       # Excluded files and directories
└── README.md        # Project documentation
```

## Getting Started

### Prerequisites

* Python 3.10 or later, or another version compatible with the code.
* Git (optional, for cloning the repository).

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/zohanaeem1513/student-management-cli.git
```

**2. Navigate to the project directory**

```bash
cd student-management-cli
```

**3. Run the application**

```bash
python main.py
```

On Windows, you can also use:

```powershell
py main.py
```

## Usage

After starting the application, use the interactive menu to select an operation.

| Option | Operation            |
| ------ | -------------------- |
| 1      | Add a student        |
| 2      | View all students    |
| 3      | Search for a student |
| 4      | Update student marks |
| 5      | Delete a student     |
| 6      | Exit the application |

Follow the terminal prompts to enter student details and perform the selected operation.

## Data Storage

Student records are stored locally in `students.json` using JSON format. The storage module handles loading records when the application starts and saving changes to the file.

The JSON file is intended for local development and is excluded from version control to help prevent accidental publication of student data.

> **Note:** Keep sensitive or personally identifiable student information out of public repositories.

## Concepts Demonstrated

This project provides practical experience with:

* Object-oriented programming (OOP)
* Classes, objects, and constructors
* Functions and modular programming
* Lists, dictionaries, and loops
* Conditional statements
* Input validation and exception handling
* JSON serialization and deserialization
* File handling and data persistence
* Git and GitHub workflows

## Future Improvements

Potential enhancements include:

* Automated unit tests using `pytest`
* Improved handling of malformed or corrupted JSON files
* Sorting and filtering student records
* Calculating average marks and identifying top-performing students
* Adding a database such as SQLite
* Introducing a graphical user interface or REST API

## Author

**Zoha Naeem**

GitHub: [@zohanaeem1513](https://github.com/zohanaeem1513)


*Built with Python as part of a journey toward developing practical software engineering and AI/ML skills.*
