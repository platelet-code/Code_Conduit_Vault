class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        memo = {}
        def dfs(i: int, j: int) -> int:
            if j < 0:
                return 0
            if i < 0:
                return -inf
                
            key = (i, j)
            if key in memo:
                return memo[key]

            memo[key] = max(dfs(i - 1, j), dfs(i - 1, j - 1) + a[j] * b[i])
            return memo[key]
        
        return dfs(len(b) - 1, 3)


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:
        f = [0] + [-inf] * 4
        for y in b:
            for j in range(3, -1, -1):
                f[j + 1] = max(f[j + 1], f[j] + a[j] * y)   
        return f[4]
