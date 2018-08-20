import sqlite3


connection = None
file_path = "sqlite/live.db"


def get_connection():
    return sqlite3.connect(file_path)


def close_connection():
    global connection

    if connection is not None:
        connection.close()

    connection = None

