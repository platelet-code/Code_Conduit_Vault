from functools import lru_cache

def main():
    n, m = map(int, input().split())
   
    @lru_cache(None)
    def can_make(x: int) -> bool:
        if x < min(n, m):
           return False
        
        if x == n or x == m:
            return True
        
        return can_make(x - n) or can_make(x - m)
    
    for i in range(n * m):
        if not can_make(i):
            if all(can_make(j) for j in range(i + 1, i + max(n, m) + 1)):
                print(i)
                break

        
if __name__ == "__main__":
    main()
