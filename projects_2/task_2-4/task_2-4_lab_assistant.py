volume = float(input("Введите нужный объем раствора (в мл): "))
salt_mass = volume * 0.009
with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write("ОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n -----------------------\n")
    file.write(f"Общий объем:\t {volume} мл\nМасса соли:\t {salt_mass:.2f} г\nОбъем воды: \t {volume} мл\n")