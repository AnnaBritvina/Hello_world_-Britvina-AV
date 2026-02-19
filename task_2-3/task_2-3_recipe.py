breed_ground = input("Введите название питательной среды ")
concentr = input("Введите концентрацию агара (%) ")
temp = input("Введите температуру стерилизации ")
with open("recipe.txt", "w", encoding="utf-8") as report:
    report.write(f"Введите название питательной среды:\t{breed_ground}\n")
    report.write(f"Введите концентрацию агара (%):\t{concentr}\n")
    report.write(f"Введите температуру стерилизации (°C):\t{temp}\n")

print("Файл 'recipe.txt' успешно сформирован!")