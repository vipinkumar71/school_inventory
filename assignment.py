"""
Assignment related CRUD Operation in this file
"""

from config import get_db_cursor


class Assignment:
    """Utility for assignment"""
    table = "assignment"

    def __init__(self):
        pass

    def assignment_option_map(self):
        return {
            1: self.get_list,
            2: self.add,
            3: self.update,
            4: self.delete,
            5: self.get_assignment_by_teacher,
            6: self.get_assignment_by_standard,
            7: self.get_assignment_by_student
        }

    def display_options(self):
        """ All the display option for the assignment table """
        print("1. See List of Assignments")
        print("2. Add Assignment")
        print("3. Update Assignment")
        print("4. Delete Assignment")
        print("5 Get assignment by standard")
        print("6.Get assignment by teacher ")
        print("7. Get assignment by student")

        selected_input = int(input("Select option: "))
        if selected_input == 2:
            assignment_name = input("Enter Assignment name:")
            standard_id = int(input("Enter standard id:"))
            teacher_id = int(input("Enter teacher id:"))
            student_id = int(input("Enter student id:"))
            self.assignment_option_map().get(selected_input)(assignment_name, standard_id, teacher_id, student_id)
        elif selected_input == 3:
            assignment_name = input("Enter Assignment name:")
            id = int(input("Enter Assignment id:"))
            self.assignment_option_map().get(selected_input)(assignment_name, id)
        elif selected_input == 4:
            id = int(input("Enter Assignment id:"))
            self.assignment_option_map().get(selected_input)(id)
        elif selected_input == 5:
            standard_id = int(input("Enter standard id:"))
            self.assignment_option_map().get(selected_input)(standard_id)
        elif selected_input == 6:
            teacher_id = int(input("Enter teacher id:"))
            self.assignment_option_map().get(selected_input)(teacher_id)
        elif selected_input == 7:
            student_id = int(input("Enter student id:"))
            self.assignment_option_map().get(selected_input)(student_id)
        else:
            self.assignment_option_map().get(selected_input)()

    """CRUD OPERATIONS"""

    def get_list(self):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * from {self.table}")
        for assignment in cursor.fetchall():
            print(f"{assignment[0]}-----{assignment[1]}")
        connection.close()
        print("You got your list")

    def add(self, assignment_name, standard_id, teacher_id, student_id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO  {self.table}(assignment_name,standard_id,teacher_id,student_id) "
                       f"VALUES('{assignment_name}',{standard_id},{teacher_id},{student_id});")
        connection.commit()
        connection.close()
        print("Successfully added 1 record")

    def update(self, assignment_name, id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE {self.table} SET assignment_name ='{assignment_name}' WHERE id ={id};")
        connection.commit()
        connection.close()
        print("Successfully Updated 1 record")

    def delete(self, id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"DELETE from {self.table} WHERE id={id};")
        connection.commit()
        connection.close()
        print("Successfully Delete 1 record")

    def get_assignment_by_standard(self, standard_id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table} WHERE standard_id= {standard_id}")
        for standard in cursor.fetchall():
            print(standard[1])
        connection.commit()
        connection.close()
        print("Successfully update record")

    def get_assignment_by_teacher(self, teacher_id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table} WHERE teacher_id= {teacher_id}")
        for teacher in cursor.fetchall():
            print(teacher[1])
        connection.commit()
        connection.close()
        print("Successfully updated record")

    def get_assignment_by_student(self, student_id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table} WHERE student_id= {student_id}")
        for student in cursor.fetchall():
            print(student[1])
        connection.commit()
        connection.close()
        print("Successfully update record")
