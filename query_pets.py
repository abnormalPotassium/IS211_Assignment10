import sqlite3
from sqlite3 import Error

def query_schema(db_file):
    conn = sqlite3.connect(db_file)
    with conn:
        
        cur = conn.cursor()
        
        while True:
            try:
                ID = input('Please provide the person\'s ID number ')
                int(ID)
            except ValueError:
                print('This isn\'t a number. If you want to exit, enter \'-1\'')
                continue
            if int(ID) == -1:
                raise SystemExit
            elif int(ID) < -1:
                print('There aren\'t any negative IDs')
                continue
            else:
                try:
                    cur.execute("""
                        SELECT person.first_name, person.last_name, person.age, pet.name, pet.breed, pet.age, pet.dead
                        FROM person 
                        INNER JOIN person_pet ON person.id = person_pet.person_id
                        INNER JOIN pet ON person_pet.pet_id = pet.id
                        WHERE person.id=?""",ID)
                    rows = cur.fetchall()
                    if not rows:
                        print('Someone with this ID does not exist!')
                        continue
                    for row in rows:
                        if int(row[5]) == 1:
                            print(f'{row[0]} {row[1]}, {row[2]} years old, owned {row[3]}, a {row[4]}, that was {row[5]} years old :(')
                        else:
                            print(f'{row[0]} {row[1]}, {row[2]} years old, owns {row[3]}, a {row[4]}, that is {row[5]} years old :)')
                except Error as e:
                    print(e)

if __name__ == '__main__':
    query_schema(r'D:\Coding Projects\IS211_Assignment10\pets.db')