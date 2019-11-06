import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()

def define_table(db_file):
    conn = sqlite3.connect(db_file)
    with conn:
        cur = conn.cursor()

        cur.execute('CREATE TABLE person(id INT PRIMARY KEY, first_name TEXT, last_name TEXT, age INT)')
        cur.execute('CREATE TABLE pet(id INT PRIMARY KEY, name TEXT, breed TEXT, age INT, dead INT)')
        cur.execute('CREATE TABLE person_pet(person_id INT, pet_id INT)')

if __name__ == '__main__':
    create_connection(r'D:\Coding Projects\IS211_Assignment10\pets.db')
    define_table(r'D:\Coding Projects\IS211_Assignment10\pets.db')