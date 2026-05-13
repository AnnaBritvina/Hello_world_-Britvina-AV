import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5434",
    user="postgres_task",
    password="student",
    database="student"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM products LIMIT 3;")

for row in cursor.fetchall():
    print(row)

conn.close()