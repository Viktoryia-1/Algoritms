# В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.

import random
numbers = [i for i in range(10)]
random.shuffle(numbers)
print(numbers)
min_el = numbers[0]
max_el = numbers[0]
for el in numbers:
    if el > max_el:
        max_el = el
    if el < min_el:
        min_el = el

a, b = numbers.index(max_el), numbers.index(min_el)

numbers.insert(a, min_el)
numbers.pop(a+1)
numbers.insert(b, max_el)
numbers.pop(b+1)
print(numbers)

