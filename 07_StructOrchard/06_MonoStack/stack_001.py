class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        rank = defaultdict(int)
        stack = []

        for x in nums2:
            while stack and stack[-1] < x:
                rank[stack.pop()] = x
            stack.append(x)
        
        while stack:
            rank[stack.pop()] = -1
        
        return [rank[num] for num in nums1]


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        rank = defaultdict(int)
        stack = []

        for x in reversed(nums2):
            while stack and x >= stack[-1]:
                stack.pop()
            rank[x] = stack[-1] if stack else -1
            stack.append(x)
        
        return [rank[num] for num in nums1]
