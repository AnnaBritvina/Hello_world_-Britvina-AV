N = int(input("Введите количество элементов массива N: "))
A = []
print("Введите элементы массива:")
for i in range(N):
    a_i = float(input(f"A[{i}] = "))
    A.append(a_i)
count = 0
i = 0
while i < N:
    if A[i] > 0:
        count = count + 1
    i = i + 1
print(f"Количество положительных чисел в массиве: {count}")