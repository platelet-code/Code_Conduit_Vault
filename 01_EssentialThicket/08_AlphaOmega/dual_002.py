class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        suf = [1] * n

        for i in range(n - 2, -1, -1):
            suf[i] = suf[i + 1] * nums[i + 1]
        
        pre = 1
        for i, x in enumerate(nums):
            suf[i] *= pre
            pre *= x

        return suf
