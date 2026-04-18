-- utenti per paese
SELECT country, COUNT(*) AS total_users
FROM users
GROUP BY country;

-- vendite totali
SELECT SUM(total_amount) AS total_sales
FROM orders;

-- spesa per utente
SELECT u.name, SUM(o.total_amount) AS total_spent
FROM users u
JOIN orders o ON u.user_id = o.user_id
GROUP BY u.name;

-- prodotti più venduti
SELECT p.product_name, SUM(oi.quantity) AS total_sold
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_name;