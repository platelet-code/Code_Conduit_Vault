class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        def minOperationsToZero(nums: List[int]) -> int:
            pos, neg = max(0, nums[0]), min(0, nums[0])
            for i in range(1, len(nums)):
                diff = nums[i] - nums[i - 1]
                if diff > 0:
                    pos += diff
                elif diff < 0:
                    neg += diff
            return max(pos, -neg)
            
        changes = [num - tar for (num, tar) in zip(nums, target)]
        return minOperationsToZero(changes)
