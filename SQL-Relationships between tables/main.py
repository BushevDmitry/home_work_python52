"""Задача 1"""

-- CREATE TABLE author(
-- id INT PRIMARY KEY,
-- name TEXT,
-- country TEXT)




-- CREATE TABLE books (
-- id INT PRIMARY KEY,
-- title TEXT,
-- year INT,
-- author_id INT,
-- FOREIGN KEY (author_id) REFERENCES author(id) ON DELETE CASCADE)

-- INSERT INTO author (id, name, country) VALUES
-- (1, 'Лев Толстой', 'Россия'),
-- (2, 'Джордж Оруэлл', 'Великобритания'),
-- (3, 'Франц Кафка', 'Чехия');


-- INSERT INTO books (id, title, year, author_id) VALUES
-- (1, 'Война и мир', 1869, 1),
-- (2, 'Анна Каренина', 1877, 1),
-- (3, '1984', 1949, 2),
-- (4, 'Скотный двор', 1945, 2),
-- (5, 'Процесс', 1925, 3);



-- DELETE FROM author WHERE id=1

-- SELECT * FROM books







""" Задача 2 """

-- CREATE TABLE categories(
-- id INT PRIMARY KEY,
-- name TEXT
-- )

-- CREATE TABLE products(
-- id INT PRIMARY KEY,
-- name TEXT,
-- price INT,
-- category_id INT,
-- FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE SET NULL
-- )


-- INSERT INTO categories VALUES (1, 'Напитки');

-- INSERT INTO products VALUES (1, 'Квас', 110, 1);

-- DELETE FROM categories WHERE id = 1;

-- SELECT * FROM products;




""" Задача 3"""
-- CREATE TABLE users (
-- id INT PRIMARY KEY,
-- email text,
-- password text
-- )

-- CREATE TABLE user_profiles(
-- user_id INT UNIQUE,
-- full_name TEXT,
-- bio TEXT,
-- avatar TEXT,
-- FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
-- )

-- INSERT INTO users (id, email, password)
-- VALUES (1, 'stepanov@mail.ru', 'qwerty');

-- INSERT INTO user_profiles (user_id, full_name, bio, avatar)
-- VALUES (1, 'Степан Степанов', 'Плавание', 'avatar.jpg')

-- SELECT * FROM users

-- INSERT INTO user_profiles (user_id, full_name, bio, avatar)
-- VALUES (1, 'Иван Иванов', 'Фотография', 'avatar2.jpg');






"""Задача 4"""
-- CREATE TABLE students(
-- 	id INT PRIMARY KEY,
-- 	name VARCHAR(50)
-- )


-- CREATE TABLE courses(
-- 	id INT PRIMARY KEY,
-- 	title VARCHAR(50)
-- )

-- CREATE TABLE enrollments (
-- 	student_id INT,
-- 	course_id INT,
-- 	enrolled_at DATE,
-- 	PRIMARY KEY (student_id, course_id),
-- 	FOREIGN KEY (student_id) REFERENCES students(id),
-- 	FOREIGN KEY (course_id) REFERENCES courses(id)
-- );


-- INSERT INTO students
-- VALUES
-- (1,'Иван Иванов'),
-- (2,'Степан Степанов'),
-- (3,'Виктория Викторова');


-- INSERT INTO courses
-- VALUES
-- (1,'SQL'),
-- (2,'Python'),
-- (3,'Java');


-- INSERT INTO enrollments
-- VALUES
-- (1, 1, '2025-04-02'),
-- (1, 2, '2024-03-05'),
-- (1, 3, '2026-05-01')

-- INSERT INTO enrollments
-- VALUES
-- (2, 1, '2025-10-07'),
-- (2, 3, '2026-08-02')

-- INSERT INTO enrollments VALUES
-- (3, 2, '2025-04-02')

-- SELECT * FROM enrollments




"""Задача 5"""

CREATE TABLE employees(
id INTEGER PRIMARY KEY,
name TEXT,
position INT,
manager_id INTEGER REFERENCES employees(id) ON DELETE SET NULL
);