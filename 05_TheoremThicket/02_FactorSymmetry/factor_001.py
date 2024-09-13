class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        if multiplier == 1:
            return nums
        
        from sortedcontainers import SortedList
        MOD = 10 ** 9 + 7
        sl = SortedList((v, i) for i, v in enumerate(nums))
        n = len(nums)
        times = [0] * n

        while k:
            v, i = sl[0]
            if v * multiplier > sl[-1][0]:
                break
            sl.pop(0)
            v *= multiplier
            times[i] += 1
            sl.add((v, i))
            k -= 1

        div, mod = divmod(k, n)
        for _, i in sl:
            times[i] += div
            if mod:
                times[i] += 1
                mod -= 1

        return [(v * pow(multiplier, t, MOD)) % MOD for v, t in zip(nums, times)]
