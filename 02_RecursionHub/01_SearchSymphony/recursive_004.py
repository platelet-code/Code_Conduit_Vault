def check(a: int, c: int) -> bool:
    b = (n - a) * c
    if a == 0 or b == 0 or c == 0:
        return False
        
    backup = vis[:]
    
    while b:
        x = b % 10
        b //= 10
        if x == 0 or backup[x - 1]:
            return False
        backup[x - 1] = True
        
    return all(c for c in backup)
    

def dfs_c(u: int, a: int, c: int) -> None:
    global cnt
    if u == 8:
        return
    
    if check(a, c):
        cnt += 1
    
    for i in range(9):
        if not vis[i]:
            vis[i] = True
            dfs_c(u + 1, a, c * 10 + (i + 1))
            vis[i] = False
            

def dfs_a(u: int, a: int) -> None:
    if a >= n:
        return
    
    if u == 7:
        return
    
    if a:
        dfs_c(u, a, 0)
    
    for i in range(9):
        if not vis[i]:
            vis[i] = True
            dfs_a(u + 1, a * 10 + (i + 1))
            vis[i] = False


if __name__ == "__main__":
    n = int(input())
    vis = [False] * 9
    cnt = 0
    dfs_a(0, 0)
    print(cnt)
