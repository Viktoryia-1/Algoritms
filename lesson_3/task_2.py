# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5
# (помните, что индексация начинается с нуля), т. к.
# именно в этих позициях первого массива стоят четные числа.
import random
numbers = [i for i in range(-10, 10)]
random.shuffle(numbers)
print(numbers)
index_list = []
for i in numbers:
    if i % 2 == 0:
        index_list.append(numbers.index(i))

print(index_list)