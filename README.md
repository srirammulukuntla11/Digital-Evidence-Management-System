# Evidence Management System (EMS)

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange)

A sophisticated Database Management System (DBMS) Project developed for **B.Tech IARE**. 
The Evidence Management System is a web-based platform tailored for securely adding, managing, and tracking case files and digital evidence. It simplifies the administrative processes of law enforcement or legal entities by establishing a secure correlation between specific cases and critical evidence files using hash values.

## ✨ Features

- **Case Management:** Create new case entries with a title, detailed description, and current status.
- **Evidence Management:** Upload and link crucial evidence details securely to a specific case utilizing a robust referencing system.
- **Data Integrations via Hashes:** Securely record file paths and compute hash values for data integrity verification of the evidence.
- **Relational Operations:** Employs standard relational database operations linking Case IDs to Evidence tables (One-to-Many).
- **Web Interface:** User-friendly and responsive front-end implemented via HTML/CSS templates to smoothly navigate between cases and evidence insertions.

## 🛠️ Technology Stack

- **Backend Platform:** Python 3, Flask Web Framework
- **Database:** MySQL
- **Database Driver:** `mysql-connector-python`
- **Frontend / Client-side:** HTML5, CSS3, Jinja2 Templating
- **Architecture Base:** MVC (Model-View-Controller) pattern

## 📋 Prerequisites

Before running this project, ensure you have the following installed on your system:

- [Python 3.8+](https://www.python.org/downloads/)
- [MySQL Server](https://dev.mysql.com/downloads/installer/) installed and running locally.
- A virtual environment (recommended).

## 🚀 Setup & Installation Instructions

Follow these steps to configure and run the Evidence Management Server on your local machine:

### 1. Clone or Download the Directory
Navigate to the root directory of the project on your machine.
```bash
cd evidence_management_system
```

### 2. Install Required Python Packages
It is highly recommended to isolate the environment. Then install Flask and the MySQL connector:
```bash
pip install Flask mysql-connector-python
```

### 3. Database Configuration
Open the MySQL command line client or use a GUI tool like MySQL Workbench and set up your database schema. 

Execute the following SQL queries to initialize your `cases` and `evidence` tables:

```sql
-- Create database
CREATE DATABASE evidence_db;
USE evidence_db;

-- Create 'cases' table
CREATE TABLE cases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(50) NOT NULL
);

-- Create 'evidence' table
CREATE TABLE evidence (
    evidence_id INT AUTO_INCREMENT PRIMARY KEY,
    case_id INT,
    file_path TEXT NOT NULL,
    hash_value VARCHAR(256),
    FOREIGN KEY (case_id) REFERENCES cases(id) ON DELETE CASCADE
);
```

### 4. Configure Application Variables
Open the `app.py` file, find the database connection section, and update it with your MySQL credentials:

```python
# DB Connection in app.py
db = mysql.connector.connect(
    host="localhost",
    user="root",          # Your MySQL username
    password="sriram@11", # Insert your MySQL password here
    database="evidence_db"
)
```

### 5. Start the Application
Run the Flask application from your terminal:
```bash
python app.py
```
The server should start running at `http://127.0.0.1:5000/`. You can navigate to it using your web browser.

## 🗂️ Project Structure

```text
evidence_management_system/
│
├── app.py                # Main Flask application and API route controller
├── database.sql          # Structured queries for DBMS table creation
├── README.md             # Project documentation
│
├── static/               # Assets (CSS styling, images, JS scripts)
│   └── ...
│
└── templates/            # HTML structural Jinja2 templates
    ├── index.html        # Main dashboard
    ├── add_case.html     # Case creation view
    ├── view_cases.html   # Cases list interface
    └── add_evidence.html # Evidence creation / linking view
```

## 🔐 Future Enhancements (Roadmap)

To elevate this project, the following features are planned for future iterations:
- [ ] User Authentication & Authorization (Admin/Viewer permissions)
- [ ] Automated cryptographic hash generation of uploaded files (SHA-256)
- [ ] Direct file attachments/uploads rather than just file paths
- [ ] Advanced searching capabilities by Case Status or Hash signatures

## 🎓 Academic Credit

Developed as an academic **DBMS Project** for **B.Tech program at IARE**.
