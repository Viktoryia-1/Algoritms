# Вводятся три разных числа.
# Найти, какое из них является средним
# (больше одного, но меньше другого).
numbers = input("Ввведите три числа через пробел")
a, b, c = numbers.split(' ')
a, b, c = int(a), int(b), int(c)

max_num = max(a, b, c)
min_num = min(a, b, c)

if max_num != a & a != min_num:
    print(a)
elif max_num != b & b != min_num:
    print(b)
else:
    print(c)
