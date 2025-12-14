# Բելման-Ֆորդի ալգորիթմ
def bellman_ford(vertices, edges, start):
    dist = {v: float("inf") for v in vertices}
    dist[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    return dist
