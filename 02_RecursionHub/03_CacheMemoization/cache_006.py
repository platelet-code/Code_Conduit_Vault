class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i: int) -> int:
            if i == 0:
                return 1
            return sum(dfs(i - x) for x in nums if x <= i)
        return dfs(target)
