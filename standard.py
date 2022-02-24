"""teacher related CRUD operation """
from config import get_db_cursor


class Standard:
    """Utility for standard table"""

    table = "standard"

    def __init__(self):
        pass

    def standard_map_return(self):
        return {
            1: self.get_list,
            2: self.add,
            3: self.update,
            4: self.delete,

        }

    def display_options(self):
        """All the display option for the standard table"""
        print("1. See List of standard")
        print("2. Add standard")
        print("3. Update standard")
        print("4. Delete standard")
        print("5. Update standard of student")
        print("6. Get student by standard")
        selected_input = int(input("Select option: "))
        if selected_input == 2:
            standard_name = input("Enter standard name:")
            self.standard_map_return().get(selected_input)(standard_name)
        elif selected_input == 3:
            standard_name = input("Enter standard name:")
            id = input("Enter standard id:")
            self.standard_map_return().get(selected_input)(standard_name, id)
        elif selected_input == 4:
            id = input("Enter standard id:")
            self.standard_map_return().get(selected_input)(id)

        else:
            self.standard_map_return().get(selected_input)()

    """ get_list method we can find list of the standard table"""

    def get_list(self):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute("SELECT * from standard")
        for standard in cursor.fetchall():
            print(f"{standard[0]}-----{standard[1]}")
        connection.close()
        print("You got your list")

    """Using the add method we can add in standard table"""

    def add(self, standard_name):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO {self.table}(standard_name) VALUES('{standard_name}')")
        connection.commit()
        connection.close()
        print("Successfully added 1 record")

        """by using the update method we can update the standard table"""

    def update(self, standard_name, id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"UPDATE {self.table} SET standard_name='{standard_name}' WHERE id={id};")
        connection.commit()
        connection.close()
        print("Successfully Updated 1 record")

    """by using the delete method we can delete the value from standard table"""

    def delete(self, id):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"DELETE from {self.table} WHERE id={id};")
        connection.commit()
        connection.close()
        print("Successfully Deleted 1 record")

