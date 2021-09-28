# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.
from random import randint
numbers = [randint(1, 10) for i in range(15)]
print(numbers)
min_el = numbers[0]
for i in numbers:
    if i < min_el:
        min_el = i

count = numbers.count(min_el)
if count > 1:
    print(f"Числa {min_el} и {min_el} является минимальными в списке")
else:
    numbers.remove(min_el)
    min_el_2 = numbers[0]
    for i in numbers:
        if i < min_el_2:
            min_el_2 = i
    print(f"Числа {min_el} и {min_el_2} являются минимальными в списке")

