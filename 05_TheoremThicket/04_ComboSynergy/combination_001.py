class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        @cache
        def fac(x):
            return math.factorial(x)

        half_len = (n + 1) // 2
        palindromes = set()
        for num in range(10 ** (half_len - 1), 10 ** half_len):
            pal_str = str(num) + str(num)[:n - len(str(num))][::-1]
            if int(pal_str) % k == 0:
                palindromes.add(tuple(sorted(Counter(pal_str).items())))

        total = 0
        for counts in palindromes:
            combinations = fac(n)
            for _, count in counts:
                combinations //= fac(count)

            if counts[0][0] == '0':
                wrong_comb = fac(n - 1)
                wrong_comb //= fac(counts[0][1] - 1)
                for _, count in counts[1:]:
                    wrong_comb //= fac(count)
                combinations -= wrong_comb

            total += combinations
        
        return total
