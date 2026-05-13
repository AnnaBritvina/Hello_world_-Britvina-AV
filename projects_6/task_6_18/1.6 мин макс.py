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

# Загружаем данные
df = pd.read_sql("""
    SELECT pr.name, pr.category, p.price
    FROM prices p
    JOIN products pr ON p.product_id = pr.id;
""", conn)

conn.close()

# Группировка по товарам и расчёт статистик
price_stats = df.groupby(['name', 'category'])['price'].agg([
    ('min_price', 'min'),
    ('max_price', 'max')
]).round(2)

# Расчёт разницы между максимальной и минимальной ценой
price_stats['price_range'] = price_stats['max_price'] - price_stats['min_price']

# Сортировка по убыванию разброса и выбор топ-5
top_5_range = price_stats.sort_values('price_range', ascending=False).head(5)

print("\n=== ТОП-5 ТОВАРОВ С НАИБОЛЬШИМ РАЗБРОСОМ ЦЕН ===")
print("=" * 80)
print(f"{'Название товара':<35} {'Категория':<18} {'Мин.цена':<12} {'Макс.цена':<12} {'Разброс':<12}")
print("=" * 80)

for (name, category), row in top_5_range.iterrows():
    print(f"{name:<35} {category:<18} {row['min_price']:<12.2f} {row['max_price']:<12.2f} {row['price_range']:<12.2f}")

print("=" * 80)