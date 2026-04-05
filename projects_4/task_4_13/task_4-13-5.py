N = int(input("Введите количество чисел N: "))
a1 = float(input("Введите число 1: "))
max_value = a1
i = 2
while i <= N:
    a_i = float(input(f"Введите число {i}: "))
    if a_i > max_value:
        max_value = a_i
    i = i + 1
print(f"Максимальное из {N} введенных чисел: {max_value}")