import psycopg2
import csv

conn = psycopg2.connect("dbname=post user=postgres password=123 host=localhost")
cur = conn.cursor()

def insertUser():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    try:
        cur.execute("CALL upsert_user_by_name(%s, %s)", (name, phone))
        conn.commit()
        print("User added or phone updated")
    except Exception as e:
        conn.rollback()
        print("Error:", e)

def manyInsertCSV():
    filename = input("Enter CSV filename: ")
    try:
        cur.execute("TRUNCATE TABLE temp_invalid_phones;")
        
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    name, phone = row[0].strip(), row[1].strip()
                    try:
                        cur.execute("CALL upsert_user_by_name(%s, %s)", (name, phone))
                    except Exception as e:
                        print(f"Error processing {name}, {phone}: {e}")
                        conn.rollback()
                        continue
        
        conn.commit()
        print("All data processed.")
        cur.execute("SELECT name, phone FROM temp_invalid_phones") 
        invalid = cur.fetchall()
        if invalid:
            print("\nInvalid phone numbers:")
            for row in invalid:
                print(f"Name: {row[0]}, Phone: {row[1]}")
    except Exception as e:
        conn.rollback()
        print("Error:", e)

def patternSearch():
    pattern = input("Enter search pattern: ")
    cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    results = cur.fetchall()
    for row in results:
        print(row)

def paginate():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    cur.execute("SELECT * FROM paginate_phonebook(%s, %s)", (limit, offset))
    results = cur.fetchall()
    for row in results:
        print(row)

def userDelete():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    try:
        cur.execute("CALL delete_user(%s, %s)", (name if name else None, phone if phone else None))
        conn.commit()
        print("Deleted.")
    except Exception as e:
        print("Error:", e)

def showAll():
    cur.execute("SELECT username, userphone FROM phonebook ORDER BY username ASC")
    for row in cur.fetchall():
        print(row)

while True:
    print("""
1. Insert user
2. Insert Many Users from CSV
3. Search by Pattern
4. Pagination
5. Delete User
6. Show All
""")
    choice = input("Choose option: ")
    if choice == "1":
        insertUser()
    elif choice == "2":
        manyInsertCSV()
    elif choice == "3":
        patternSearch()
    elif choice == "4":
        paginate()
    elif choice == "5":
        userDelete()
    elif choice == "6":
        showAll()
    else:
        print("Invalid choice")
