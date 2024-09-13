from typing import List

class UnionFind:
    def __init__(self, size: int) -> None:
        self.fa = list(range(size))

    def find(self, x: int) -> int:
        root = x
        while self.fa[root] != root:
            root = self.fa[root]
        while self.fa[x] != root:
            self.fa[x], x = root, self.fa[x]
        return root

    def union(self, a: int, b: int) -> None:
        self.fa[self.find(a)] = self.find(b)

            
def solve(grid: List[List[str]]) -> bool:
    n, m = len(grid), len(grid[0])
    uf = UnionFind(n * m)
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    sx = sy = ex = ey = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'S':
                sx, sy = i, j
            elif grid[i][j] == 'E':
                ex, ey = i, j
            if grid[i][j] == '#':
                continue
            for dx, dy in directions:
                x, y = i + dx, j + dy
                if 0 <= x < n and 0 <= y < m and grid[x][y] != '#':
                    uf.union(i * m + j, x * m + y)

    if uf.find(ex * m + ey) == uf.find(sx * m + sy):
        return True

    row = [False] * n
    col = [False] * m
    start_root = uf.find(sx * m + sy)

    for i in range(n):
        for j in range(m):
            if uf.find(i * m + j) == start_root:
                row[i] = col[j] = True

    for i in range(n):
        for j in range(m):
            if uf.find(i * m + j) == uf.find(ex * m + ey):
                for k in range(-1, 2):
                    if (0 <= i + k < n and row[i + k]) or (0 <= j + k < m and col[j + k]):
                        return True

    return False


if __name__ == "__main__":
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]
    if solve(grid):
        print("YES")
    else:
        print("NO")
