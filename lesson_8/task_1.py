# На улице встретились N друзей. Каждый пожал руку
# всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа

import numpy as np
n = int(input("Введите количество друзей: "))


def handshake(n):
    graph = np.ones((n, n))
    np.fill_diagonal(graph, 0)
    count = 0
    for el in graph:
        for i in el:
            if i == 1:
                count += 1
    return f"Количество рукопожатий между друзьями равно {round(count / 2)}"


print(handshake(n))