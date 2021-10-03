# Поиск простых чисел
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59.
import timeit
import cProfile

# Вариант 1
def first(n, n_user):
    simple_list = []
    s = 0
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                s += 1
        if s == 0:
            simple_list.append(i)
        else:
            s = 0
    if n_user < len(simple_list):
        number = simple_list[n_user - 1]

        return number

# a = first(10000, 5)
# print(a)
# print(simple_list)

# n = 30
# 100 loops, best of 5: 12 nsec per loop
# n = 100
# 100 loops, best of 5: 11.1 nsec per loop
# n = 1000
# 100 loops, best of 5: 8.28 nsec per loop
# n = 10000
# 100 loops, best of 5: 8.13 nsec per loop

# cProfile.run("first(10000, 5)")
# n = 30
#   15 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_2.py:7(first)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#        10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# n = 100
# 30 function calls in 0.001 seconds
# 25    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# n = 1000
# 173 function calls in 0.043 seconds
# 1    0.043    0.043    0.043    0.043 task_2.py:7(first)
# 168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# n = 10000
# 1234 function calls in 3.176 seconds
# 1    3.176    3.176    3.176    3.176 task_2.py:7(first)
# 1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# Вариант 2

def second(n, n_user):
    simple_list = [2]
    for i in range(3, n + 1, 2):
        for j in range(2, i):
            if i > 10 and i % 5 == 0:
                break
            if i % j == 0:
                break
        else:
            simple_list.append(i)
    if n_user < len(simple_list):
        number = simple_list[n_user - 1]

        return number

# a_2 = second(30, 5)
# print(a_2)
# n = 30
# 100 loops, best of 5: 12.6 nsec per loop
# n = 100
# 100 loops, best of 5: 13.2 nsec per loop
# n = 1000
# 100 loops, best of 5: 12.6 nsec per loop
# n = 10000
# 100 loops, best of 5: 9.76 nsec per loop

# cProfile.run("second(10000, 5)")

# n = 30
# 14 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_2.py:66(second)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# n = 100
# 29 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 task_2.py:66(second)
# 24    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

#  n = 1000
# 172 function calls in 0.018 seconds
# 1    0.017    0.017    0.017    0.017 task_2.py:63(second)
# 167    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# n = 10000
# 1233 function calls in 0.783 seconds
# 1    0.930    0.930    0.931    0.931 task_2.py:63(second)
# 1228    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}

# Решето Эратосфена

def third(n, n_user):
    start_list = [i for i in range(n)]
    start_list[1] = 0
    for i in range(2, n):
        if start_list[i] != 0:
            j = i * 2
            while j < n:
                start_list[j] = 0
                j += i

    simple_list = [i for i in start_list if i != 0]

    if n_user < len(simple_list):
        number = simple_list[n_user - 1]

        return number

# a_3 = third(10000, 5)
# print(a_3)

# n = 30
# 100 loops, best of 5: 10.8 nsec per loop
# n = 100
# 100 loops, best of 5: 10.0 nsec per loop
# n = 1000
# 100 loops, best of 5: 10.7 nsec per loop
# n = 10000
# 100 loops, best of 5: 10.1 nsec per loop

cProfile.run("third(10000, 5)")

# n = 30
# 7 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_2.py:115(third)
#         1    0.000    0.000    0.000    0.000 task_2.py:116(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_2.py:125(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# n = 100
# 7 function calls in 0.000 seconds

# n = 1000
# 7 function calls in 0.001 seconds

# n = 10000
# 1    0.004    0.004    0.005    0.005 task_2.py:124(third)
# 7 function calls in 0.006 seconds

