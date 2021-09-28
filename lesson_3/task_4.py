# Определить, какое число в массиве встречается чаще всего.
import random
numbers = [random.randint(2, 9) for i in range(10)]

print(numbers)
count_numbers = 0
number = 0

for el in set(numbers):
    a = numbers.count(el)
    if a > count_numbers:
        count_numbers = a
        number = el
print(f"Число {number} втречается в данном списке {count_numbers} раз")





