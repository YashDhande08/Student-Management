import sqlite3

def create_connection():
    conn = sqlite3.connect('students.db')
    return conn


import mysql.connector

def create_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",        # Replace with your MySQL server host
            user="root",    # Replace with your MySQL username
            password="dhande@143",# Replace with your MySQL password
            database="attendance" # Replace with your database name
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def create_table():
    conn = create_connection()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            age INT NOT NULL,
            gender ENUM('Male', 'Female', 'Other') NOT NULL,
            course VARCHAR(255) NOT NULL
        )
        ''')
        conn.commit()
        conn.close()


def add_student(name, age, gender, course):
    conn = create_connection()
    if conn is None:
        print("Failed to connect to the database.")
        return
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO students (name, age, gender, course) VALUES (%s, %s, %s, %s)
    ''', (name, age, gender, course))
    conn.commit()
    conn.close()



def get_all_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    conn.close()
    return students


def update_student(student_id, name, age, gender, course):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
    UPDATE students
    SET name = ?, age = ?, gender = ?, course = ?
    WHERE id = ?
    ''', (name, age, gender, course, student_id))
    conn.commit()
    conn.close()


def delete_student(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
