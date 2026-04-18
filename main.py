import psycopg2
import pandas as pd

# 1. CONNESSIONE
conn = psycopg2.connect(
    dbname="sales_analysis",
    user="postgres",
    password="Inter2307!",
    port="5433"
)

cur = conn.cursor()

# CREATE TABLE
with open("sql/create_tables.sql", "r", encoding="utf-8") as f:
    cur.execute(f.read())

conn.commit()

# INSERT DATA
with open("sql/insert_data.sql", "r", encoding="utf-8") as f:
    cur.execute(f.read())

conn.commit()

cur.close()

#QUERY DATA

def run_query(sql_query):
    return pd.read_sql(sql_query, conn)

# 1. utenti per paese
query1 = """
SELECT country, COUNT(*) AS total_users
FROM users
GROUP BY country;
"""
print(run_query(query1))

# 2. vendite totali
query2 = """
SELECT SUM(total_amount) AS total_sales
FROM orders;
"""
print(run_query(query2))

# 3. spesa per utente
query3 = """
SELECT u.name, SUM(o.total_amount) AS total_spent
FROM users u
JOIN orders o ON u.user_id = o.user_id
GROUP BY u.name
ORDER BY total_spent DESC;
"""
print(run_query(query3))

# 4. prodotti più venduti
query4 = """
SELECT p.product_name, SUM(oi.quantity) AS total_sold
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC;
"""
print(run_query(query4))

# 5. top cliente
query5 = """
SELECT u.name, SUM(o.total_amount) AS total_spent
FROM users u
JOIN orders o ON u.user_id = o.user_id
GROUP BY u.name
ORDER BY total_spent DESC
LIMIT 1;
"""
print(run_query(query5))

# 6. vendite mensili
query6 = """
SELECT DATE_TRUNC('month', order_date) AS month,
       SUM(total_amount) AS revenue
FROM orders
GROUP BY month
ORDER BY month;
"""
print(run_query(query6))

# 7. clienti ricorrenti
query7 = """
SELECT user_id, COUNT(order_id) AS num_orders
FROM orders
GROUP BY user_id
HAVING COUNT(order_id) > 1;
"""
print(run_query(query7))

# 8. ranking clienti
query8 = """
SELECT u.name,
       SUM(o.total_amount) AS total_spent,
       RANK() OVER (ORDER BY SUM(o.total_amount) DESC) AS ranking
FROM users u
JOIN orders o ON u.user_id = o.user_id
GROUP BY u.name;
"""
print(run_query(query8))

# 4. CHIUSURA
conn.close()