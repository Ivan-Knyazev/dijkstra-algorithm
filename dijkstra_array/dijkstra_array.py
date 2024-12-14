def dijkstra(graph, start):
    num_vertices = len(graph)
    distances = [float('inf')] * num_vertices  # Массив расстояний
    distances[start] = 0  # Расстояние до начальной вершины равно 0
    # Массив для отслеживания посещённых вершин
    visited = [False] * num_vertices

    for _ in range(num_vertices):
        # Находим вершину с минимальным расстоянием
        min_distance = float('inf')
        min_index = -1

        for v in range(num_vertices):
            if not visited[v] and distances[v] < min_distance:
                min_distance = distances[v]
                min_index = v

        # Помечаем вершину как посещённую
        visited[min_index] = True

        # Обновляем расстояния до соседей
        for v in range(num_vertices):
            if graph[min_index][v] > 0 and not visited[v]:  # Если есть ребро
                new_distance = distances[min_index] + graph[min_index][v]
                if new_distance < distances[v]:
                    distances[v] = new_distance

    return distances


# Пример графа в виде матрицы смежности
# 0 означает отсутствие ребра между вершинами
graph = [
    [0, 1, 4, 0, 0],
    [1, 0, 2, 5, 0],
    [4, 2, 0, 1, 0],
    [0, 5, 1, 0, 3],
    [0, 0, 0, 3, 0]
]

# Запуск алгоритма Дейкстры
start_vertex = 0  # Начальная вершина (например, 0 соответствует 'A')
shortest_paths = dijkstra(graph, start_vertex)

# Вывод результатов
print(f"Кратчайшие расстояния от вершины {start_vertex}:")
for vertex, distance in enumerate(shortest_paths):
    print(f"До вершины {vertex}: {distance}")
