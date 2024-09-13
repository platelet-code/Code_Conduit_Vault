class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def sieve_of_euler(n: int) -> List[int]:
            vis = [False] * (n + 1)
            primes = []
            for i in range(2, n + 1):
                if not vis[i]:
                    primes.append(i)
                for j in primes:
                    if j * i > n:
                        break
                    vis[j * i] = True
                    if i % j == 0:
                        break
            return primes

        upper_limit = int(r**0.5)
        primes = sieve_of_euler(upper_limit)
        
        special_count = 0
        for p in primes:
            p_square = p * p
            if p_square < l:
                continue
            if p_square > r:
                break
            special_count += 1
        
        return (r - l + 1) - special_count
