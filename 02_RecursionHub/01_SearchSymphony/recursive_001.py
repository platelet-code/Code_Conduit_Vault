def main():
    n = int(input())
    def dfs(u: int, used: int) -> None:
        if u == n:
            subset = [str(i + 1) for i in range(n) if (used >> i & 1)]
            print(" ".join(subset))
            return

        dfs(u + 1, used)
        dfs(u + 1, used + (1 << u))

    dfs(0, 0)


if __name__ == "__main__":
    main()



from collections import defaultdict

def main():
    n = int(input())
    used = defaultdict(bool)
    
    def dfs(u: int) -> None:
        if u == n:
            subset = [str(i + 1) for i in range(n) if used[i]]
            print(" ".join(subset))
            return
        
        dfs(u + 1)
        
        used[u] = True
        dfs(u + 1)
        used[u] = False
        
    dfs(0)

if __name__ == "__main__":
    main()
