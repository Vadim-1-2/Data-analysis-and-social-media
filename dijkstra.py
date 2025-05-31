import heapq
import math


def dijkstra(graph, start, is_adjacency_matrix=False):
    # Определение количества вершин
    if is_adjacency_matrix:
        num_vertices = len(graph)
    else:
        num_vertices = len(graph)

    # Инициализация расстояний
    distances = {v: math.inf for v in range(num_vertices)}
    distances[start] = 0

    # Приоритетная очередь, где элементы имеют вид (расстояние, вершина)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Если текущее расстояние больше уже найденного, пропускаем обработку
        if current_distance > distances[current_vertex]:
            continue

        # Обработка соседей
        if is_adjacency_matrix:
            # Если граф задан матрицей смежности
            for neighbor in range(num_vertices):
                if graph[current_vertex][neighbor] != 0:  # Проверяем наличие ребра
                    weight = graph[current_vertex][neighbor]
                    distance = current_distance + weight

                    # Если найден более короткий путь
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))
        else:
            # Если граф задан списком смежности
            for neighbor, weight in graph[current_vertex]:
                distance = current_distance + weight

                # Если найден более короткий путь
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Пример использования
if __name__ == "__main__":
    # Пример графа в виде матрицы смежности
    adjacency_matrix = [
        [0, 10, 0, 0, 0, 0],
        [10, 0, 5, 0, 0, 0],
        [0, 5, 0, 20, 1, 0],
        [0, 0, 20, 0, 2, 2],
        [0, 0, 1, 2, 0, 3],
        [0, 0, 0, 2, 3, 0]
    ]

    # Пример графа в виде списка смежности
    adjacency_list = {
        0: [(1, 10)],
        1: [(0, 10), (2, 5)],
        2: [(1, 5), (3, 20), (4, 1)],
        3: [(2, 20), (4, 2), (5, 2)],
        4: [(2, 1), (3, 2), (5, 3)],
        5: [(3, 2), (4, 3)]
    }

    # Запуск алгоритма Дейкстры
    start_vertex = 0
    print("Матрица смежности:")
    print(dijkstra(adjacency_matrix, start_vertex, is_adjacency_matrix=True))

    print("\nСписок смежности:")
    print(dijkstra(adjacency_list, start_vertex, is_adjacency_matrix=False))