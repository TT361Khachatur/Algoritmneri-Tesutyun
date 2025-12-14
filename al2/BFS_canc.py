# BFS ցանցերում
from collections import deque

def bfs_grid(grid, start):
    rows, cols = len(grid), len(grid[0])
    visited = set([start])
    queue = deque([start])
    result = []

    while queue:
        r, c = queue.popleft()
        result.append((r, c))
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc))

    return result
