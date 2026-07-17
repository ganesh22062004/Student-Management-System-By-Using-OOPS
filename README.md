Student Management System
Overview

The Student Management System is a simple command-line application developed in Python using Object-Oriented Programming (OOP) concepts. It allows users to manage student records by adding, viewing, updating, deleting, and listing students. The application also provides functionality to change the school name for all students and display the total number of registered students.

Features
Add new student records
View student details using Roll Number
Update student information
Delete student records
Display the total number of students
Change the school name (applies to all students)
View all registered students
Menu-driven and user-friendly interface
Technologies Used
Programming Language: Python 3
Concepts: Object-Oriented Programming (Classes, Objects, Class Methods)
Storage: In-memory dictionary (No database required)
Project Structure
Student-Management-System/
│
├── student_management.py    # Main Python program
├── README.md                # Project documentation
Class Design
Student Class
Attributes
Attribute	Description
roll_no	Student Roll Number
name	Student Name
phone	Contact Number
address	Student Address
student_class	Student Class
school_name	Common school name (Class Variable)
students	Dictionary storing all student objects
Methods
Method	Description
display()	Displays student details
update()	Updates student information
total_students()	Returns total number of students
change_school_name()	Updates the school name for all students
Menu Options
===== Welcome to Student Management System =====

1. Add Student
2. View Student
3. Update Student
4. Delete Student
5. Total Students
6. Change School Name
7. View All Students
Sample Output
===== Welcome to Student Management System =====

1. Add Student
2. View Student
3. Update Student
4. Delete Student
5. Total Students
6. Change School Name
7. View All Students

Enter your choice: 1

Enter Roll No: 101
Enter Name: John
Enter Phone: 9876543210
Enter Address: Hyderabad
Enter Class: 10

Student added successfully!

View Student

----- Student Details -----

Roll No : 101
Name    : John
Phone   : 9876543210
Address : Hyderabad
Class   : 10
School  : XYZ School
How to Run
1. Clone the Repository
git clone https://github.com/your-username/student-management-system.git
2. Navigate to the Project Directory
cd student-management-system
3. Run the Program
python student_management.py

Ensure Python 3 is installed on your system.

OOP Concepts Used
Classes and Objects
Constructors (__init__)
Instance Variables
Class Variables
Class Methods
Encapsulation
Dictionary-based Object Management
Current Limitations
Data is stored only in memory.
Student records are lost after the program exits.
No input validation for phone numbers or duplicate roll numbers.
Single-user command-line application.
Future Enhancements
Save records using SQLite or MySQL.
Store data in JSON or CSV files.
Add search by student name.
Validate user inputs.
Build a graphical user interface (Tkinter/PyQt).
Develop a web-based version using Flask or Django.
Add login and authentication.
Generate student reports.
Learning Objectives

This project demonstrates:

Python Object-Oriented Programming
Class and Object Management
CRUD (Create, Read, Update, Delete) Operations
Dictionary-based Data Storage
Menu-Driven Console Applications
Author

Your Name

GitHub: https://github.com/ganesh22062004/Student-Management-System-By-Using-OOPS
Email: ganeshpattiguda@gamil.com
License

This project is open source and available under the MIT License.

Project Status

Completed – Suitable for Python beginners and intermediate learners to understand OOP, CRUD operations, and command-line application development.
