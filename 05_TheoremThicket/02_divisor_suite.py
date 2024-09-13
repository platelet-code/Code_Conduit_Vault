def divide(x: int) -> List[int]:
    ans = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            ans.append(i)
            if i != x // i:
                ans.append(x // i)         
    return sorted(ans)


def calculate_divisors_product(numbers: List[int], mod=10**9+7) -> int:
    from functools import reduce
    prime = dict()
    for x in numbers:
        for i in range(2, int(x**0.5) + 1):
            while x % i == 0: 
                x //= i; 
                prime[i] = prime.get(i, 0) + 1
        if x > 1: 
            prime[x] = prime.get(x, 0) + 1
    return reduce(lambda x, y: x * y % mod, (v + 1 for v in prime.values()), 1)


def sum_of_divisors(numbers: List[int], modulus=10**9+7) -> int:
    from collections import defaultdict
    prime_counts = defaultdict(int)
    
    for num in numbers:
        for i in range(2, int(num**0.5) + 1):
            while num % i == 0:
                num //= i
                prime_counts[i] += 1
        if num > 1:
            prime_counts[num] += 1
    
    ans = 1
    for prime, count in prime_counts.items():
        divisor_sum = sum((pow(prime, i, modulus) for i in range(1, count + 1)), 1)
        ans = ans * divisor_sum % modulus
    
    return ans


def compute_gcd_lcm(a: int, b: int) -> int:
    def euclidean_gcd(x: int, y: int) -> int:
        while y:
            x, y = y, x % y
        return x
      
    gcd = euclidean_gcd(a, b)
    lcm = a * b // gcd if gcd != 0 else 0
    return gcd, lcm


def is_perfect_number(x: int) -> bool:
    perfect_numbers = [6, 28, 496, 8128, 33550336, 8589869056, 137438691328]
    return x in perfect_numbers


def count_divisibles(n: int, primes: List[int]) -> int:
    m = len(primes)
    result = 0
    
    for i in range(1, 1 << m):
        subset_product = 1
        bits_count = bin(i).count('1')
        
        for j in range(m):
            if i & (1 << j):
                if subset_product > n // primes[j]:
                    subset_product = -1
                    break
                subset_product *= primes[j]

        if subset_product != -1:
            if bits_count % 2:
                result += n // subset_product
            else:
                result -= n // subset_product
    
    return result
