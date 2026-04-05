N = int(input("Введите количество натуральных чисел N: "))
sum = 0
i = 1
while i <= N:
    sum = sum + i
    i = i + 1
print(f"Сумма первых {N} натуральных чисел = {sum}")