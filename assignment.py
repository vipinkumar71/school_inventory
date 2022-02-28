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
        }

    def display_options(self):
        """ All the display option for the assignment table """
        print("1. See List of Assignments")
        print("2. Add Assignment")
        print("3. Update Assignment")
        print("4. Delete Assignment")

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
