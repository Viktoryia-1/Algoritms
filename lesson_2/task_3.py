# Сформировать из введенного числа обратное по порядку
# входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843

num = str(input("Введите число: "))
num_2 = num
revers_num = ""
if num.isdigit():
    while len(num) != 0:
        a = num[-1]
        revers_num += a
        num = num[: -1]
else:
    print("Это не число")
print(f"Для числа {num_2} обратным числом является {revers_num}")


# Версия для ленивых


def reverse_num(num):
    if num.isdigit():
        num_2 = num[::-1]
        return f"Для числа {num} обратным числом является {num_2}"

print(reverse_num("123"))


# Рекурсия

def reverse_string(string, new_string=""):
    if len(string) == 0:
        return new_string
    a = string[-1]
    new_string += a
    string = string[:-1]
    return reverse_string(string, new_string)


print(f"Для числа {'123'} обратным числом является {reverse_string('123')}")

