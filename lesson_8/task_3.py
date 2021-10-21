# 3. Написать программу, которая обходит не
# взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму
# поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции,
# которая принимает на вход число вершин


def make_graph(num):
    graph = {}
    for el in range(num):
        graph[el] = [i for i in range(num) if i != el]
    return graph


graph = make_graph(4)
print(graph)


is_visited = []


def dfs(graph, start, is_visited):
    if start not in graph:
        return print("Данной вершины нет в графе")
    if start not in is_visited:
        is_visited.append(start)
        for k in graph[start]:
            dfs(graph,k, is_visited)
    return is_visited


result_visited = dfs(graph, 2, is_visited)
print(result_visited)

