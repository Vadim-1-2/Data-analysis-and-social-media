import networkx as nx
import matplotlib.pyplot as plt

# Создание графа
G = nx.Graph()

# Список для графа
edges = []

# Первое кольцо
for i in range(1, 14):
    edges.append((i, i + 1))
edges.append((14, 15))  # Замыкаем первое кольцо с первой стороны

# Второе кольцо
for i in range(16, 30):
    edges.append((i, i + 1))
edges.append((15, 16))  # Замыкаем второе кольцо с первой стороны


edges.append((15, 1))  # Замыкаем первое кольцо со второй стороны
edges.append((15, 30)) # Замыкаем второе кольцо со второй стороны


G.add_edges_from(edges)

# Вычисление мер центральности в собственных векторах
eigen_centrality = nx.eigenvector_centrality(G)

# Вывод результатов
for node, centrality in eigen_centrality.items():
    print(f"Вершина {node}: Центральность = {centrality:.4f}")

# Визуализация графа
pos = nx.spring_layout(G)  # Выбор метода раскладки графа

# Рисование графа
nx.draw(G, pos, with_labels=False, node_size=700, font_size=14)

# Добавление меток центральности
labels = {node: f"{centrality:.2f}" for node, centrality in eigen_centrality.items()}
nx.draw_networkx_labels(G, pos, labels=labels, font_size=14)

# Отображение графа
plt.title("Граф с мерой центральности с пиком в середине и «ямами» по бокам от пика")
plt.show()