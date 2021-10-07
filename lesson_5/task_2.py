# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’]
# соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
# Примечание: Если воспользоваться функциями hex() и/или int()
# для преобразования систем счисления, задача решается в несколько строк.
# Для прокачки алгоритмического мышления такой вариант не подходит.
# Поэтому использование встроенных функций для перевода из одной системы
# счисления в другую в данной задаче под запретом.
# Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.

from collections import deque
number_1 = str(input("Введите первое число")).upper()
number_2 = str(input("Введите второе число")).upper()

symbol_string = "ABCDEF"


def hex_n(number):
    hex_num = ''
    while number > 9:
        a = number % 16
        if a <= 9:
            hex_num += str(a)
        else:
            for x, item in enumerate(symbol_string, 10):
                if a == x:
                    hex_num += str(item)
        number = number // 16
        if number <=9 and number > 0:
            hex_num += str(number)
            break
    return hex_num[::-1]


def dex_n(number):
    summ = 0
    len_of_number = len(number)
    while len_of_number > 0:
        for i in range(0, len_of_number):
            a = number[-1]
            if a in symbol_string:
                for k, el in enumerate(symbol_string, 10):
                    if a == el:
                        part_of_summ = k * 16 ** i
                        summ += part_of_summ
            else:
                part_of_summ = int(a) * 16 ** i
                summ += part_of_summ
            number = number[:-1]
            len_of_number -= 1
    return summ


first = dex_n(number_1)
second = dex_n(number_2)


print(f"Сумма чисел {number_1} и {number_2} равна: {deque(hex_n(first + second))}")
print(f"Произведение чисел {number_1} и {number_2} равно: {deque(hex_n(first * second))}")

