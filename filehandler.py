# The main responsibility of file handler file is to read/write data to students.json
# Importing JSON - as we are working with JSON
import json

# Importing Student class from student module
from student import Student

# This funtion is used to save students into students.json
# object->dictionary->JSON


def save_student(students):
    student_data = []  # Creating an empty list to store

    # Loop through each student object in students list
    for student in students:
        # Converting data
        student_data.append(
            {
                "student_id": student.student_id,
                "name": student.name,
                "age": student.age,
                "course": student.course,
                "email": student.email,
            }
        )
    try:
        with open("student.json", "w") as file:
            json.dump(student_data, file, indent=4)

    except Exception as e:
        print(f"Error while saving file {e}")


# Function to load data from students.json
# JSON->dictionary->objects


def load_students(students):  # created a function that loads student data
    # With automatically closes the file
    # Opened student.json in read mode
    with open("student.json", "r") as file:
        student_data = json.load(file)  # Converts json data into python object

    return student_data
