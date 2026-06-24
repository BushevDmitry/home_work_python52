"Задача 1"
SELECT * FROM customers;

"Задача 2""
SELECT contact_name, city FROM customers;

"Задача 3"

SELECT order_id, (shipped_date - order_date) AS delivery_lead_time  FROM orders;

"Задача 4"

SELECT DISTINCT name FROM city;

"Задача 5"

SELECT DISTINCT city, country FROM address;

"Задача 6"

SELECT COUNT(customers) FROM address;

"Задача 7"
SELECT COUNT(DISTINCT country) FROM address;

"Задача 8"
SELECT *
FROM orders
WHERE ship_country IN ('France', 'Austria', 'Spain');

"Задача 9"
SELECT * FROM orders ORDER BY required_date DESC, shipped_date ASC;

"Задача 10"

SELECT MIN(unit_price) AS min_price FROM products WHERE units_in_stock > 30;

"Задача 11"
SELECT MAX(units_in_stock) AS max_units FROM products WHERE unit_price > 30;

"Задача 12""

SELECT AVG(shipped_date - order_date) FROM orders WHERE ship_country = 'USA';

"Задача 13"
SELECT SUM(units_in_stock * unit_price) FROM products WHERE discontinued = 0;
