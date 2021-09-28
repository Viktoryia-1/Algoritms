# Найти максимальный элемент среди
# минимальных элементов столбцов матрицы.
import random
matrix = [[random.randint(0, 9) for i in range(5)] for el in range(4)]
for i in matrix:
    print(i)

print("*" * 15)
mim_sum = matrix[0]
print(mim_sum)
for i in matrix:
    for j, item in enumerate(i):
        if mim_sum[j] > item:
            mim_sum[j] = item

print("*" * 15)

print(mim_sum)

max_el = mim_sum[0]
for i in mim_sum:
    if i > max_el:
        max_el = i

print(f"Максимальный из минимальных элементов столбцов данной матрицы: {max_el} ")
