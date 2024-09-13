class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # 邻项交换 排序不等式
        degrees = [0] * n
        for a, b in roads:
            degrees[a] += 1
            degrees[b] += 1
        
        degrees.sort()
        return sum(d * i for i, d in enumerate(degrees, 1))
