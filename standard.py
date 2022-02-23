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
            2: self.add
        }

    def display_options(self, standard_name=None):
        """All the display option for the standard table"""
        print("1. See List of standard")
        print("2. Add standard")
        print("3. Update standard")
        print("4. Delete standard")

        selected_input = int(input("Select option: "))
        if selected_input == 2:
            standard_name = input("Enter standard name:")
            self.standard_map_return().get(selected_input)(standard_name)
        else:
            self.standard_map_return().get(selected_input)()

    def get_list(self):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute("SELECT * from standard")
        for standard in cursor.fetchall():
            print(f"{standard[0]}-----{standard[1]}")

        connection.close()

    def add(self, standard_name):
        connection = get_db_cursor()
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO {self.table}(standard_name) VALUES('{standard_name}')")
        connection.commit()
        connection.close()
