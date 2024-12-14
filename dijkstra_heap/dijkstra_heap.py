import heapq

def dijkstra(graph, start):
    # Инициализация расстояний и кучи
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]  # (расстояние, вершина)

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если расстояние больше, чем уже найденное, пропускаем
        if current_distance > distances[current_vertex]:
            continue

        # Обходим соседей текущей вершины
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Если найдено более короткое расстояние
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Пример графа в виде списка смежности
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Запуск алгоритма Дейкстры
start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

# Вывод результатов
print(f"Кратчайшие расстояния от вершины '{start_vertex}':")
for vertex, distance in shortest_paths.items():
    print(f"До вершины '{vertex}': {distance}")
