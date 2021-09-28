# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
from random import randint, shuffle
numbers = list(set([randint(5, 20) for i in range(10)]))
shuffle(numbers)
print(numbers)
max_el = numbers[0]
min_el = numbers[0]
for i in numbers:
    if i > max_el:
        max_el = i
    if i < min_el:
        min_el = i

small_index = numbers.index(min_el)
big_index = numbers.index(max_el)

if small_index < big_index:
    numbers_2 = numbers[small_index + 1:big_index]
    print(numbers_2)
    print(sum(numbers_2))
else:
    numbers_2 = numbers[big_index + 1:small_index]
    print(numbers_2)
    print(sum(numbers_2))