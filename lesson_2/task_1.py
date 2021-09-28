# Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не завершается,
# а запрашивает новые данные для вычислений. Завершение программы должно выполняться
# при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак
# (не '0', '+', '-', '', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя.

while True:
    symbols = "0", "+", "-", "/", "*"
    num_1 = int(input("Введите первое число: "))
    num_2 = int(input("Введите второе число: "))
    symbol = input("Введите символ операции: ")
    if symbol not in symbols:
        print("Ошибка символа")
        continue
    elif symbol == "0":
        break
    elif symbol == "+":
        print(num_1 + num_2)
    elif symbol == "-":
        print(num_1 - num_2)
    elif symbol == "*":
        print(num_1 * num_2)
    else:
        try:
            print(num_1 / num_2)
        except ZeroDivisionError as err:
            print(f"Ошибка деления на ноль: {err}")
