def Dijcstra(graph, start, end=0):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):
        is_visited[start] = True
        for i, vertex in enumerate(graph[start]):
            if vertex != 0 and not is_visited[i]:
                if cost[i] > cost[start] + vertex:
                    cost[i] = cost[start] + vertex
                    parent[i] = start


        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i

    return cost, parent


graph = [[0, 0, 1, 1, 9, 0, 0, 0],
         [0, 0, 9, 4, 0, 0, 5, 0],
         [0, 9, 0, 0, 3, 0, 6, 0],
         [0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 5, 0],
         [0, 0, 7, 0, 8, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 2, 0]]

print(Dijcstra(graph, 0))
