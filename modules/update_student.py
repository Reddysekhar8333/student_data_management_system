from database.db_config import get_connection

def update_student(student_id, new_grade):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET grade = %s WHERE id = %s", (new_grade, student_id))
    conn.commit()
    conn.close()
    print("✅ Student grade updated successfully!")
