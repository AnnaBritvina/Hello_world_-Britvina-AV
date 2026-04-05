N = int(input("Введите число N для вычисления факториала: "))
i = 1
factorial = 1
while i <= N:
    factorial = factorial * i
    i = i + 1
print(f"Факториал числа {N}! = {factorial}")