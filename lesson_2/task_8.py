# Посчитать, сколько раз встречается определенная цифра в введенной
# последовательности чисел. Количество вводимых чисел и цифра,
# которую необходимо посчитать, задаются вводом с клавиатуры.

numbers = str(input("Введите последовательность чисел: "))
number = str(input("Введите искомое число: "))
count = 0

for el in numbers:
    if el == number:
        count += 1

if count != 0:
    print(f"Число {number} встречается в данной последоавтельности {count} раз")
else:
    print(f"Число {number} не найдено в данной последовательности")