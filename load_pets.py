import sqlite3
from sqlite3 import Error

def load_table(db_file):
    conn = sqlite3.connect(db_file)
    with conn:
        cur = conn.cursor()

        persons = (
            (1, 'James', 'Smith', 41),
            (2, 'Diana', 'Greene', 23),
            (3, 'Sara', 'White', 27),
            (4, 'William', 'Gibson', 23)
        )

        pets = (
            (1, 'Rusty', 'Dalmation', 4, 1),
            (2, 'Bella', 'Alaskan Malamute', 3, 0),
            (3, 'Max', 'Cocker Spaniel', 1, 0),
            (4, 'Rocky', 'Beagle', 7, 0),
            (5, 'Rufus', 'Cocker Spaniel', 1, 0),
            (6, 'Spot', 'Bloodhound', 2, 1)
        )

        person_pets = (
            (1, 1),
            (1, 2),
            (2, 3),
            (2, 4),
            (3, 5),
            (4, 6)
        )

        cur.executemany("INSERT INTO person VALUES(?,?,?,?)", persons)
        cur.executemany("INSERT INTO pet VALUES(?,?,?,?,?)", pets)
        cur.executemany("INSERT INTO person_pet VALUES(?,?)", person_pets)

if __name__ == '__main__':
    load_table(r'D:\Coding Projects\IS211_Assignment10\pets.db')