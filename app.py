from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# DB Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sriram@11",   # 🔴 change this
    database="evidence_db"
)

cursor = db.cursor()

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Add Case
@app.route('/add_case', methods=['GET', 'POST'])
def add_case():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        status = request.form['status']

        cursor.execute(
            "INSERT INTO cases (title, description, status) VALUES (%s, %s, %s)",
            (title, description, status)
        )
        db.commit()
        return redirect('/view_cases')

    return render_template('add_case.html')

# View Cases
@app.route('/view_cases')
def view_cases():
    cursor.execute("SELECT * FROM cases")
    data = cursor.fetchall()
    return render_template('view_cases.html', cases=data)

# Add Evidence
@app.route('/add_evidence', methods=['GET', 'POST'])
def add_evidence():
    if request.method == 'POST':
        case_id = request.form['case_id']
        file_path = request.form['file_path']
        hash_value = request.form['hash_value']

        cursor.execute(
            "INSERT INTO evidence (case_id, file_path, hash_value) VALUES (%s, %s, %s)",
            (case_id, file_path, hash_value)
        )
        db.commit()
        return redirect('/')

    return render_template('add_evidence.html')

if __name__ == '__main__':
    app.run(debug=True)