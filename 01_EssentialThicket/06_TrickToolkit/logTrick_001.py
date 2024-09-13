class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        def logTrick(nums: List[int], op):
            res = defaultdict(int)
            dp = []
            for pos, cur in enumerate(nums):
                for v in dp:
                    v[2] = op(v[2], cur)
                dp.append([pos, pos + 1, cur])

                ptr = 0
                for v in dp[1:]:
                    if dp[ptr][2] != v[2]:
                        ptr += 1
                        dp[ptr] = v
                    else:
                        dp[ptr][1] = v[1]
                dp = dp[: ptr + 1]

                for v in dp:
                    res[v[2]] += v[1] - v[0]

            return res
        
        result = logTrick(nums, lambda x, y: x & y)
        return result[k]
