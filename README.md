# 🎓 Student Management System

A simple and interactive **Student Management System** built with **Python** using **Object-Oriented Programming (OOP)** concepts. This project allows users to manage student records through a menu-driven command-line interface.

---

## 📌 Features

* ➕ Add a new student
* 👀 View student details
* ✏️ Update student information
* 🗑️ Delete a student record
* 📊 Display the total number of students
* 🏫 Change the school name for all students
* 📋 View all student records
* 🔄 Menu-driven interface with continuous execution

---

## 🛠️ Technologies Used

* **Python 3**
* Object-Oriented Programming (OOP)
* Dictionary Data Structure
* Command-Line Interface (CLI)

---

## 📂 Project Structure

```text
Student-Management-System-By-Using-OOPS/
│
├── Student management system oops.py
└── README.md
```
## 🚀 Getting Started

### Prerequisites

* Python 3.8 or later

### Installation

1. Clone the repository:

```bash
git clone https://github.com/ganesh22062004/Student-Management-System-By-Using-OOPS.git
```

2. Navigate to the project directory:

```bash
cd Student-Management-System-By-Using-OOPS
```

3. Run the application:

```bash
python "Student management system oops.py"
```

---

## 📖 How It Works

After running the program, the following menu is displayed:

```text
1. Add Student
2. View Student
3. Update Student
4. Delete Student
5. Total Students
6. Change School Name
7. View All Students
```

Choose an option by entering the corresponding number and follow the prompts.

---

## 🧱 Object-Oriented Design

### Student Class

The `Student` class stores and manages student information.

### Attributes

| Attribute       | Description                         |
| --------------- | ----------------------------------- |
| `roll_no`       | Student Roll Number                 |
| `name`          | Student Name                        |
| `phone`         | Contact Number                      |
| `address`       | Student Address                     |
| `student_class` | Student Class                       |
| `school_name`   | Shared school name (Class Variable) |

---

## ⚙️ Methods

### Instance Methods

* `display()` – Displays student information.
* `update()` – Updates student details.

### Class Methods

* `total_students()` – Returns the total number of students.
* `change_school_name()` – Updates the school name for all students.

---

## 📸 Sample Output

```text
===== Welcome to Student Management System =====

1. Add Student
2. View Student
3. Update Student
4. Delete Student
5. Total Students
6. Change School Name
7. View All Students

Enter your choice (1-7): 1

Enter Roll No: 101
Enter Name: John
Enter Phone: 9876543210
Enter Address: Hyderabad
Enter Class: 10

Student added successfully!
```

---

## 💡 Future Improvements

* Store data permanently using JSON, CSV, or SQLite
* Validate user input
* Prevent duplicate roll numbers
* Search students by name
* Sort student records
* Export student data to Excel or CSV
* Develop a graphical user interface (GUI) using Tkinter or PyQt
* Build a web version using Flask or Django

---

## 🎯 Learning Outcomes

This project demonstrates:

* Python programming fundamentals
* Object-Oriented Programming (OOP)
* Classes and Objects
* Constructors (`__init__`)
* Instance and Class Variables
* Class Methods (`@classmethod`)
* Dictionaries for data storage
* Menu-driven application development

---

## 🤝 Contributing

Contributions are welcome. Feel free to fork the repository, create a feature branch, and submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this project with proper attribution.

---

## 👨‍💻 Author

**Ganesh Pattiguda**

* GitHub: https://github.com/ganesh22062004
* LinkedIn: https://www.linkedin.com/in/ganesh-pattiguda/

> If you found this project helpful, consider giving it a ⭐ on GitHub.
