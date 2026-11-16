import psycopg2
import getpass

# Ask for the PostgreSQL password securely
password = getpass.getpass("Enter PostgreSQL password: ")

# Connect to our PostgreSQL database
connection = psycopg2.connect(
    host="localhost",
    database="student_management",
    user="postgres",
    password=password,
    port="5432"
)

print("Successfully connected to PostgreSQL!")

# Retrieve and display all students from the database
def getAllStudents():
    cursor = connection.cursor()

    # Retrieve every student from the students table
    cursor.execute("SELECT * FROM students ORDER BY student_id")

    students = cursor.fetchall()

    # Display each student's information
    for student in students:
        print(student)

    cursor.close()

# Add a new student to the PostgreSQL database
def addStudent(first_name, last_name, email, enrollment_date):
    cursor = connection.cursor()

    # Insert a new student using the provided information
    cursor.execute(
        """
        INSERT INTO students
        (first_name, last_name, email, enrollment_date)
        VALUES (%s, %s, %s, %s)
        """,
        (first_name, last_name, email, enrollment_date)
    )

    # Save the changes to the database
    connection.commit()

    print("Student added successfully!")

    # Close the cursor
    cursor.close()

# Update a student's email address using their student ID
def updateStudentEmail(student_id, new_email):
    cursor = connection.cursor()

    # Find the student by ID and update their email
    cursor.execute(
        """
        UPDATE students
        SET email = %s
        WHERE student_id = %s
        """,
        (new_email, student_id)
    )

    # Save the changes to the database
    connection.commit()

    print("Student email updated successfully!")

    # Close the cursor
    cursor.close()

# Delete a student from the database using their student ID
def deleteStudent(student_id):
    cursor = connection.cursor()

    # Delete the student with the specified ID
    cursor.execute(
        """
        DELETE FROM students
        WHERE student_id = %s
        """,
        (student_id,)
    )

    # Save the deletion permanently
    connection.commit()

    print("Student deleted successfully!")

    # Close the cursor
    cursor.close()

# Display the application menu
while True:
    print("\n===== Student Management System =====")
    print("1. View All Students")
    print("2. Add Student")
    print("3. Update Student Email")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        getAllStudents()

    elif choice == "2":
        first_name = input("First name: ")
        last_name = input("Last name: ")
        email = input("Email: ")
        enrollment_date = input("Enrollment date (YYYY-MM-DD): ")

        addStudent(first_name, last_name, email, enrollment_date)

    elif choice == "3":
        student_id = int(input("Student ID: "))
        new_email = input("New email: ")

        updateStudentEmail(student_id, new_email)

    elif choice == "4":
        student_id = int(input("Student ID: "))

        deleteStudent(student_id)

    elif choice == "5":
        print("Exiting application...")
        break

    else:
        print("Invalid choice. Please try again.")

# Close the database connection when finished
connection.close()