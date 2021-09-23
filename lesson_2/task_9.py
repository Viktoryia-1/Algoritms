# Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

numbers = input("Введите числа через запятую: ")
numbers = numbers.split(",")
string = ""
for el in numbers:
    summ = 0
    max_summ = 0
    if summ > max_summ:
        max_summ = summ
        print(max_summ)
    while el != 0:
        el = int(el)
        a = el % 10
        summ += a
        el = el // 10
    string += str(summ) + ","

string = string[: -1]
print(string)
max_el = 0
for el in string.split(","):
    el = int(el)
    if el > max_el:
        max_el = el
print(max_el)





