import timeit
import cProfile

# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

# Вариант 1

def first():
    multiples_of_2 = 0
    multiples_of_3 = 0
    multiples_of_4 = 0
    multiples_of_5 = 0
    multiples_of_6 = 0
    multiples_of_7 = 0
    multiples_of_8 = 0
    multiples_of_9 = 0

    for i in range(2, 98):
        if i % 2 == 0:
            multiples_of_2 += 1
        if i % 3 == 0:
            multiples_of_3 += 1
        if i % 4 == 0:
            multiples_of_4 += 1
        if i % 5 == 0:
            multiples_of_5 += 1
        if i % 6 == 0:
            multiples_of_6 += 1
        if i % 7 == 0:
            multiples_of_7 += 1
        if i % 8 == 0:
            multiples_of_8 += 1
        if i % 9 == 0:
            multiples_of_9 += 1
# 100 loops, best of 5: 11 nsec per loop
# n = 998
# 100 loops, best of 5: 11.6 nsec per loop
# n = 9998
# 100 loops, best of 5: 17.6 nsec per loop

# cProfile.run("first()")

# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:10(first)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# print(f"Чисел, кратных 2 {multiples_of_2} \n"
#       f"Чисел, кратных 3 {multiples_of_3} \n"
#       f"Чисел, кратных 4 {multiples_of_4} \n"
#       f"Чисел, кратных 5 {multiples_of_5} \n"
#       f"Чисел, кратных 6 {multiples_of_6} \n"
#       f"Чисел, кратных 7 {multiples_of_7} \n"
#       f"Чисел, кратных 8 {multiples_of_8} \n"
#       f"Чисел, кратных 9 {multiples_of_9}")
# print(f"\n")

# Вариант 2

def second():
    list_summ = []
    for i in range(2, 10):
        summ = 98 // i
        list_summ.append(summ)


# for i, el in enumerate(second(), 2):
#     print(f"Чисел, кратных {i} : {el}")
#
# print(f"\n")
# summ = 98
# 100 loops, best of 5: 10.2 nsec per loop

# summ = 9998
# 100 loops, best of 5: 10.8 nsec per loop

# cProfile.run("second()")

# 12 function calls in 0.000 seconds
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1_2.py:4(second)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# summ = 998
# 12 function calls in 0.000 seconds


# summ = 9998
# 12 function calls in 0.000 seconds

# Вариант 3

def third():
    x_el = []
    for el in range(2, 10):
        summ_2 = 0
        for i in range(2, 98):
            if i % el == 0:
                summ_2 += 1
        x_el.append(summ_2)


# for i, el in enumerate(x_el, 2):
#     print(f"Чисел, кратных {i} : {el}")

#  n = 99
# 100 loops, best of 5: 10.7 nsec per loop
# n = 998
# 100 loops, best of 5: 12 nsec per loop
# n = 9998
# 100 loops, best of 5: 12.5 nsec per loop

# cProfile.run("third()")
#  n = 98
#  12 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_3.py:4(third)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         8    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# n = 998
# 12 function calls in 0.002 seconds
# n = 9998
# 12 function calls in 0.012 seconds

# ВЫВОД:
# Вариант 1:
# Не оптимально.Занимает времени больше других (долго проверяет все условия),
# доллго писать сам код

# Вариант 2
# Самый оптимальный. Работает быстрее остальных: увеличение числа на 9900 увеличило время
# выполнения на 0.6 nsec

# Вариант 3
# Очень похож на второй, но работает медленне за счет большего количества вычислений
# в самом цикле.