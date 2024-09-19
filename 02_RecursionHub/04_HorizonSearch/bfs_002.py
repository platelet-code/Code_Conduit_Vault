class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        dis = [[inf] * n for _ in range(m)]
        dis[0][0] = grid[0][0]
        q = deque([(0, 0)])

        while q:
            i, j = q.popleft()
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= x < m and 0 <= y < n:
                    cost = grid[x][y]
                    if dis[i][j] + cost < dis[x][y]:
                        dis[x][y] = dis[i][j] + cost
                        if cost == 0:
                            q.appendleft((x, y))
                        else:
                            q.append((x, y))
        
        return dis[-1][-1] < health
