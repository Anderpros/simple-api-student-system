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
1. Get all students (using Git Bash) \
   curl -i http://127.0.0.1:5000/students \
   **Result:** \
   <img width="302" height="344" alt="image" src="https://github.com/user-attachments/assets/fb25b24f-f7c1-436a-8da9-1f444dc3eea9" />

   
2. Add a new student \
   curl -i -X POST -H "Content-Type: application/json" \
   -d '{"name": "Justin", "major": "Business", "gpa": 3.9}' \
   http://127.0.0.1:5000/students \
   **Result:** \
   <img width="577" height="230" alt="image" src="https://github.com/user-attachments/assets/56679593-c9ed-4cd4-9f45-1f2d13bccf1f" /> \
   **Updated Data:** \
   <img width="258" height="299" alt="image" src="https://github.com/user-attachments/assets/3204e774-b70e-4584-8269-00cf3f499ff0" />
   
3. Update student \
   curl -i -X PUT -H "Content-Type: application/json" \
   -d '{"major": "Data Science"}' \
   http://127.0.0.1:5000/students/1 \
   **Result:** \
   <img width="664" height="210" alt="image" src="https://github.com/user-attachments/assets/db3eb60f-780a-4024-a940-64028ad1e399" /> \
   **Updated Data:** \
   <img width="246" height="302" alt="image" src="https://github.com/user-attachments/assets/b5cfeab7-bcbe-48b1-92a9-baaa11d8da55" />
   
4. Delete student \
   curl -i -X DELETE http://127.0.0.1:5000/students/2 \
   **Result:** \
   <img width="394" height="194" alt="image" src="https://github.com/user-attachments/assets/e199da69-b588-45b4-8fa6-2fc611b6062e" /> \
   **Updated Data:** \
   <img width="249" height="212" alt="image" src="https://github.com/user-attachments/assets/82eb9c5b-0bc3-403a-8ad6-d81f294b9625" />

## Limitations
- Data is not saved permanently; restarting the server will reset all student records.
- No user authentication or access control is implemented.
- This API is for educational and prototyping purposes only, not for production use.
