# Матрица 5x4 заполняется вводом с клавиатуры,
# кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в последнюю ячейку строки. В конце следует
# вывести полученную матрицу.
matrix = []
while len(matrix) != 5:
    line = []
    matrix.append(line)
    while len(line) != 4:
        num = int(input("Введите число: "))
        line.append(num)
        if len(line) == 3:
            num = sum(line)
            line.append(num)


for i in matrix:
    for j in i:
        print(f"{j: > 4}", end="")
    print()