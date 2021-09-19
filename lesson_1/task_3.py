# Написать программу, которая генерирует в указанных пользователем
# границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f',
# то вводятся эти символы. Программа должна вывести на экран любой
# символ алфавита от 'a' до 'f' включительно.

import random
import string
d_for_int = input("Укажите диапазон для чисел через пробел: ")
left, right = d_for_int.split(" ")
left, right = int(left), int(right)
d_for_letters = input("Укажите две буквы через пробел: ")
letter_1, letter_2 = d_for_letters.split(" ")
letter_1_ind = string.ascii_letters.index(letter_1)
letter_2_ind = string.ascii_letters.index(letter_2)
random_int = random.randint(abs(left), abs(right))
random_r = random.uniform(left, right)
random_letter = random.choices(string.ascii_letters[letter_1_ind:letter_2_ind])
print(f"Случайное целое число от {abs(left)} до {abs(right)}: {random_int} \n"
      f"Случайное вещественное число от {left} до {right}: {random_r} \n"
      f"Случайная буква от {letter_1} до {letter_2}: {random_letter}")