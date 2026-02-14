capsule = float(input("Введите общее количество произведенных капсул: "))
capacity = float(input("Введите количество капсул в одной упаковке: "))
full = capsule // capacity
overtime = capsule % capacity
print(f"Введите общее количество произведенных капсул: {capsule}")
print(f"Введите количество капсул в одной упаковке: {capacity}\n")
print("--- Отчет фасовочного цеха ---")
print(f"Полных упаковок:\t {full}")
print(f"Остаток капсул:\t {overtime}")
