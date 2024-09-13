class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        left = 0
        right = (n + 1) // 2
        ans = 0

        while right < n:
            if nums[left] * 2 <= nums[right]:
                print(left, right, nums[left], nums[right])
                left += 1
                right += 1
                ans += 2
            else:
                right += 1
        
        return ans
