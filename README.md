# StudentManagementSystem-Python
# 🎓 Student Management System

A Command Line Interface (CLI) based Student Management System developed using Python. The project demonstrates the concepts of Object-Oriented Programming (OOP), File Handling using JSON, Exception Handling, Modular Programming, and Git.

---

## 📌 Project Description

This application allows users to manage student records through a simple command-line interface. Users can add, view, search, update, and delete student records. Student information is stored permanently in a JSON file, ensuring that the data remains available even after the program is closed.

---

## ✨ Features

- Add a new student
- View all students
- Search a student by Student ID
- Update student details
- Delete a student
- Store data permanently using JSON
- Automatically load saved data when the program starts
- Exception handling for file operations

---

## 🛠 Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- File Handling
- Exception Handling
- Git
- GitHub

---

## 📂 Project Structure

```
StudentManagementSystem/
│
├── main.py
├── manager.py
├── student.py
├── filehandler.py
├── students.json
├── README.md
└── __pycache__/
```

---

## 📖 Modules Description

### `student.py`
Contains the `Student` class used to create student objects.

### `manager.py`
Contains the `StudentManager` class which performs all CRUD operations:
- Add Student
- View Students
- Search Student
- Update Student
- Delete Student

### `filehandler.py`
Responsible for reading and writing student data to the `students.json` file.

### `main.py`
Contains the menu-driven interface and interacts with the user.

### `students.json`
Stores student data permanently in JSON format.

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
```

### 2. Move to the project directory

```bash
cd StudentManagementSystem
```

### 3. Run the application

```bash
python main.py
```

---

## 💻 Menu Options

```
1. Add Student
2. View Student
3. Search Student
4. Update Student
5. Delete Student
6. Exit
```

---

## 📁 Data Storage

Student records are stored in **students.json** using JSON format.

The project converts:

```
Student Object
      ↓
Python Dictionary
      ↓
JSON File
```

While reading:

```
JSON File
      ↓
Python Dictionary
      ↓
Student Object
```

---

## ⚠ Exception Handling

The project handles common file-related exceptions such as:

- FileNotFoundError
- JSON decoding errors
- General exceptions while reading and writing files

---

## 📚 Python Concepts Used

- Classes & Objects
- Constructors (`__init__`)
- Object-Oriented Programming (OOP)
- Lists
- Dictionaries
- Loops
- Functions
- Modules
- JSON File Handling
- Exception Handling

---

## 🎯 Future Improvements

- Input validation
- Duplicate Student ID checking
- Email validation
- Sorting student records
- Export data to CSV
- GUI version using Tkinter

---

## 👨‍💻 Author

**Your Name**

---

## 📜 License

This project is developed for learning purposes as part of a Python assignment.