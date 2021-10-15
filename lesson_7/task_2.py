# Отсортируйте по возрастанию методом слияния одномерный
# вещественный массив, заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
from random import shuffle


def merge_list(left, right):
    final_list = []
    l_index, r_index = 0, 0
    for i in range(len(left) + len(right)):
        if l_index < len(left) and r_index < len(right):
            if left[l_index] <= right[r_index]:
                final_list.append(left[l_index])
                l_index += 1
            else:
                final_list.append(right[r_index])
                r_index += 1
        elif l_index == len(left):
            final_list.append(right[r_index])
            r_index += 1
        elif r_index == len(right):
            final_list.append(left[l_index])
            l_index += 1
    return final_list



def sep_list(array):
    if len(array) < 2:
        return array
    med = len(array) // 2
    left_side = array[:med]
    right_side = array[med:]
    return merge_list(sep_list(left_side), sep_list(right_side))


list_1 = [i for i in range(0, 50)]
shuffle(list_1)
print(list_1)

print(sep_list(list_1))