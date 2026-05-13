import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
# ============================================================
# 1. ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ
# ============================================================
DB_CONFIG = {
    'host': 'localhost',
    'port': 5434,
    'user': 'postgres_task',
    'password': 'student',
    'database': 'student'
}

print("Подключение к базе данных...")
try:
    conn = psycopg2.connect(**DB_CONFIG)
    print("Подключение успешно")
except Exception as e:
    print(f"Ошибка подключения: {e}")
    exit(1)

# ============================================================
# 2. ИЗВЛЕЧЕНИЕ ДАННЫХ
# ============================================================

# Запрос 1: Средняя цена и количество цен по категориям (для столбчатых диаграмм)
df_categories = pd.read_sql("""
    SELECT
        p.category,
        ROUND(AVG(pr.price)::numeric, 2) AS avg_price,
        COUNT(pr.id) AS price_count
    FROM products p
    JOIN prices pr ON p.id = pr.product_id
    GROUP BY p.category
    ORDER BY avg_price DESC
""", conn)

# Запрос 2: Распределение цен по всем товарам (для гистограммы)
df_prices = pd.read_sql("SELECT price FROM prices", conn)

# Запрос 3: Количество поставщиков по категориям (для круговой диаграммы)
df_suppliers_cat = pd.read_sql("""
    SELECT
        p.category,
        COUNT(s.id) AS supplier_count
    FROM products p
    JOIN suppliers s ON p.id = s.product_id
    GROUP BY p.category
    ORDER BY supplier_count DESC
""", conn)

# Запрос 4: Аномалии — товары, у которых нет ни одного поставщика
df_no_suppliers = pd.read_sql("""
    SELECT
        p.name AS product_name,
        p.category
    FROM products p
    LEFT JOIN suppliers s ON p.id = s.product_id
    WHERE s.id IS NULL
    ORDER BY p.category, p.name
""", conn)

# Запрос 5: Товары с максимальным разбросом цен (для дополнительного вывода)
df_price_range = pd.read_sql("""
    SELECT
        p.name,
        p.category,
        MIN(pr.price) AS min_price,
        MAX(pr.price) AS max_price,
        COUNT(pr.id) AS price_entries
    FROM products p
    JOIN prices pr ON p.id = pr.product_id
    GROUP BY p.id, p.name, p.category
    HAVING COUNT(pr.id) > 1
    ORDER BY (MAX(pr.price) - MIN(pr.price)) DESC
    LIMIT 5
""", conn)

conn.close()
print("Данные загружены\n")

# ============================================================
# 3. ПОДГОТОВКА ДАННЫХ И СТАТИСТИЧЕСКИЕ МЕТРИКИ
# ============================================================
# Статистика цен
mean_price = df_prices['price'].mean()
median_price = df_prices['price'].median()
std_price = df_prices['price'].std()
min_price = df_prices['price'].min()
max_price = df_prices['price'].max()

# Квартили для анализа
q1 = df_prices['price'].quantile(0.25)
q3 = df_prices['price'].quantile(0.75)
iqr = q3 - q1

# ============================================================
# 4. ВИЗУАЛИЗАЦИЯ (4 ГРАФИКА)
# ============================================================
plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "grid.linestyle": "--"
})

fig = plt.figure(figsize=(16, 10))
fig.suptitle("Анализ базы данных товаров", fontsize=16, fontweight="bold", y=1.01)

# Используем GridSpec для гибкого размещения
gs = gridspec.GridSpec(2, 3, figure=fig, height_ratios=[5, 4], width_ratios=[2, 1, 2], hspace=0.45, wspace=0.35)

ax1 = fig.add_subplot(gs[0, 0:2])  # Средняя цена по категориям
ax2 = fig.add_subplot(gs[0, 2])    # Количество поставщиков по категориям
ax3 = fig.add_subplot(gs[1, 0])    # Распределение цен (гистограмма)
ax4 = fig.add_subplot(gs[1, 1:3])  # Количество цен по категориям

# ----------------------------------------------------------------------
# ГРАФИК 1: Горизонтальная столбчатая диаграмма "Средняя цена по категориям"
# Обоснование: горизонтальные столбцы удобны, когда названия категорий длинные.
# ----------------------------------------------------------------------
bars1 = ax1.barh(df_categories['category'], df_categories['avg_price'], color='#4a90d9', edgecolor='white', height=0.6)
for bar, val in zip(bars1, df_categories['avg_price']):
    ax1.text(bar.get_width() + 50, bar.get_y() + bar.get_height()/2, f'{val:,.0f} руб.', va='center', fontsize=9)
ax1.set_xlabel('Средняя цена (руб.)')
ax1.set_title('Средняя цена товаров по категориям', fontweight='bold')
ax1.grid(axis='x')

# ----------------------------------------------------------------------
# ГРАФИК 2: Круговая диаграмма "Количество поставщиков по категориям"
# Обоснование: показывает долю каждого поставщика от общего числа.
# ----------------------------------------------------------------------
total_suppliers = df_suppliers_cat['supplier_count'].sum()
pie_labels = [f"{row.category} ({row.supplier_count} шт.)" for _, row in df_suppliers_cat.iterrows()]
wedges, _, autotexts = ax2.pie(
    df_suppliers_cat['supplier_count'], labels=None, autopct='%1.0f%%',
    colors=['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#ffeaa7'],
    startangle=90, wedgeprops={'edgecolor': 'white', 'linewidth': 1.5}, pctdistance=0.7
)
for autotext in autotexts:
    autotext.set_fontsize(9); autotext.set_fontweight('bold')
ax2.set_title('Распределение поставщиков по категориям', fontweight='bold')
ax2.legend(wedges, pie_labels, loc='lower center', bbox_to_anchor=(0.5, -0.22), fontsize=8, frameon=False)

# ----------------------------------------------------------------------
# ГРАФИК 3: Гистограмма "Распределение цен"
# Обоснование: показывает форму распределения, центральную тенденцию и разброс.
# На этом графике отражены статистические метрики: среднее, медиана, Q1, Q3.
# ----------------------------------------------------------------------
n, bins, patches = ax3.hist(df_prices['price'], bins=20, color='#f0ad4e', edgecolor='white', alpha=0.7)
ax3.axvline(mean_price, color='crimson', linestyle='--', linewidth=1.5, label=f'Среднее: {mean_price:,.0f} руб.')
ax3.axvline(median_price, color='green', linestyle='--', linewidth=1.5, label=f'Медиана: {median_price:,.0f} руб.')
ax3.axvline(q1, color='blue', linestyle=':', linewidth=1.2, alpha=0.7, label=f'Q1 (25%): {q1:,.0f} руб.')
ax3.axvline(q3, color='blue', linestyle=':', linewidth=1.2, alpha=0.7, label=f'Q3 (75%): {q3:,.0f} руб.')
ax3.set_xlabel('Цена (руб.)')
ax3.set_ylabel('Количество товаров')
ax3.set_title('Распределение цен на товары', fontweight='bold')
ax3.legend(fontsize=8)
# Текстовый блок с метриками
stats_text = f"Всего цен: {len(df_prices)}\nСр. откл.: {std_price:,.0f} руб.\nРазмах: {max_price - min_price:,.0f} руб.\nIQR: {iqr:,.0f} руб."
ax3.text(0.95, 0.95, stats_text, transform=ax3.transAxes, va='top', ha='right', fontsize=8,
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# ----------------------------------------------------------------------
# ГРАФИК 4: Вертикальная столбчатая диаграмма "Количество цен по категориям"
# Обоснование: наглядно показывает, для товаров какой категории зафиксировано больше всего цен.
# ----------------------------------------------------------------------
bars4 = ax4.bar(df_categories['category'], df_categories['price_count'], color='#2ecc71', edgecolor='white', width=0.6)
for bar, val in zip(bars4, df_categories['price_count']):
    ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3, str(val), ha='center', fontsize=9)
ax4.set_ylabel('Количество записей о ценах')
ax4.set_title('Количество цен по категориям', fontweight='bold')
ax4.set_xticklabels(df_categories['category'], rotation=40, ha='right', fontsize=8)

# ----------------------------------------------------------------------
# ГЛОБАЛЬНАЯ ПОДПИСЬ ОБ АНОМАЛИЯХ
# ----------------------------------------------------------------------
anomaly_msg = f"✓ Аномалий не обнаружено" if df_no_suppliers.empty else f"⚠ Аномалия: {len(df_no_suppliers)} товаров не имеют поставщиков"
fig.text(0.5, -0.03, anomaly_msg, ha='center', fontsize=10,
         color='green' if df_no_suppliers.empty else '#8b0000',
         bbox=dict(boxstyle='round', facecolor='#f0fff0' if df_no_suppliers.empty else '#fff3f3', edgecolor='green' if df_no_suppliers.empty else '#d9534f'))

# Сохранение и показ
plt.tight_layout()
plt.savefig("store_analysis.png", bbox_inches="tight", dpi=150)
print("✓ График сохранён как store_analysis.png")
plt.show()

# ============================================================
# 5. ВЫВОДЫ ПО ГРАФИКАМ
# ============================================================
print("\n" + "="*70)
print("ВЫВОДЫ ПО ГРАФИКАМ")
print("="*70)

print("\n ГРАФИК «Средняя цена по категориям» (горизонтальная столбчатая диаграмма)")
print(f"   - Самая высокая средняя цена у категории «{df_categories.iloc[0]['category']}»: {df_categories.iloc[0]['avg_price']:,.0f} руб.")
print(f"   - Самая низкая средняя цена у категории «{df_categories.iloc[-1]['category']}»: {df_categories.iloc[-1]['avg_price']:,.0f} руб.")
print("   - Вывод: категория «Электроника» и «Бытовая техника» ожидаемо дороже, чем «Книги» и «Продукты».")
print("   - Обоснование типа: горизонтальные столбцы позволяют легко читать названия категорий.")

print("\n КРУГОВАЯ ДИАГРАММА «Распределение поставщиков по категориям»")
print(f"   - Больше всего поставщиков у категории «{df_suppliers_cat.iloc[0]['category']}»: {df_suppliers_cat.iloc[0]['supplier_count']} шт.")
for _, row in df_suppliers_cat.iterrows():
    print(f"     • {row.category}: {row.supplier_count} поставщиков ({row.supplier_count/total_suppliers*100:.0f}%)")
print("   - Вывод: количество поставщиков коррелирует с количеством товаров в категории.")
print("   - Обоснование типа: круговая диаграмма наглядно показывает доли.")

print("\n ГИСТОГРАММА «Распределение цен» (отражены статистические метрики)")
print(f"   - Средняя цена: {mean_price:,.0f} руб., Медиана: {median_price:,.0f} руб.")
print(f"   - Стандартное отклонение: {std_price:,.0f} руб. — {'большой разброс' if std_price > 10000 else 'разброс небольшой'}.")
print(f"   - 25% товаров стоят дешевле {q1:,.0f} руб., 75% — дешевле {q3:,.0f} руб.")
print(f"   - Межквартильный размах (IQR): {iqr:,.0f} руб.")
print("   - Вывод: распределение скошено вправо (есть дорогие товары, которые тянут среднее вверх).")

print("\n ГРАФИК «Количество цен по категориям» (вертикальная столбчатая диаграмма)")
for _, row in df_categories.iterrows():
    print(f"   - {row.category}: {row.price_count} записей о ценах")
print("   - Вывод: количество цен пропорционально количеству товаров в категории (у всех примерно по 2 цены на товар).")
print("   - Обоснование типа: вертикальные столбцы удобны для сравнения абсолютных значений.")

# ============================================================
# 6. АНОМАЛИИ
# ============================================================
print("\n" + "="*70)
print("ПРОВЕРКА АНОМАЛИЙ")
print("="*70)

if df_no_suppliers.empty:
    print("Аномалий не обнаружено: у всех товаров есть хотя бы один поставщик.")
else:
    print(f"Найдено {len(df_no_suppliers)} товаров, у которых нет поставщиков:")
    for _, row in df_no_suppliers.iterrows():
        print(f"   - {row['product_name']} (категория: {row['category']})")
    print("\n   → Рекомендация: Проверить эти товары вручную или добавить поставщиков.")

if not df_price_range.empty:
    print("\nТовары с максимальным разбросом цен (для дополнительного анализа):")
    for _, row in df_price_range.iterrows():
        print(f"   - {row['name']}: от {row['min_price']:,.0f} до {row['max_price']:,.0f} руб. (разница {row['max_price'] - row['min_price']:,.0f} руб.)")