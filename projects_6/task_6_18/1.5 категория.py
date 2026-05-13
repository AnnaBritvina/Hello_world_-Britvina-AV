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

# Загружаем данные с категориями и ценами
df = pd.read_sql("""
    SELECT pr.category, p.price
    FROM prices p
    JOIN products pr ON p.product_id = pr.id;
""", conn)

conn.close()

# Группировка и расчёт статистик
stats = df.groupby('category')['price'].agg([
    ('count', 'count'),
    ('mean', 'mean'),
    ('median', 'median'),
    ('std', 'std')
]).round(2)

# Сортировка по убыванию средней цены
stats = stats.sort_values('mean', ascending=False)

# Вывод результатов
print("\n=== Статистика цен по категориям ===")
print("=" * 70)
print(f"{'Категория':<20} {'Кол-во':<8} {'Средняя':<12} {'Медиана':<12} {'Ст.откл.':<12}")
print("=" * 70)

for category, row in stats.iterrows():
    print(f"{category:<20} {row['count']:<8.0f} {row['mean']:<12.2f} {row['median']:<12.2f} {row['std']:<12.2f}")

print("=" * 70)