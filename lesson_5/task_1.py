# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
from collections import OrderedDict


all_factories = []
count_factories = int(input("Введите количество анализируемых предприятий: "))
count = count_factories
summ_profit = 0
while count != 0:
    d = OrderedDict()
    d["firm"] = input("Введите название фирмы: ")
    d["profit"] = float(input("Введите прибыль предприятия: "))
    summ_profit += d["profit"]
    all_factories.append(d)
    count -= 1

mean_number = summ_profit / count_factories

less_profit = []
high_profit = []

for i in all_factories:
    if i["profit"] > mean_number:
        high_profit.append(i["firm"])
    else:
        less_profit.append(i["firm"])

print(f"\tПрибыль выше среднего имеют предприятия: {high_profit}\n "
f"\tПрибыль ниже среднего имеют предприятия: {less_profit}")

