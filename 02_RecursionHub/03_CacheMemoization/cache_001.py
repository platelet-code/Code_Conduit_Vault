from functools import lru_cache

def main():
    T = int(input())
    for _ in range(T):
        n, m = map(int, input().split())
        weights = []
        for __ in range(n):
            row = list(map(int, input().split()))
            weights.append(row)

        @lru_cache(None)
        def dfs(r: int, c: int) -> int:
            if r >= n or c >= m:
                return 0
            return max(dfs(r + 1, c), dfs(r, c + 1)) + weights[r][c]

        print(dfs(0, 0))


if __name__ == "__main__":
    main()
