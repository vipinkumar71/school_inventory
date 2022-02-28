"""
Entrypoint for the project
"""
from standard import Standard
from student import Student
from teacher import Teacher
from assignment import Assignment

OPTIONS_MAP = {
    1: Student().display_options,
    2: Teacher().display_options,
    3: Standard().display_options,
    4: Assignment().display_options
}


def display_options():
    """options in the system """
    print("welcome to school Inventory System")
    print("Select your option")
    print("1. Student")
    print("2. Teacher")
    print("3. Standard")
    print("4. Assignment")


def option_router():
    """routes option according to the input"""
    selected_option = int(input("Enter your option:"))
    return OPTIONS_MAP.get(selected_option)()


if __name__ == '__main__':
    display_options()
    option_router()
