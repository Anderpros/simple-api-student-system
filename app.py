from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
students = {
    "1": {"name": "Leonard Bartolomeus", "major": "Information Systems", "gpa": 3.8},
    "2": {"name": "Dillon", "major": "Management", "gpa": 3.9}
}

# GET all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students), 200

# GET a single student by ID
@app.route('/students/<id>', methods=['GET'])
def get_student(id):
    if id in students:
        return jsonify(students[id]), 200
    return jsonify({"error": "Student not found"}), 404

# POST new student
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_id = str(len(students) + 1)
    students[new_id] = {
        "name": data.get("name"),
        "major": data.get("major"),
        "gpa": data.get("gpa")
    }
    return jsonify({"message": "Student added", "id": new_id}), 201

# PUT update student
@app.route('/students/<id>', methods=['PUT'])
def update_student(id):
    if id not in students:
        return jsonify({"error": "Student not found"}), 404
    data = request.get_json()
    students[id].update(data)
    return jsonify({"message": "Student updated"}), 200

# DELETE student
@app.route('/students/<id>', methods=['DELETE'])
def delete_student(id):
    if id in students:
        del students[id]
        return jsonify({"message": f"Student {id} deleted successfully"}), 200
    return jsonify({"error": "Student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
