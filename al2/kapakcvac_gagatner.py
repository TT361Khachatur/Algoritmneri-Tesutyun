
# Կապակցված գագաթների խմբերի հայտնաբերում գրաֆերում
def connected_components(graph):
    visited = set()
    components = []

    def dfs(v, comp):
        visited.add(v)
        comp.append(v)
        for u in graph.get(v, []):
            if u not in visited:
                dfs(u, comp)

    for v in graph:
        if v not in visited:
            comp = []
            dfs(v, comp)
            components.append(comp)

    return components
