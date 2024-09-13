def pascal_triangle(max_n=2010, mod=10**9+7) -> List[int]:
    c = [[0] * (max_n + 1) for _ in range(max_n + 1)]

    for i in range(max_n + 1):
        for j in range(i + 1):
            if j == 0:
                c[i][j] = 1
            else:
                c[i][j] = (c[i - 1][j] + c[i - 1][j - 1]) % mod
    
    return c


class Combinatorics:
    def __init__(self, max_n=100010, mod=10**9+7):
        self.mod = mod
        self.fact, self.inv_fact = self.prepare_factorials(max_n, mod)

    def modular_inverse(self, a: int, p: int) -> int:
        def extended_gcd(a: int, b: int) -> Tuple[int, int]:
            if b == 0:
                return 1, 0
            x1, y1 = extended_gcd(b, a % b)
            x, y = y1, x1 - (a // b) * y1
            return x, y
            
        x, y = extended_gcd(a, p)
        return (x % p + p) % p

    def prepare_factorials(self, max_n: int, mod: int) -> Tuple[List[int], List[int]]:
        fact = [1] * (max_n + 1)
        inv_fact = [1] * (max_n + 1)
        for i in range(1, max_n + 1):
            fact[i] = fact[i - 1] * i % mod
            inv_fact[i] = inv_fact[i - 1] * self.modular_inverse(i, mod) % mod
        return fact, inv_fact

    def combination(self, n: int, k: int) -> int:
        if k > n:
            return 0
        return (self.fact[n] * self.inv_fact[k] % self.mod * self.inv_fact[n - k] % self.mod)


class LucasTheorem:
    def __init__(self, mod: int) -> None:
        self.mod = mod
        self.inv = [1] * (mod + 1)
        for i in range(2, mod):
            self.inv[i] = (self.mod - self.mod // i) * self.inv[self.mod % i] % self.mod

    def combination(self, a: int, b: int) -> int:
        if b > a:
            return 0
        result = 1
        for i in range(1, b + 1):
            numerator = (a - i + 1) % self.mod
            denominator_inv = self.inv[i]
            result = result * numerator % self.mod * denominator_inv % self.mod
        return result

    def lucas(self, a: int, b: int) -> int:
        if a < self.mod and b < self.mod:
            return self.combination(a, b)
        return (self.combination(a % self.mod, b % self.mod) * self.lucas(a // self.mod, b // self.mod) % self.mod)


class CombinationCalculator:
    def __init__(self, n: int) -> None:
        self.primes = []
        self.is_prime = [True] * (n + 1)
        self.sieve_primes(n)

    def sieve_primes(self, n: int) -> None:
        for i in range(2, n + 1):
            if self.is_prime[i]:
                self.primes.append(i)
            for prime in self.primes:
                if i * prime > n:
                    break
                self.is_prime[i * prime] = False
                if i % prime == 0:
                    break

    def count_factors(self, n: int, p: int) -> int:
        count = 0
        while n:
            n //= p
            count += n
        return count

    def calculate(self, a: int, b: int) -> List[int]:
        if b > a:
            return [0]

        sum_factors = [0] * len(self.primes)
        for i, prime in enumerate(self.primes):
            sum_factors[i] = self.count_factors(a, prime) - self.count_factors(b, prime) - self.count_factors(a - b, prime)

        result = [1]
        for i, prime in enumerate(self.primes):
            for _ in range(sum_factors[i]):
                result = self.mul(result, prime)
        
        return result[::-1]

    def mul(self, digits: List[int], x: int) -> List[int]:
        carry = 0
        for i in range(len(digits)):
            carry += digits[i] * x
            digits[i] = carry % 10
            carry //= 10
        while carry:
            digits.append(carry % 10)
            carry //= 10
        return digits


class CatalanCalculator:
    def __init__(self, mod: int = 10**9 + 7):
        self.mod = mod
    
    def modular_inverse(self, a: int, p: int) -> int:
        def extended_gcd(a: int, b: int) -> Tuple[int, int]:
            if b == 0:
                return 1, 0
            x1, y1 = extended_gcd(b, a % b)
            x, y = y1, x1 - (a // b) * y1
            return x, y
            
        x, y = extended_gcd(a, p)
        return (x % p + p) % p

    def catalan_combinatorial(self, n: int) -> int:
        catalan = 1
        for i in range(1, n + 1):
            numerator = (2 * n - i + 1) % self.mod
            denominator_inv = self.modular_inverse(i, self.mod)
            catalan = catalan * numerator % self.mod * denominator_inv % self.mod
        return catalan * self.modular_inverse(n + 1, self.mod) % self.mod

    def catalan_formula(self, n: int) -> int:
        catalan = 1
        for i in range(2, n + 1):
            catalan = (catalan * (2 * (2 * i - 1) % self.mod) * self.modular_inverse(i + 1, self.mod)) % self.mod
        return catalan
