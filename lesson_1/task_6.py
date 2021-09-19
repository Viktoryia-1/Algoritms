# По длинам трех отрезков, введенных пользователем, определить
# возможность существования треугольника, составленного из этих отрезков.
# Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.
sids_length = input("Введите стороны треугольника через пробел: ")
a, b, c = sids_length.split(" ")
a, b, c = int(a), int(b), int(c)

if a == b and a == c and b == c:
    print("Треугольник равносторонний")
elif a == b or a == c or b == c:
    print("Треугольник равнобедренный")
else:
    print("Треугольник разносторонний")