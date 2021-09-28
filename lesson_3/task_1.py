# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

# Вариант 1
multiples_of_2 = 0
multiples_of_3 = 0
multiples_of_4 = 0
multiples_of_5 = 0
multiples_of_6 = 0
multiples_of_7 = 0
multiples_of_8 = 0
multiples_of_9 = 0

for i in range(2, 99):
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

print(f"Чисел, кратных 2 {multiples_of_2} \n"
      f"Чисел, кратных 3 {multiples_of_3} \n"
      f"Чисел, кратных 4 {multiples_of_4} \n"
      f"Чисел, кратных 5 {multiples_of_5} \n"
      f"Чисел, кратных 6 {multiples_of_6} \n"
      f"Чисел, кратных 7 {multiples_of_7} \n"
      f"Чисел, кратных 8 {multiples_of_8} \n"
      f"Чисел, кратных 9 {multiples_of_9}")
print(f"\n")

# Вариант 2
list_summ = []
for i in range(2, 10):
    summ = 98 // i
    list_summ.append(summ)

for i, el in enumerate(list_summ, 2):
    print(f"Чисел, кратных {i} : {el}")

print(f"\n")

# Вариант 3
x_el = []
for el in range(2, 10):
    summ_2 = 0
    for i in range(2, 99):
        if i % el == 0:
            summ_2 += 1
    x_el.append(summ_2)


for i, el in enumerate(x_el, 2):
    print(f"Чисел, кратных {i} : {el}")