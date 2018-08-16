import sqlite3
import os


connection = None
file_path = "data/test.db"


def get_connection():
    global connection

    if connection is None:
        connection = sqlite3.connect(file_path)

    return connection


def close_connection():
    global connection

    if connection is not None:
        connection.close()

    connection = None


def destroy():
    os.remove(file_path)