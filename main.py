"Задача 1"
SELECT * FROM orders WHERE ship_country LIKE 'U%';

"Задача 2"
SELECT
    order_id,
    customer_id,
    freight,
    ship_country
FROM orders
WHERE ship_country LIKE 'N%'
ORDER BY freight DESC
LIMIT 10;

"Задача 3"
SELECT first_name, last_name, home_phone FROM employees WHERE region IS NULL;

"Задача 4"
SELECT COUNT(*)
FROM customers
WHERE region IS NOT NULL;

"Задача 5"
SELECT country, COUNT(*) FROM suppliers GROUP BY country ORDER BY supplier_count DESC;


"Задача 6"
SELECT
    ship_country,
    SUM(freight)
FROM orders
WHERE region IS NOT NULL
GROUP BY ship_country
HAVING SUM(freight) > 2750
ORDER BY total_freight DESC;

"Задача 7"
SELECT country
FROM customers
UNION
SELECT country
FROM suppliers
ORDER BY country ASC;

"Задача 8"
SELECT country FROM customers INTERSECT SELECT country FROM suppliers INTERSECT SELECT country FROM employees ORDER BY country ASC;

"Задача 9"
SELECT country
FROM customers
INTERSECT
SELECT country
FROM suppliers
EXCEPT
SELECT country
FROM employees
ORDER BY country ASC;
