from database.db_config import get_connection

def add_student(name, age, course, grade):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students (name, age, course, grade) VALUES (%s, %s, %s, %s)",
        (name, age, course, grade)
    )
    conn.commit()
    conn.close()
    print(" Student added successfully!")
