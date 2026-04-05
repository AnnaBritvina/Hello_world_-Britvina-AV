N = int(input("Введите количество элементов массива N: "))
A = []
print("Введите элементы массива:")
for i in range(N):
    a_i = float(input(f"A[{i}] = "))
    A.append(a_i)
sum = 0
i = 0
while i < N:
    if i % 2 != 0:
        sum = sum + A[i]
    i = i + 1
print(f"Сумма элементов с нечётными индексами: {sum}")