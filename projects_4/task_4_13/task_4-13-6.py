N = int(input("Введите количество чисел N: "))
sum_squares = 0
i = 1
while i <= N:
    sum_squares = sum_squares + (i ** 2)
    i = i + 1
print(f"Сумма квадратов первых {N} натуральных чисел = {sum_squares}")