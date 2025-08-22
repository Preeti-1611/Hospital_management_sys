import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="system_nursing",
        port=3306  # <-- added this line
    )

