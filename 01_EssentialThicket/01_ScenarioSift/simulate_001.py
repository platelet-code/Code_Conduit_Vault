import copy
from typing import List

def solve_light_puzzle(grid: List[List[str]]) -> int:
    n, m = len(grid), len(grid[0])
    dx = [1, 0, 0, 0, -1]
    dy = [0, 1, 0, -1, 0]
    
    def turn(x: int, y: int) -> None:
        for i in range(5):
            xi, yi = x + dx[i], y + dy[i]
            if 0 <= xi < n and 0 <= yi < m:
                g[xi][yi] = '0' if g[xi][yi] == '1' else '1'
                
    ret = float('inf')
    
    for op in range(1 << m):
        g = copy.deepcopy(grid)
        step = bin(op).count("1")
        
        for i in range(m):
            if op >> i & 1:
                turn(0, i)
        
        for i in range(n - 1):
            for j in range(m):
                if g[i][j] == '0':
                    turn(i + 1, j)
                    step += 1
        
        if all(cell == '1' for row in g for cell in row):
            ret = min(ret, step)
    
    return ret if ret <= 6 else -1


def main():
    n = int(input().strip())
    for _ in range(n):
        grid = []
        while len(grid) < 5:
            line = input().strip()
            if line:
                grid.append(list(line))
        result = solve_light_puzzle(grid)
        print(result)


if __name__ == "__main__":
    main()