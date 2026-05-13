import psycopg2

import pandas as pd

try:

    # Устанавливаем соединение

    connection = psycopg2.connect(
        host="localhost",          # База в контейнере, но доступна через localhost
        port="5432",               # Поорт из секции ports
        user="postgres",           # POSTGRES_USER
        password="example",        # POSTGRES_PASSWORD
        database="testdb"          # POSTGRES_DB
    )
    query = "SELECT * FROM enrollments"

    df = pd.read_sql(query, connection)
    print(df.head(10))
    print(df.info())


except Exception as error:
    print(f"Ошибка при подключении: {error}")