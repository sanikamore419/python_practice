# sqlite_advanced.py
# Advanced SQL Operations using SQLite

import sqlite3

# Connect to database
conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# -------------------------------------------
# 1. CREATE TABLES WITH FOREIGN KEY
# -------------------------------------------
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
CREATE TABLE IF NOT EXISTS departments (
    dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
    dept_name TEXT UNIQUE NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    dept_id INTEGER,
    marks INTEGER,
    FOREIGN KEY(dept_id) REFERENCES departments(dept_id)
)
""")

conn.commit()
print("Tables created successfully!\n")

# -------------------------------------------
# 2. INSERT DATA INTO departments
# -------------------------------------------

departments = [("Computer Science",), ("Mechanical",), ("AI & DS",)]

cursor.executemany("INSERT OR IGNORE INTO departments (dept_name) VALUES (?)", departments)
conn.commit()

# -------------------------------------------
# 3. INSERT DATA INTO students
# -------------------------------------------
students = [
    ("Sanika", 20, 1, 89),
    ("Aarav", 21, 2, 76),
    ("Riya", 19, 3, 92),
    ("Mohan", 22, 1, 67),
    ("Priya", 20, 3, 85),
]

cursor.executemany(
    "INSERT INTO students (name, age, dept_id, marks) VALUES (?, ?, ?, ?)",
    students
)
conn.commit()


# -------------------------------------------
# 4. WHERE CLAUSE (Filter results)
# -------------------------------------------
print("Students with marks > 80:")
cursor.execute("SELECT name, marks FROM students WHERE marks > 80")
for row in cursor.fetchall():
    print(row)
print()


# -------------------------------------------
# 5. ORDER BY (Sort results)
# -------------------------------------------
print("Students sorted by marks (descending):")
cursor.execute("SELECT name, marks FROM students ORDER BY marks DESC")
for row in cursor.fetchall():
    print(row)
print()


# -------------------------------------------
# 6. LIMIT (Fetch top N records)
# -------------------------------------------
print("Top 3 scorers:")
cursor.execute("SELECT name, marks FROM students ORDER BY marks DESC LIMIT 3")
for row in cursor.fetchall():
    print(row)
print()


# -------------------------------------------
# 7. JOIN (Combine data from two tables)
# -------------------------------------------
print("Students with their department names:")
cursor.execute("""
SELECT students.name, departments.dept_name, students.marks
FROM students
JOIN departments ON students.dept_id = departments.dept_id
""")
for row in cursor.fetchall():
    print(row)
print()


# -------------------------------------------
# 8. GROUP BY (Aggregate functions)
# -------------------------------------------
print("Average marks by department:")
cursor.execute("""
SELECT departments.dept_name, AVG(students.marks)
FROM students
JOIN departments ON students.dept_id = departments.dept_id
GROUP BY departments.dept_name
""")
for row in cursor.fetchall():
    print(row)
print()


# -------------------------------------------
# 9. UPDATE with condition
# -------------------------------------------
cursor.execute("UPDATE students SET marks = marks + 5 WHERE dept_id = 1")
conn.commit()
print("After giving grace marks to CS dept students:")
cursor.execute("SELECT name, marks FROM students WHERE dept_id = 1")
for row in cursor.fetchall():
    print(row)
print()


# -------------------------------------------
# 10. DELETE with condition
# -------------------------------------------
cursor.execute("DELETE FROM students WHERE marks < 70")
conn.commit()
print("Students after deleting those with marks < 70:")
cursor.execute("SELECT name, marks FROM students")
for row in cursor.fetchall():
    print(row)
print()


# Close Connection
conn.close()
print("Database operations completed!")
