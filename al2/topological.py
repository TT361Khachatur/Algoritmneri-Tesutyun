# Տոպոլոգիական սորտավորում
def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(v):
        visited.add(v)
        for u in graph.get(v, []):
            if u not in visited:
                dfs(u)
        stack.append(v)

    for v in graph:
        if v not in visited:
            dfs(v)

    return stack[::-1]
