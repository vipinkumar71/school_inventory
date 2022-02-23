"""
Student relate CRUD Operation in this file
"""
import self as self

from config import get_db_cursor


class Student:
    """Utility for students"""
    table = "student"

    def __init__(self):
        pass

    def student_map_return(self):
        return {
            1: self.get_list,
            2: self.add
        }

    def display_options(self):
        """ All the display option for the student table """
        print("1. See List of students")
        print("2. Add Student")
        print("3. Update student")
        print("4. Delete student")
        selected_input = int(input("Select option: "))
        if selected_input == 2:
            name = input("Enter student name")
            self.student_map_return().get(selected_input)(name)
        else:
            self.student_map_return().get(selected_input)()

    def get_list(self):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute("SELECT * from student")
        for student in cursor.fetchall():
            print(f"{student[0]}-----{student[1]}")
        connection.close()

    def add(self, name):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO  {self.table}(name) VALUES('{name}')")
        connection.commit()
        connection.close()
        print("Successfully added 1 record")

