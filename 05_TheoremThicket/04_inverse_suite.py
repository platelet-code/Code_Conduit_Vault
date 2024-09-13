def quick_multiply(a: int, b: int, p: int) -> int:
    result = 0
    while b > 0:
        if b & 1:
            result = (result + a) % p
        a = (a + a) % p
        b >>= 1
    return result


def quick_power_mod(base: int, exponent: int, modulus: int) -> int:
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent & 1:
            result = result * base % modulus
        base = base * base % modulus
        exponent >>= 1
    return result


def modular_inverse(a: int, p: int) -> int:
    def extended_gcd(a: int, b: int) -> Tuple[int, int]:
        if b == 0:
            return 1, 0
        x1, y1 = extended_gcd(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        return x, y
        
    x, y = extended_gcd(a, p)
    return (x % p + p) % p


def modular_inverse_fermat(a: int, p: int) -> int:
    return pow(a, p-2, p)


def modular_inverse_euler(a: int, p: int) -> int:
    def phi(x: int) -> int:
        result, i = x, 2
        while i * i <= x:
            if x % i == 0:
                while x % i == 0: x //= i
                result -= result // i
            i += 1
        if x > 1: result -= result // x
        return result
    
    return pow(a, phi(p) - 1, p)


def linear_modular_inverse(n: int, p: int) -> List[int]:
    inv = [0] * (n + 1)
    inv[1] = 1
    for i in range(2, n + 1):
        inv[i] = (p - p // i * inv[p % i]) % p
    return inv[1:]
