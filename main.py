# From manager.py, class StudentManager is being imported
from manager import StudentManager

# Created an instance/object of class StudentManager
manager = StudentManager()

while True:
    print("\n---------------Welcome To Student Management System---------------")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    print(choice, type(choice))

    if choice == 1:
        manager.add_student()

    elif choice == 2:
        manager.view_students()

    elif choice == 3:
        manager.search_student()

    elif choice == 4:
        manager.update_student()

    elif choice == 5:
        manager.delete_student()

    elif choice == 6:
        print("Thank you for using Student Management System")
        break

    else:
        print("Invalid Input Occured! Please write valid input")
