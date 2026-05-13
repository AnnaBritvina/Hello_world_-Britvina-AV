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

# Загружаем данные в DataFrame
df = pd.read_sql("SELECT price FROM prices;", conn)

# Закрываем соединение
conn.close()

# Выводим статистику
print("=== describe() ===")
print(df['price'].describe().round(2))

# Дополнительно выводим с единицами измерения
print("\n=== Статистика цен (руб.) ===")
stats = df['price'].describe().round(2)
print(f"  count   : {stats['count']:.0f} шт.")
print(f"  mean    : {stats['mean']:.2f} руб.")
print(f"  std     : {stats['std']:.2f} руб.")
print(f"  min     : {stats['min']:.2f} руб.")
print(f"  25%     : {stats['25%']:.2f} руб.")
print(f"  50%     : {stats['50%']:.2f} руб.")
print(f"  75%     : {stats['75%']:.2f} руб.")
print(f"  max     : {stats['max']:.2f} руб.")