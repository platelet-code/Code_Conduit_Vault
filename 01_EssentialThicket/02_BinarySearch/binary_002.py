def main():
    n, k = map(int, input().split())
    cakes = []
    for _ in range(n):
        x, y = map(int, input().split())
        cakes.append((x, y))
    
    def is_red(x: int) -> bool:
        cnt = 0
        for a, b in cakes:
            cnt += (a // x) * (b // x)
        return cnt >= k
    
    left, right = 1, 10 ** 5 + 10
    while left < right:
        pivot = (left + right + 1) // 2
        if is_red(pivot):
            left = pivot
        else:
            right = pivot - 1
    
    print(left)


if __name__ == "__main__":
    main()
