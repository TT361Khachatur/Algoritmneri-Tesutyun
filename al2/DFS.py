# DFS գրաֆերում
def dfs(graph, start):
    visited = set()
    order = []

    def visit(v):
        visited.add(v)
        order.append(v)
        for u in graph.get(v, []):
            if u not in visited:
                visit(u)

    visit(start)
    return order
