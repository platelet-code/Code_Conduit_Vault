class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def build_kmp_fail(pattern: str) -> list:
            m = len(pattern)
            fail = [-1] * m
            for i in range(1, m):
                j = fail[i - 1]
                while j != -1 and pattern[j + 1] != pattern[i]:
                    j = fail[j]
                if pattern[j + 1] == pattern[i]:
                    fail[i] = j + 1
            return fail
            
        def check(s: str) -> bool:
            doubled_s = (s + s)[1:-1]
            return s in doubled_s
        
        n = len(s)
        fail = build_kmp_fail(s)
        lps = (fail)[-1] + 1
        return lps > 0 and n % (n - lps) == 0
