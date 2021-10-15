# Массив размером 2m + 1, где m — натуральное число,
# заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.

from random import shuffle, randint
from numpy import median
m = int(input("Введите число: "))
n = 2 * m + 1
array = [randint(1, 100) for i in range(n)]
shuffle(array)
print(array)


def median_m(array):
    if len(array) == 1:
        return int(array[0])
    max_el = max(array)
    min_el = min(array)
    for el in array:
        if el < max_el and el > min_el:
            med_el = el
            array.remove(max_el)
            array.remove(min_el)
            return median_m(array)


print(f"Медана списка {median_m(array)}")

# Проверяем
print(median(array))