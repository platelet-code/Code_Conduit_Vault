def minDistance(word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)
    @cache
    def dfs(i: int, j: int) -> int:
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1
        if word1[i] == word2[j]:
            return dfs(i - 1, j - 1)
        return min(dfs(i - 1, j), dfs(i, j - 1), dfs(i - 1, j - 1)) + 1
    return dfs(n - 1, m - 1)


def minDistance(word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)
    f = [[0] * (m + 1) for _ in range(n + 1)]
    f[0] = list(range(m + 1))

    for i, x in enumerate(word1):
        f[i + 1][0] = i + 1
        for j, y in enumerate(word2):
            if x == y:
                f[i + 1][j + 1] = f[i][j] 
            else:
                f[i + 1][j + 1] = min(f[i][j + 1], f[i + 1][j], f[i][j]) + 1

    return f[n][m]
