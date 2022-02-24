"""teacher related CRUD operation"""
import self

from config import get_db_cursor


class Teacher:
    """Utility for teacher table"""
    table = "teacher"

    def __init__(self):
        pass

    def teacher_option_map(self):
        return {
            1: self.get_list,
            2: self.add,
            3: self.update,
            4: self.delete,
            5: self.associate_teacher_by_standard,
            6: self.teacher_standard
        }

    def display_options(self):
        """All the display option for the student table"""
        print("1. See List of teachers")
        print("2. Add teacher")
        print("3. Update teacher")
        print("4. Delete teacher")
        print("5. Update standard of teacher")
        print("6  Get teacher by standard")

        selected_input = int(input("Select option: "))
        if selected_input == 2:
            name = input("Enter student name:")
            self.teacher_option_map().get(selected_input)(name)
        elif selected_input == 3:
            name = input("Enter teacher name:")
            id = input("Enter teacher id:")
            self.teacher_option_map().get(selected_input)(name, id)
        elif selected_input == 4:
            id = input("Enter teacher id:")
            self.teacher_option_map().get(selected_input)(id)
        elif selected_input == 5:
            standard_id = int(input("Enter standard id:"))
            teacher_id = int(input("Enter teacher id:"))
            self.teacher_option_map().get(selected_input)(standard_id, teacher_id)
        elif selected_input == 6:
            standard_id = int(input("Enter standard id:"))
            self.teacher_option_map().get(selected_input)(standard_id)
        else:
            self.teacher_option_map().get(selected_input)()

    """CRUD operations"""

    def get_list(self):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute("SELECT * from teacher")
        for teacher in cursor.fetchall():
            print(f"{teacher[0]}-----{teacher[1]}")

        connection.close()
        print("You got your list")

    def add(self, name):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO  {self.table}(name) VALUES('{name}')")
        connection.commit()
        connection.close()
        print("Successfully added 1 record")

    def update(self, name, id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE {self.table} SET name='{name}' WHERE id={id};")
        connection.commit()
        connection.close()
        print("Successfully updated 1 record")

    def delete(self, id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"DELETE from {self.table} WHERE id={id};")
        connection.commit()
        print("Successfully deleted 1 record")

    def associate_teacher_by_standard(self, standard_id, teacher_id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE {self.table} SET standard_id='{standard_id}' WHERE id='{teacher_id}'")
        connection.commit()
        connection.close()
        print("Successfully updated record")

    def teacher_standard(self, standard_id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {self.table} WHERE standard_id= {standard_id}")
        for teacher in cursor.fetchall():
            print(teacher[1])
        connection.commit()
        connection.close()
        print("Successfully update record")
