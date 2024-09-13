class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        max_area = 0
        n = len(matrix[0])
        heights = [0] * (n + 1)
        
        def largestRectangleArea(heights: List[int]) -> int:
            n = len(heights)
            left = [0] * n
            right = [n] * n
            
            stack = []
            for i in range(n):
                while stack and heights[stack[-1]] >= heights[i]:
                    right[stack.pop()] = i
                left[i] = stack[-1] if stack else -1
                stack.append(i)
            
            ans = 0
            for x, l, r in zip(heights, left, right):
                ans = max(ans, (r - l - 1) * x)
            return ans

        for row in matrix:
            for i in range(n):
                if row[i] == '1':
                    heights[i] += 1
                else:
                    heights[i] = 0
            max_area = max(max_area, largestRectangleArea(heights))   

        return max_area
