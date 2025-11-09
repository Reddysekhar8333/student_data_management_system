# Student Data Management System

A Python-based console application for efficient student record management using MySQL database.

## 🚀 Features

- **Add Student**: Insert new student records
- **View All Students**: Display all records in formatted table
- **Search Student**: Find students by ID
- **Update Student**: Modify existing records
- **Delete Student**: Remove student records
- **MySQL Integration**: Secure and scalable data storage

## 🛠️ Tech Stack

- **Python** - Core application logic
- **MySQL** - Database management
- **mysql-connector-python** - Database connectivity

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/Reddysekhar8333/student_data_management_system.git
cd student_data_management_system
```
2. **Install dependencies**
```bash
pip install mysql-connector-python
```
3. **Database Setup**

* Create MySQL database: ```student_management```

* Update connection details in the script:

```python
mydb = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="student_management"
)
```
## 🎯 Usage

Run the application:

```bash
python student_management.py
```
Menu Options:

* Add Student

* View All Students

* Search Student

* Update Student

* Delete Student

* Exit

## 🗃️ Database Schema
```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    grade VARCHAR(10),
    email VARCHAR(100)
);
```
## 👨‍💻 Author
SOMPALLI REDDYSEKHAR

GitHub: https://github.com/Reddysekhar8333

phone: 8333958264
