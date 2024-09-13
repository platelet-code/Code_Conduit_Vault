def digital_triangle(triangle: List[List[int]]) -> int:
    n = len(triangle)

    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            triangle[i][j] += max(triangle[i + 1][j + 1], triangle[i + 1][j])
    
    return triangle[0][0]


def digital_triangle(triangle: List[List[int]]) -> int:
    n = len(triangle)
    @lru_cache(None)
    def dfs(level, index):
        if level == n - 1:
            return triangle[level][index]
        left = dfs(level + 1, index)
        right = dfs(level + 1, index + 1)
        return triangle[level][index] + max(left, right)
    return dfs(0, 0)
