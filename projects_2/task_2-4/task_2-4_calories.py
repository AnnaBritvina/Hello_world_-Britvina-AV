protein = float(input("Введите массу белков в продукте: "))
fat = float(input("Введите массу жиров в продукте: "))
carbohydrates = float(input("Введите массу углеводов в продукте: "))

kal = (protein * 4) + (fat * 9) + (carbohydrates * 4)


print(f"Общая калорийность продукта:\t {kal}")