import psycopg2

import pandas as pd

try:

    # Устанавливаем соединение

    connection = psycopg2.connect(
        host="localhost",          # База в контейнере, но доступна через localhost
        port="5434",               # Порт из секции ports
        user="postgres_task",           # POSTGRES_USER
        password="student",        # POSTGRES_PASSWORD
        database="student"          # POSTGRES_DB
    )
    print("✓ Подключение установлено")

except Exception as error:

    print(f"Ошибка при подключении: {error}")

# SQL-запрос с использованием JOIN
sql_query = """
SELECT 
    pr.price, 
    p.name AS product_name, 
    p.category
FROM 
    prices pr
JOIN 
    products p ON pr.product_id = p.id;
"""

# Загрузка результата в pandas DataFrame
try:
    df = pd.read_sql_query(sql_query, connection)
    print("Данные успешно загружены.")
    print(df.head(200))  # Вывод первых 5 строк для проверки
except Exception as e:
    print(f"Ошибка выполнения запроса: {e}")