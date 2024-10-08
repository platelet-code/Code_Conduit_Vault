# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack, nums = [], []

        while head:
            nums.append(head.val)
            head = head.next

        ans = [0] * len(nums)
        
        for i, x in enumerate(nums):
            while stack and nums[stack[-1]] < x:
                ans[stack.pop()] = x
            stack.append(i)
        
        while stack:
            ans[stack.pop()] = 0
        
        return ans