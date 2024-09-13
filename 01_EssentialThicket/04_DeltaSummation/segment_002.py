from collections import defaultdict

def main():
    cnt = defaultdict(int)
    n, k = map(int, input().split())
    
    modulus = 0
    
    for _ in range(n):
        x = int(input())
        modulus = (modulus + x) % k
        cnt[modulus] += 1
    
    ret = 0
    for val in cnt.values():
        ret += val * (val - 1) // 2
    ret += cnt[0]
    print(ret)


if __name__ == "__main__":
    main()
