import psycopg2
import pandas as pd

# Подключение к базе данных
conn = psycopg2.connect(
    host="localhost",
    port="5434",
    user="postgres_task",
    password="student",
    database="student"
)

# Загружаем данные с ценой и категорией
df = pd.read_sql("""
    SELECT p.price, pr.name, pr.category 
    FROM prices p
    JOIN products pr ON p.product_id = pr.id;
""", conn)

conn.close()

# Расчёт квартилей
q1 = df['price'].quantile(0.25)
q2 = df['price'].quantile(0.50)
q3 = df['price'].quantile(0.75)
iqr = q3 - q1

print("=== Квартили цен (руб.) ===")
print(f"Q1  (25%): {q1:.2f} руб.")
print(f"Q2  (50%): {q2:.2f} руб.")
print(f"Q3  (75%): {q3:.2f} руб.")
print(f"IQR (Q3-Q1): {iqr:.2f} руб.")

# Вывод товаров с ценой выше Q3
print("\n=== Товары с ценой выше Q3 (дорогие) ===")
high_prices = df[df['price'] > q3]
print(f"Найдено товаров: {len(high_prices)}")
print("\nСписок:")
for idx, row in high_prices.iterrows():
    print(f"  {row['name']:35} | {row['category']:20} | {row['price']:.2f} руб.")