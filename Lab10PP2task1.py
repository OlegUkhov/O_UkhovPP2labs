import psycopg2
import csv

conn = psycopg2.connect("dbname=postgres user=postgres password=123 host=localhost")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS phonebook (username TEXT, userphone TEXT UNIQUE)""")
conn.commit()

def addFromCsv():
    filename = input("Enter CSV filename: ")
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 2:
                try:
                    cur.execute("INSERT INTO phonebook VALUES (%s, %s)", (row[0], row[1]))
                    print(f"Added: {row[0]}")
                except psycopg2.Error as e:
                    print(f"Error adding {row[0]}: {e}")
    conn.commit()

def addFromConsole():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    try:
        cur.execute("INSERT INTO phonebook VALUES (%s, %s)", (name, phone))
        conn.commit()
        print("Contact added")
    except psycopg2.Error as e:
        print(f"Error: {e}")

def showAll():
    cur.execute("SELECT * FROM phonebook")
    for name, phone in cur.fetchall():
        print(f"{name}: {phone}")

def queryBy():
    print("\nQuery options:")
    print("1. Search by name")
    print("2. Search by phone")
    choice = input("Select query type: ")
    
    if choice == "1":
        prefix = input("Enter name prefix: ")
        cur.execute("SELECT * FROM phonebook WHERE username LIKE %s", (f"{prefix}%",))
    elif choice == "2":
        prefix = input("Enter phone prefix: ")
        cur.execute("SELECT * FROM phonebook WHERE userphone LIKE %s", (f"{prefix}%",))
    else:
        print("Invalid choice")
        return
    
    results = cur.fetchall()
    if not results:
        print("No matches found")
    else:
        for name, phone in results:
            print(f"{name}: {phone}")

def deleteUser():
    print("Delete by:")
    print("1. Name")
    print("2. Phone")
    choice = input("Select option: ")
    
    if choice == "1":
        name = input("Enter name to delete: ")
        cur.execute("DELETE FROM phonebook WHERE username = %s", (name,))
    elif choice == "2":
        phone = input("Enter phone to delete: ")
        cur.execute("DELETE FROM phonebook WHERE userphone = %s", (phone,))
    else:
        print("Invalid choice")
        return
    
    conn.commit()
    print("Deleted successfully")

while True:
    print("\nPhonebook Menu:")
    print("1. Add contacts from CSV")
    print("2. Add contact from console")
    print("3. Show all contacts")
    print("4. Query contacts")
    print("5. Delete contact")
    
    try:
        choice = input("Enter your choice: ")
        
        if choice == "1":
            addFromCsv()
        elif choice == "2":
            addFromConsole()
        elif choice == "3":
            showAll()
        elif choice == "4":
            queryBy()
        elif choice == "5":
            deleteUser()
        else:
            print("Invalid option, try again")
    
    except KeyboardInterrupt:
        print("\nProgram terminated")
        break
    except Exception as e:
        print(f"Error: {e}")

cur.close()
conn.close()