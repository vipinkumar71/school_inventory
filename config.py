"""
All the project related configuration will be related in this file
"""
import mysql.connector

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "bumblebee@71"
MYSQL_DATABASE = "db_school"


def get_db_cursor():
    connection = mysql.connector.connect(
        host=MYSQL_HOST, username=MYSQL_USER, passwrod=MYSQL_PASSWORD, database=MYSQL_DATABASE
    )
