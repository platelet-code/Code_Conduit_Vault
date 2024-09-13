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
