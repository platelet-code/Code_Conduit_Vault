class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = Counter(s)  # 直接维护窗口外的字母个数
        if any(cnt[c] < k for c in "abc"):
            return -1
        
        mx = left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1
            while left <= right and cnt[c] < k:  
                cnt[s[left]] += 1
                left += 1
            mx = max(mx, right - left + 1)
        return len(s) - mx
