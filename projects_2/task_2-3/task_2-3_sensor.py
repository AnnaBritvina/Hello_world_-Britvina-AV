oper_name = input("Введите имя оператора: ")
pressure_sens = input("Введите текущее значение датчика давления: ")
with open("sensor_log.txt", "w", encoding="utf-8") as report:
    report.write(f"Введите имя оператора:\t{oper_name}\n")
    report.write(f"Введите текущее значение датчика давления::\t{pressure_sens}\n")
print("Данные успешно сохранены в sensor_log.txt")