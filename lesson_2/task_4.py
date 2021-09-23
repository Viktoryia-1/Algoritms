# Найти сумму n элементов следующего ряда чисел:
# 1, -0.5, 0.25, -0.125,… Количество элементов(n)
# вводится с клавиатуры

num = int(input("Введите целое число: "))
sum_num = 0
start = 1
num_row = []
while num != 0:
    sum_num += start
    num_row.append(start)
    step = start * - 0.5
    num -= 1
    start = step

print(f"Сумма числового ряда {num_row} равна {sum_num}")