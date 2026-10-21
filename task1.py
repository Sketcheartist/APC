
from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)
DB_NAME = "students.db"

# Create the database and table
def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            batch TEXT NOT NULL,
            contact TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


# HTML webpage
HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Details</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef2f7;
            padding: 30px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 25px;
            border-radius: 12px;
            box-shadow: 0 4px 12px #cccccc;
        }
        h1, h2 {
            text-align: center;
            color: #234b75;
        }
        input {
            width: 100%;
            padding: 10px;
            margin: 8px 0 15px;
            box-sizing: border-box;
            border: 1px solid #bbb;
            border-radius: 5px;
        }
        button {
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            color: white;
            cursor: pointer;
            margin-right: 8px;
        }
        .submit-btn { background: #167d4a; }
        .read-btn { background: #1769aa; }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        th, td {
            border: 1px solid #ccc;
            padding: 9px;
            text-align: left;
            overflow-wrap: anywhere;
        }
        th { background: #dce9f7; }
        .message { color: #167d4a; }
    </style>
</head>
<body>
<div class="container">
    <h1>Student Details Form</h1>

    <form method="POST" action="/">
        <label>Student Name</label>
        <input type="text" name="name"
               placeholder="Enter student name" required>

        <label>Batch</label>
        <input type="text" name="batch"
               placeholder="Enter batch" required>

        <label>Contact Number</label>
        <input type="tel" name="contact"
               placeholder="Enter contact number" required>

        <label>Email</label>
        <input type="email" name="email"
               placeholder="Enter email address" required>

        <button class="submit-btn" type="submit">
            Submit
        </button>

        <button class="read-btn" type="button"
                onclick="window.location.href='/read'">
            Read
        </button>
    </form>

    {% if message %}
        <p class="message">{{ message }}</p>
    {% endif %}

    {% if students is not none %}
        <h2>Submitted Student Data</h2>

        {% if students %}
        <table>
            <tr>
                <th>Name</th>
                <th>Batch</th>
                <th>Contact</th>
                <th>Email</th>
            </tr>
            {% for student in students %}
            <tr>
                <td>{{ student[0] }}</td>
                <td>{{ student[1] }}</td>
                <td>{{ student[2] }}</td>
                <td>{{ student[3] }}</td>
            </tr>
            {% endfor %}
        </table>
        {% else %}
            <p>No student records found.</p>
        {% endif %}
    {% endif %}
</div>
</body>
</html>
"""


# Display the form and save submitted data
@app.route("/", methods=["GET", "POST"])
def home():
    message = None

    if request.method == "POST":
        name = request.form["name"].strip()
        batch = request.form["batch"].strip()
        contact = request.form["contact"].strip()
        email = request.form["email"].strip()

        if not all([name, batch, contact, email]):
            return "All fields are required.", 400

        conn = sqlite3.connect(DB_NAME)
        conn.execute(
            "INSERT INTO students (name, batch, contact, email) "
            "VALUES (?, ?, ?, ?)",
            (name, batch, contact, email)
        )
        conn.commit()
        conn.close()

        message = "Student details submitted successfully!"

    return render_template_string(
        HTML, message=message, students=None
    )


# Read and display all submitted records
@app.route("/read")
def read():
    conn = sqlite3.connect(DB_NAME)
    students = conn.execute(
        "SELECT name, batch, contact, email "
        "FROM students ORDER BY id DESC"
    ).fetchall()
    conn.close()

    return render_template_string(
        HTML, message=None, students=students
    )


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
