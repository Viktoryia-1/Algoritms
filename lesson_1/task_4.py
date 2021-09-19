# 4. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят,
# и сколько между ними находится букв.
import string
letters = input("Введите две буквы через пробел: ")
letters = letters.lower()
letter_1, letter_2 = letters.split(' ')
if letter_1 and letter_2 in string.ascii_lowercase:
    num_1 = string.ascii_letters.index(letter_1) + 1
    num_2 = string.ascii_letters.index(letter_2) + 1
    letters_between = abs(num_1 - num_2) - 1
    print(f"Буква {letter_1} на {num_1} месте,\n"
        f"Буква {letter_2} на {num_2} месте \n"
        f"Количество букв между ними {letters_between}")