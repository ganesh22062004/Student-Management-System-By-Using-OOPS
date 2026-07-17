class Student:
    students = {}  # to store all students
    school_name = "XYZ School"

    def __init__(self, roll_no, name, phone, address, student_class):
        self.roll_no = roll_no
        self.name = name
        self.phone = phone
        self.address = address
        self.student_class = student_class

        # Store object in dictionary
        Student.students[self.roll_no] = self

    def display(self):
        print("\n----- Student Details -----")
        print("Roll No :", self.roll_no)
        print("Name    :", self.name)
        print("Phone   :", self.phone)
        print("Address :", self.address)
        print("Class   :", self.student_class)
        print("School  :", Student.school_name)

    def update(self):
        print("\n1. Change Name")
        print("2. Change Phone")
        print("3. Change Address")
        print("4. Change Class")

        choice = input("Enter choice (1-4): ")

        if choice == "1":
            self.name = input("Enter new name: ")
        elif choice == "2":
            self.phone = input("Enter new phone: ")
        elif choice == "3":
            self.address = input("Enter new address: ")
        elif choice == "4":
            self.student_class = input("Enter new class: ")
        else:
            print("Invalid choice")
            return

        print("Student updated successfully!")
        self.display()

    @classmethod
    def total_students(cls):
        return len(cls.students)

    @classmethod
    def change_school_name(cls):
        cls.school_name = input("Enter new school name: ")
        print("School name updated successfully!")


def main():
    print("\n===== Welcome to Student Management System =====")
    print("""
1. Add Student
2. View Student
3. Update Student
4. Delete Student
5. Total Students
6. Change School Name
7. View All Students
""")

    option = input("Enter your choice (1-7): ")

    if option == "1":
        roll = input("Enter Roll No: ")
        name = input("Enter Name: ")
        phone = input("Enter Phone: ")
        address = input("Enter Address: ")
        student_class = input("Enter Class: ")

        Student(roll, name, phone, address, student_class)
        print("Student added successfully!")

    elif option == "2":
        roll = input("Enter Roll No: ")
        if roll in Student.students:
            Student.students[roll].display()
        else:
            print("Student not found")

    elif option == "3":
        roll = input("Enter Roll No: ")
        if roll in Student.students:
            Student.students[roll].update()
        else:
            print("Student not found")

    elif option == "4":
        roll = input("Enter Roll No: ")
        if roll in Student.students:
            Student.students.pop(roll)
            print("Student deleted successfully!")
        else:
            print("Student not found")

    elif option == "5":
        print("Total Students:", Student.total_students())

    elif option == "6":
        Student.change_school_name()

    elif option == "7":
        if Student.students:
            print("\nTotal Students:", Student.total_students())
            for stu in Student.students.values():
                stu.display()
        else:
            print("No students available")

    else:
        print("Invalid option")


if __name__ == "__main__":
    while True:
        main()
        cont = input("\nDo you want to continue? (y/n): ")
        if cont.lower() != "y":
            print("Thank you!")
            break
