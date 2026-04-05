N = int(input("Введите количество элементов массива N: "))
A = []
print("Введите элементы массива:")
for i in range(N):
    a_i = float(input(f"A[{i}] = "))
    A.append(a_i)
i = 0
sum = 0
while i < N:
    sum = sum + A[i]
    i = i + 1
average = sum / N
print(f"Среднее арифметическое элементов массива: {average}")