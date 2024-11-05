import heapq

def dijkstra(n, roads, start, end):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v, cost in roads:
        graph[u].append((v, cost))
        graph[v].append((u, cost))
    distances = {i: float('inf') for i in range(1, n + 1)}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_cost, current_node = heapq.heappop(pq)
        if current_cost > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_cost + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances[end]

n = 4
roads = [
    (1, 2, 4),
    (1, 3, 2),
    (2, 3, 5),
    (2, 4, 1),
    (3, 4, 7)
]
start, end = 1, 4
print(dijkstra(n, roads, start, end))