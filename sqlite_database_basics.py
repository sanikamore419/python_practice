# sqlite_database_basics.py
# Basic CRUD operations using SQLite in Python

import sqlite3

# -------------------------------
# 1. CONNECT TO DATABASE
# -------------------------------
# Creates database file if not exists
conn = sqlite3.connect("sample.db")
cursor = conn.cursor()

# -------------------------------
# 2. CREATE TABLE
# -------------------------------
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        course TEXT
    )
""")
conn.commit()
print("Table created successfully!\n")

# -------------------------------
# 3. INSERT DATA
# -------------------------------
def insert_student(name, age, course):
    cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", 
                   (name, age, course))
    conn.commit()
    print(f"Inserted: {name}")

insert_student("Sanika", 20, "Computer Science")
insert_student("Aarav", 21, "Mechanical")
insert_student("Riya", 19, "AI & DS")

# -------------------------------
# 4. READ DATA (SELECT)
# -------------------------------
def fetch_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    print("\n------ Student Records ------")
    for row in rows:
        print(row)
    print("-----------------------------\n")

fetch_students()

# -------------------------------
# 5. UPDATE DATA
# -------------------------------
def update_student(student_id, new_course):
    cursor.execute("UPDATE students SET course = ? WHERE id = ?", 
                   (new_course, student_id))
    conn.commit()
    print(f"Updated student {student_id} to course {new_course}")

update_student(1, "Data Science")
fetch_students()

# -------------------------------
# 6. DELETE DATA
# -------------------------------
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print(f"Deleted student with ID = {student_id}")

delete_student(2)
fetch_students()

# -------------------------------
# 7. CLOSE CONNECTION
# -------------------------------
conn.close()
print("Database connection closed!")
