# BFS գրաֆերում
from collections import deque

def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    order = []

    while queue:
        v = queue.popleft()
        order.append(v)
        for u in graph.get(v, []):
            if u not in visited:
                visited.add(u)
                queue.append(u)

    return order
