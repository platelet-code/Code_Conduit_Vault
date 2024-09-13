def is_prime(n: int) -> bool:
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


def miller_rabin(n: int, k=10) -> bool:
    import random
    if n <= 1: return False
    if n in (2, 3): return True
    if n % 2 == 0: return False
    
    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    def witness(a: int) -> bool:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return False
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                return False
        return True

    return not any(witness(random.randint(2, n - 2)) for _ in range(k))


def prime_factors(x: int) -> List[Tuple[int, int]]:
    result = []
    factor = 2
    while factor * factor <= x:
        count = 0
        while x % factor == 0:
            x //= factor
            count += 1
        if count > 0:
            result.append((factor, count))
        factor += 1

    if x > 1:
        result.append((x, 1))

    return result


def sieve_of_eratosthenes(n: int) -> List[int]:
    is_prime = [True] * (n + 1)
    
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
                
    primes = [p for p in range(2, n + 1) if is_prime[p]]
    return primes


def sieve_of_euler(n: int) -> List[int]:
    vis = [False] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if not vis[i]: primes.append(i)
        for j in primes:
            if j * i > n: break
            vis[j * i] = True
            if i % j == 0: break
    return primes
