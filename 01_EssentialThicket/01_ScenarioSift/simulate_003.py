from collections import defaultdict

def main():
    n = int(input())
    sqrt_n = int(n ** 0.5)
    sum_pairs = defaultdict(list)
    
    for a in range(sqrt_n + 1):
        for b in range(a, sqrt_n + 1):
            sum_ab = a * a + b * b
            if sum_ab <= n:
                sum_pairs[sum_ab].append((a, b))
    
    for a in range(sqrt_n + 1):
        for b in range(sqrt_n + 1):
            target = n - a * a - b * b
            if target in sum_pairs:
                c, d = sum_pairs[target][0][0], sum_pairs[target][0][1]
                quadruplet = sorted([a, b, c, d])
                print(*quadruplet)
                return

if __name__ == "__main__":
    main()