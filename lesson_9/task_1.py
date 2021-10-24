# Определение количества различных подстрок с использованием
# хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша
# (hash(), sha1() или любой другой из модуля hashlib
# задача считается не решённой.

import hashlib


def r_k(string, subs):
    assert len(string) > 0 and len(subs) > 0, "Строка не может быть пустой"
    assert len(string) != len(subs), "Целая строка не считается вхождением"
    assert len(string) > len(subs), "Подстрока не может быть длиннее строки"

    len_subs = len(subs)
    h_subs = hashlib.sha1(subs.encode("utf-8")).hexdigest()

    counter = 0
    for el in range(len(string) - len_subs + 1):
        if h_subs == hashlib.sha1(string[el: el + len_subs].encode("utf-8")).hexdigest():
            counter += 1

    return counter


string = input("Введите строку: ")
subs = input("Введите подстроку: ")
answer = r_k(string, subs)
print(f"Количество вхождений подстроки в строку: {answer}" if answer != 0 else f"Подстрока не нейдена")