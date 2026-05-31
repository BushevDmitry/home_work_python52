"""Задача 1"""

CREATE TABLE books (
id INT PRIMARY KEY,
title TEXT NOT NULL,
author TEXT,
year INT,
pages int
)


INSERT INTO books (id, title, author, year, pages)
VALUES
(1, 'Преступление и наказание', 'Достоевский Ф.М.', 1866, 600),
(2, 'Бесы' , 'Достоевский Ф.М.', 1872, 550),
(3, 'Белая гвардия', 'Булгаков М.А.', 1925, 525),
(4, 'Вишневый сад', 'Чехов А.П.', 1904, 100),
(5, 'Отцы и дети', 'Тургенев И.С.', 1862, 250);

SELECT * FROM books






"""Задача 2"""

CREATE TABLE products(
id INT PRIMARY KEY,
name TEXT UNIQUE,
price FLOAT,
category VARCHAR(20) DEFAULT 'Разное',
is_aviable BOOLEAN
)

INSERT INTO products(id, name, price, category, is_aviable)
VALUES
(1, 'Кока-Кола', 120.99, 'Напитки', TRUE),
(2, 'Квас', 110.99, 'Напитки', TRUE),
(3, 'Макароны', 80.99, 'Бакалея', FALSE),
(4, 'Зубачистки', 30.99, DEFAULT, TRUE);

SELECT * from products

