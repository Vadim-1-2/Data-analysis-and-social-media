import networkx as nx
import numpy as np

# Заданные параметры
n = 70  # Количество вершин
p = 0.45  # Вероятность появления ребра

# Создание графа в модели Эрдеша-Реньи
G = nx.erdos_renyi_graph(n, p)

# Вычисление средней степени вершины в созданном графе
average_degree = np.mean([d for _, d in G.degree()])

# Теоретическая средняя степень вершины
theoretical_average_degree = (n - 1) * p

print(f"Средняя степень вершины в созданном графе: {average_degree:.2f}")
print(f"Теоретическая средняя степень вершины: {theoretical_average_degree:.2f}")
