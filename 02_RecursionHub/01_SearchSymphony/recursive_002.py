def main():
    n, m = map(int, input().split())
    
    def dfs(u: int, cnt: int, used: int) -> None:
        if cnt == m:
            subset = [str(i + 1) for i in range(n) if used >> i & 1]
            print(" ".join(map(str, subset)))
            return
        
        if n - u + cnt < m:
            return
        
        if u == n:
            return
        
        dfs(u + 1, cnt + 1, used | (1 << u))
        dfs(u + 1, cnt, used)
    
    dfs(0, 0, 0)

if __name__ == "__main__":
    main()



def main():
    n, m = map(int, input().split())
    subset = []
    
    def dfs(u: int, start: int) -> None:
        if u == m:
            print(" ".join(map(str, subset)))
            return
        
        if n - u + start < m:
            return
        
        for i in range(start, n):
            subset.append(i + 1)
            dfs(u + 1, i + 1)
            subset.pop()
    
    dfs(0, 0)

if __name__ == "__main__":
    main()
