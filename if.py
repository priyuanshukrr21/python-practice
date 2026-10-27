import sqlite3

# Connect to the database
conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        roll_no INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        marks REAL
    )
""")

# Insert a record safely
cursor.execute(
    "INSERT OR REPLACE INTO students VALUES (?, ?, ?)",
    (101, "Aman", 85)
)

# Save changes
conn.commit()

# Read records
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection
conn.close()