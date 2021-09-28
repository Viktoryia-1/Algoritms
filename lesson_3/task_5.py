# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
import random
numbers = [random.randint(-20, 20) for i in range(15)]
print(numbers)

minus_numbers = [i for i in numbers if i < 0]
if len(minus_numbers) > 0:
    min_max_el = minus_numbers[0]
    for i in minus_numbers:
        if i > min_max_el:
            min_max_el = i
    print(f"Максимальный отрицательный элемент : {min_max_el}, "
          f"это {numbers.index(min_max_el) + 1} позиция в списке")
else:
    print("Массив не содержит отрицательных чисел")