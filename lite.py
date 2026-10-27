import sqlite3

conn = sqlite3.connect("college.db")

try:
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET marks = ? WHERE roll_no = ?",
        (88, 101)
    )
    conn.commit()
    print("Transaction successful")

except sqlite3.Error:
    conn.rollback()
    print("Transaction failed")

finally:
    conn.close()