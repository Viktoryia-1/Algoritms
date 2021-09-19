# Пользователь вводит номер буквы в алфавите.
# Определить, какая это буква.
import string
user_number = int(input("Введите число от 1 до 26: "))
index_number = user_number - 1
result = string.ascii_lowercase[index_number]
print(result)