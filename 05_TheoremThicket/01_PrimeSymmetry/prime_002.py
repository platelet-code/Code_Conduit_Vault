class Solution:
    def countPrimes(self, n: int) -> int:
        def sieve_of_eratosthenes(n: int) -> List[int]:
            is_prime = [True] * (n + 1)
            
            for p in range(2, int(n**0.5) + 1):
                if is_prime[p]:
                    for i in range(p * p, n + 1, p):
                        is_prime[i] = False
            
            return is_prime
        
        is_prime = sieve_of_eratosthenes(n)
        return sum(1 for i in range(2, n) if is_prime[i])
