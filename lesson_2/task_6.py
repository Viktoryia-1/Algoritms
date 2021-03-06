# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести ответ
from random import randint
num = randint(0, 101)
guess_count = 10
count = 0

while True:
    user_guess = int(input("Введите целое число от 0 до 100: "))
    guess_count -= 1
    count += 1
    if guess_count == 0:
        print(f"Вы проиграли. Загаданное число {num}")
        break
    if 0 < user_guess < 100:
        print(f"Осталось {guess_count} попыток")
        if user_guess == num:
            print(f"Вы угадали с {count} попытки. Загаданное число {num}")
            break
        elif user_guess > num:
            print("Ваше число больше загаданного")
        elif user_guess < num:
            print("Ваше число меньше загаданного")
    else:
        print("Ошибка диапазона числа. \n"
              "Введите число от 0 до 100")
