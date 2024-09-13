class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        all_values = sorted({val for row in grid for val in row})
        values_positions = defaultdict(set)

        for row_index, row in enumerate(grid):
            for val in row:
                values_positions[val].add(row_index)
            
        @cache
        def dp(index: int, row_mask: int) -> int:
            if index == len(all_values):
                return 0

            max_score = dp(index + 1, row_mask)

            val = all_values[index]
            for r in range(num_rows):
                if r in values_positions[val] and not (row_mask >> r & 1):
                    score = val + dp(index + 1, row_mask | (1 << r))
                    max_score = max(max_score, score)

            return max_score
        
        return dp(0, 0)
