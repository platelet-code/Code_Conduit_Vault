class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        def is_red(score: int) -> bool:
            pre_x = -inf
            for s in start:
                x = pre_x + score
                if x > s + d:
                    return False
                pre_x = max(x, s)
            return True
            
        
        left, right = 1, 2 * (10 ** 9) + 1
        while left < right:
            pivot = (left + right + 1) // 2
            if is_red(pivot):
                left = pivot
            else:
                right = pivot - 1
        
        return left
