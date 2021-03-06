# Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным
# использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;


# Сформировать из введенного числа обратное по порядку
# входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843
import sys

def sum_memory(objects):
    sum_mem = 0
    for el in objects:
        sum_mem += sys.getsizeof(objects[el])
    return sum_mem

# print(sys.version)
# print(sys.platform)
# 3.9.2 (v3.9.2:1a79785e3e, Feb 19 2021, 09:06:10)
# [Clang 6.0 (clang-600.0.57)]
# darwin


def show_sizeof(x, size_count=0):
    size_count += sys.getsizeof(x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                for k, v in x.items():
                    show_sizeof(k)
                    show_sizeof(v)
                    size_count += sys.getsizeof(k)
                    size_count += sys.getsizeof(v)
        elif not isinstance(x, str):
            repeat_more_one = []
            for el in x:
                show_sizeof(el)
                repeat = x.count(el)
                if repeat > 1:
                    repeat_more_one.append(el)
                    continue
                else:
                    size_count += sys.getsizeof(el)
            for e in set(repeat_more_one):
                size_count += sys.getsizeof(e)
    return size_count


num = str(input("Введите число: "))
num_2 = num
revers_num = ""
if num.isdigit():
    while len(num) != 0:
        global a
        a = num[-1]
        revers_num += a
        num = num[: -1]
    else:
        f"Это не число"


print(f"Для числа {num_2} обратным числом является {revers_num}")
print(f"Обьем потребляемой памяти равен {int(sum(map(show_sizeof,[num, num_2, revers_num, a])))}")

# Версия для ленивых


num_n = input("Введите число: ")
if num_n.isdigit():
    num = int(num_n[::-1])



print(f"Для числа {num_n} обратным числом является {num}")
print(f"Обьем потребляемой памяти равен {show_sizeof(num_n) + show_sizeof(num)}")


# Рекурсия

def reverse_string(string, new_string=""):
    if len(string) == 0:
        return int(new_string)
    global a_2
    a_2 = string[-1]
    new_string += a_2
    string = string[:-1]
    return reverse_string(string, new_string)


string = input("Введите число: ")
initial_string = string

print(f"Для числа {initial_string} обратным числом является {reverse_string(string)}")
print(f"Обьем потребляемой памяти {int(sum(map(show_sizeof,[string, reverse_string(string), a_2, initial_string])))}")

# Сложно. Переделала функцию из урока на вывод общего обьема потребляемой памяти.
# Не могу с уверенностью сказать, что все корректно работает.
# Результат:

# Введите число: 123
# Для числа 123 обратным числом является 321
# Обьем потребляемой памяти равен 203

# Введите число: 123
# Для числа 123 обратным числом является 321
# Обьем потребляемой памяти равен 80

# Введите число: 123
# Для числа 123 обратным числом является 321
# Обьем потребляемой памяти 182

# Везде работу веду со строкой, но удалось в слайсе и рекурсии сэкономить
# немного памяти, перегнав результат в целое число. В каждом варианте можно еще
# убрать по 52 байта, если не выводить изначально введенное пользователем значение.
# Не нравится использование global, но лучше ничего в голову не пришло.
# Алгоритм со слайсом на мой взгляд самый удачный - быстро и можно при желании
# обратить в число или оставить строку.



