class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        cnt = defaultdict(int)
        for i in range(len(nums1)):
            x = nums1[i]
            if x % k:
                continue
            x //= k

            for d in range(1, isqrt(x) + 1):
                if x % d:
                    continue
                cnt[d] += 1
                if d * d < x:
                    cnt[x // d] += 1
        
        return sum(cnt[num] for num in nums2)
