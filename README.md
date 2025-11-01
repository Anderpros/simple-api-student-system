# simple-api-student-system
System Integration Assignment 3, by Leonard Marveli B. IS 2022

A simple RESTful API built using **Flask** for managing student records.  
This project is made for **System Integration – Assignment 3**.

---

## Features
- Retrieve all students  
- Add new student  
- Update student details  
- Delete student record

## API Endpoints (Method /Endpoint → Description)
- GET /students           → Retrieve all student records
- GET /students/<id>      → Retrieve a specific student record by ID
- POST /students          → Add a new student record
- PUT /students/<id>      → Update an existing student record
- DELETE /students/<id>   → Delete a student record

## Setup Instructions
1. Clone the repository \
   git clone https://github.com/Anderpros/simple-api-student-system.git \
   cd simple-api-student-system

2. Install dependencies \
   pip install flask

3. Run the app \
   python app.py

4. The server runs at \
   http://127.0.0.1:5000

## Example API Calls (via cURL)
1. Get all students \
   curl -i http://127.0.0.1:5000/students
   
2. Add a new student \
   curl -i -X POST -H "Content-Type: application/json" \
   -d '{"name": "Justin", "major": "Business", "gpa": 3.9}' \
   http://127.0.0.1:5000/students
   
3. Update student \
   curl -i -X PUT -H "Content-Type: application/json" \
   -d '{"major": "Data Science"}' \
   http://127.0.0.1:5000/students/1
   
4. Delete student \
   curl -i -X DELETE http://127.0.0.1:5000/students/2

## Limitations
- Data is not saved permanently; restarting the server will reset all student records.
- No user authentication or access control is implemented.
- This API is for educational and prototyping purposes only, not for production use.
