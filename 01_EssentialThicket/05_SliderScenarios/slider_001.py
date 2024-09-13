class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        left = 0
        cnt = defaultdict(int)

        for right, x in enumerate(s):
            cnt[x] += 1
            while left <= right and cnt[x] >= 2:
                cnt[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)
        
        return ans
