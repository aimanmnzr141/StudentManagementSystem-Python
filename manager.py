# From student.py, Student class is being imported
from student import Student


class StudentManager:

    def __init__(self):  # Constructor for the manager
        # Creates an empty list that stores the data of all the student objects.
        # Container where many student objects will be kept
        self.students = []

    def add_student(self):  # Self represent the current student manager object
        student_id = int(input("Enter student id: "))
        name = input("Enter student name: ")
        age = int(input("Enter student age :"))
        course = input("Enter student course: ")
        email = input("Enter student email: ")

        # Created object of Student class
        new_student = Student(student_id, name, age, course, email)
        # Adds the new student to the manager list
        self.students.append(new_student)

        print("Student added successfully!")

    def view_students(self):  # Defining the view method
        # Check if the List is empty
        if not self.students:
            print("No Student Found!")
            return

        print("The list of students are: \n")
        for current_student in self.students:
            print(f"id: {current_student.student_id}")
            print(f"name: {current_student.name}")
            print(f"age: {current_student.age}")
            print(f"course: {current_student.course}")
            print(f"email: {current_student.email}")

            print("-" * 30)  # Separator

    def search_student(self):  # Defining search method
        search_id = int(input("Enter student id: "))
        for search_student in self.students:
            if search_student.student_id == search_id:  # Comparing the id
                print("Student Found! ")
                print(f"id: {search_student.student_id}")
                print(f"name: {search_student.name}")
                print(f"age: {search_student.age}")
                print(f"course: {search_student.course}")
                print(f"email: {search_student.email}")
                return

        print("Sorry! Student not found")

    def update_student(self) # Defining update method
        # Asking user to enter the student id they want to update.
        update_id = int(input("Enter student id you want to update:")) # input stored in variable update_id
        # Loop through self.students
        for update_student in self.students:  
            if update_student.student_id == update_id: # Comparing the id
                print("Student Found!")
                update_student.student_id = int(input("Enter New id:")) # Taking input from user and updating accordingly
                update_student.name = input("Enter New Name: ")
                update_student.age = int(input("Enter New Age: "))
                update_student.course = input("Enter New Course : ")
                update_student.email = input("Enter New Email: ")
                print("Student updated successfully!")
                return
        print("Sorry! Student not found")

    def delete_student(self): # Defining Delete Method
        # Getting student id that user wants to delete
        delete_id = int(input("Enter id that you want to delete :"))
        for del_student in self.students:
            if del_student.student_id == delete_id: #Compare each students ID with delete_id
                self.students.remove(del_student)
                print("Student Deleted Successfully!")
                return
        print("Sorry! Student not found")




