def main():
    n = int(input())
    
    def dfs(u: int, used: int, permutation: list) -> None:
        if u == n:
            print(" ".join(map(str, permutation)))
            return
        
        for i in range(n):
            if not (used >> i & 1):
                dfs(u + 1, used + (1 << i), permutation + [i + 1])
    
    dfs(0, 0, [])


if __name__ == "__main__":
    main()



def main():
    from collections import defaultdict
    vis = defaultdict(bool)
    answer = []
    n = int(input())
    
    def dfs(u: int) -> None:
        if u == n:
            print(" ".join(map(str, answer)))
            return
        
        for i in range(n):
            if not vis[i]:
                vis[i] = True
                answer.append(i + 1)
                dfs(u + 1)
                answer.pop()
                vis[i] = False
    
    dfs(0)
    

if __name__ == "__main__":
    main()
