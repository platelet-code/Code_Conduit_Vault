def longestCommonSubsequence(text1: str, text2: str) -> int:
    @cache
    def dfs(i: int, j: int) -> int:
        if i < 0 or j < 0:
            return 0
        if text1[i] == text2[j]:
            return dfs(i - 1, j - 1) + 1
        return max(dfs(i - 1, j), dfs(i, j - 1))
    
    return dfs(len(text1) - 1, len(text2) - 1)


def longestCommonSubsequence(text1: str, text2: str) -> int:
    n, m = len(text1), len(text2)
    f = [[0] * (m + 1) for _ in range(n + 1)]
    for i, x in enumerate(text1):
      for j, y in enumerate(text2):
          if x == y:
              f[i + 1][j + 1] = f[i][j] + 1 
          else:
              f[i + 1][j + 1] = max(f[i][j + 1], f[i + 1][j])
    
    return f[n][m]
