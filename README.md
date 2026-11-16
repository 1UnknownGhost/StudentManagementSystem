# Student Management System

## Description

This project is a Python application that connects to a PostgreSQL database to perform CRUD (Create, Read, Update, Delete) operations on student records.

## Technologies Used

- Python 3
- PostgreSQL 18
- pgAdmin 4
- psycopg2

## Database Setup

1. Open pgAdmin 4 and connect to your PostgreSQL server.
2. Create a database named `student_management`.
3. Open the Query Tool for the new database.
4. Open `database/setup.sql` and execute its contents in the Query Tool.
5. Verify that the three initial students were inserted successfully.

## Installation

Make sure Python 3 and PostgreSQL are installed.

Install the required Python library:

python3 -m pip install psycopg2-binary

## Running the Application

1. Open the project folder in VS Code.
2. Open the terminal.
3. Run:

python3 main.py


4. Enter your PostgreSQL password when prompted.

## Application Functions

- **getAllStudents()** — Retrieves and displays all students.
- **addStudent()** — Inserts a new student into the database.
- **updateStudentEmail()** — Updates a student's email address using their student ID.
- **deleteStudent()** — Deletes a student using their student ID.

## Demonstration Video

Video link: https://youtu.be/VnFizWkpJcc?si=l0yxZDceV8-jDAes

## Author

Matin Maroufiazar
Student ID: 101337874
