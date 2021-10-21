# 2. Доработать алгоритм Дейкстры (рассматривался на уроке), чтобы он
# дополнительно возвращал список вершин, которые необходимо обойти.


# Не доработала, код не мой.
# Только немного добавила описания
# В целом вообще не понимаю, как этот алгоритм работает
from collections import deque
g = [[0, 0, 1, 1, 9, 0, 0, 0],
     [0, 0, 9, 4, 0, 0, 5, 0],
     [0, 9, 0, 0, 3, 0, 6, 0],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 5, 0],
     [0, 0, 7, 0, 8, 1, 0, 0],
     [0, 0, 0, 0, 0, 1, 2, 0]]


def dijkstra(graph, start):
    lenght = len(graph)
    is_visited = [False] * lenght
    cost = [float('inf')] * lenght
    parent = [-1] * lenght
    path = [None]*lenght
    path_start = start
    cost[start] = 0
    min_cost = 0
    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start

        min_cost = float('inf')
        for i in range(lenght):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
    for i in range(lenght):
        if i != path_start:
            node = i
            if parent[node] == -1:
                path[i] = deque([f"Пути от вершины {s} до вершины {node} не существует"])
            else:
                path[i] = deque([f" Путь от вершины {s} до вершины {i}"])
                while True:
                    path[i].appendleft(parent[node])
                    if parent[node] == path_start:
                        break
                    node = parent[node]

    return cost, path

s = int(input("От какой вершины идти: "))
cost, path = dijkstra(g, s)
print(cost)
for el in path:
    print(el)
