from functools import lru_cache

def main():
    n, m, k = map(int, input().split())
    MOD = 10**9 + 7
    treasures = [list(map(int, input().split())) for _ in range(n)]
    
    @lru_cache(None)
    def dfs(i: int, j: int, cnt: int, last_val: int) -> int:
        if i == n or j == m:
            return 0
        
        if i == n - 1 and j == m - 1:
            if (cnt == 1 and last_val < treasures[i][j]) or cnt == 0:
                return 1
            return 0
        
        ways = dfs(i + 1, j, cnt, last_val) + dfs(i, j + 1, cnt, last_val)
        
        if cnt > 0 and last_val < treasures[i][j]:
            ways += dfs(i + 1, j, cnt - 1, treasures[i][j]) + dfs(i, j + 1, cnt - 1, treasures[i][j])
        
        return ways % MOD
    
    print(dfs(0, 0, k, -1))
    
    
if __name__ == "__main__":
    main()



from collections import defaultdict

def main():
    n, m, k = map(int, input().split())
    MOD = 10**9 + 7
    treasures = [list(map(int, input().split())) for _ in range(n)]
    memo = defaultdict(int)
    

    def dfs(i: int, j: int, cnt: int, last_val: int) -> int:
        if i == n or j == m:
            return 0
        
        if i == n - 1 and j == m - 1:
            if (cnt == 1 and last_val < treasures[i][j]) or cnt == 0:
                return 1
            return 0
        
        key = (i, j, cnt, last_val)
        if key in memo:
            return memo[key]
        
        ways = dfs(i + 1, j, cnt, last_val) + dfs(i, j + 1, cnt, last_val)
        
        if cnt > 0 and last_val < treasures[i][j]:
            ways += dfs(i + 1, j, cnt - 1, treasures[i][j]) + dfs(i, j + 1, cnt - 1, treasures[i][j])
        
        ways %= MOD
        memo[key] = ways
        return ways
    
    print(dfs(0, 0, k, -1))
    
    
if __name__ == "__main__":
    main()
