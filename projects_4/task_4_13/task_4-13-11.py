N = int(input("Введите количество элементов массива N: "))
A = []
print("Введите элементы массива:")
for i in range(N):
    a_i = float(input(f"A[{i}] = "))
    A.append(a_i)
sum = 0
i = 0
count = 0
while i < N:
    if i % 2 == 0:
        sum = sum + A[i]
        count = count + 1
    i = i + 1
if count > 0:
    average = sum / count
print(f"Среднее арифметическое элементов с чётными индексами: {average}")