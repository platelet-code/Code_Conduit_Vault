class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)
        n = len(students[0])

        score = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                score[i][j] = sum(students[i][k] == mentors[j][k] for k in range(n))
        
        @cache
        def dfs(i: int, mask: int) -> int:
            if i == m:
                return 0
            
            max_score = 0
            for j in range(m):
                if not (mask >> j & 1):
                    total_score = score[i][j] + dfs(i + 1, mask | (1 << j))
                    max_score = max(max_score, total_score)
            
            return max_score
        
        return dfs(0, 0)



class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m, n = len(students), len(students[0])
        g = [[0] * m for _ in range(m)]

        for i in range(m):
            for j in range(m):
                g[i][j] += sum(students[i][k] == mentors[j][k] for k in range(n))

        f = [0] * (1 << m)
        for mask in range(1, 1 << m):
            c = bin(mask).count("1")
            for i in range(m):
                if mask & (1 << i):
                    f[mask] = max(f[mask], f[mask ^ (1 << i)] + g[c - 1][i])
        
        return f[(1 << m) - 1]
