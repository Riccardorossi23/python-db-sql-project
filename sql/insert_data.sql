INSERT INTO users (name, email, signup_date, country) VALUES
('Luca', 'luca@email.com', '2023-01-10', 'Italy'),
('Anna', 'anna@email.com', '2023-02-15', 'Italy'),
('John', 'john@email.com', '2023-03-20', 'USA');

INSERT INTO products (product_name, category, price) VALUES
('Laptop', 'Electronics', 1200),
('Phone', 'Electronics', 800),
('Shoes', 'Fashion', 100);

INSERT INTO orders (user_id, order_date, total_amount) VALUES
(1, '2023-04-01', 1300),
(2, '2023-04-02', 800),
(1, '2023-04-10', 100);

INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1, 1, 1, 1200),
(1, 3, 1, 100),
(2, 2, 1, 800),
(3, 3, 1, 100);