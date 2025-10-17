CREATE DATABASE IF NOT EXISTS student_db;
USE student_db;

CREATE TABLE IF NOT EXISTS students (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(40),
    age INT,
    course VARCHAR(50),
    grade VARCHAR(10) 
);