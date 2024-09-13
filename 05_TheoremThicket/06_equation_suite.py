def solve_linear_congruence(a: int, b: int, m: int) -> int:
    def extended_gcd(a: int, b: int) -> Tuple[int, int]:
        if b == 0:
            return 1, 0
        x1, y1 = extended_gcd(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        return x, y
        
    from math import gcd
    d = gcd(a, m)
    if b % d != 0:
        return -1
    a, b, m = a // d, b // d, m // d
    x, _ = extended_gcd(a, m)
    x = (x * b % m + m) % m
    return x


def chinese_remainder_theorem(equations: List[Tuple[int, int]]) -> int:
    def extended_gcd(a: int, b: int) -> Tuple[int, int]:
        if b == 0:
            return 1, 0
        else:
            x1, y1 = extended_gcd(b, a % b)
            x, y = y1, x1 - (a // b) * y1
            return x, y
            
    x, M = 0, 1
    for modulus, _ in equations:
        M *= modulus
    for modulus, remainder in equations:
        Mi = M // modulus
        mi_inverse, _ = extended_gcd(Mi, modulus)
        x = (x + Mi * mi_inverse * remainder) % M
    return x if x >= 0 else x + M


def extended_chinese_remainder_theorem(m: List[int], a: List[int]) -> int:
    def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
        if b == 0:
            return a, 1, 0
        gcd, x, y = extended_gcd(b, a % b)
        return gcd, y, x - (a // b) * y

    def merge_equation(m1: int, r1: int, m2: int, r2: int) -> Tuple[int, int]:
        gcd, p, q = extended_gcd(m1, m2)
        if (r2 - r1) % gcd:
            return 0, 0
        lcm = m1 // gcd * m2
        r = (r1 + (r2 - r1) * p * (m1 // gcd)) % lcm
        return lcm, r

    lcm, r = m[0], a[0]
    for i in range(1, len(m)):
        lcm, r = merge_equation(lcm, r, m[i], a[i])
        if lcm == 0:
            return -1
    return r


def xor_gaussian_elimination(matrix: List[List[int]]) -> Union[List[int], str]:
    n = len(matrix)
    for i in range(n):
        if matrix[i][i] == 0:
            for j in range(i + 1, n):
                if matrix[j][i] == 1:
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
            else: continue
        for j in range(i + 1, n):
            if matrix[j][i] == 1:
                for k in range(i, n + 1): matrix[j][k] ^= matrix[i][k]
    
    for i in range(n - 1, -1, -1):
        if matrix[i][i] == 0:
            if matrix[i][n] == 1: return "No solution"
            continue
        for j in range(i): 
            if matrix[j][i] == 1: matrix[j][n] ^= matrix[i][n]
    
    if any(all(row[j] == 0 for j in range(i, n)) and row[n] == 0 for i, row in enumerate(matrix)):
        return "Multiple sets of solutions"
    
    return [row[n] for row in matrix]


def linear_gaussian_elimination(matrix: List[List[float]], epsilon=1e-6) -> Union[List[float], str]:
    n, m = len(matrix), len(matrix[0]) - 1
    col = row = 0
    for col in range(m):
        pivot = max(range(row, n), key=lambda i: abs(matrix[i][col]))
        if abs(matrix[pivot][col]) < epsilon:
            continue
        matrix[row], matrix[pivot] = matrix[pivot], matrix[row]
        for i in range(row + 1, n):
            factor = matrix[i][col] / matrix[row][col]
            for j in range(col, m + 1):
                matrix[i][j] -= factor * matrix[row][j]
        
        row += 1
        if row == n:
            break
    
    if any(abs(matrix[i][m]) > epsilon for i in range(row, n)):
        return "No solution"
    
    if row < m:
        return "Infinite group solutions"
    
    solution = [0.0] * m
    for i in range(row - 1, -1, -1):
        solution[i] = (matrix[i][m] - sum(matrix[i][j] * solution[j] for j in range(i + 1, m))) / matrix[i][i]
    return solution
