# Դեկստրայի ալգորիթմ
import heapq

def dijkstra(graph, start):
    dist = {v: float("inf") for v in graph}
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, v = heapq.heappop(pq)
        if d > dist[v]:
            continue
        for u, w in graph[v]:
            if dist[u] > d + w:
                dist[u] = d + w
                heapq.heappush(pq, (dist[u], u))

    return dist
