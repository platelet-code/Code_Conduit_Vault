from itertools import product
from typing import List, Tuple
import copy


def solve_switch_puzzle(grid: List[List[str]]) -> List[Tuple[int, int]]:
    def turn_one(x: int, y: int) -> None:
        g[x][y] = '+' if g[x][y] == '-' else '-'
    
    def turn_all(x: int, y: int) -> None:
        for i in range(4):
            turn_one(x, i)
            turn_one(i, y)
        turn_one(x, y)
    
    def get(x: int, y: int) -> int:
        return x * 4 + y

    best = []
    for op in range(1 << 16):
        moves = []
        g = copy.deepcopy(grid)
        for i, j in product(range(4), repeat=2):
            if op & (1 << get(i, j)):
                turn_all(i, j)
                moves.append((i, j))
                
        if all(cell == '-' for row in g for cell in row):
            if not best or len(moves) < len(best):
                best = moves

    return best


def main():
    grid = [list(input().strip()) for _ in range(4)]
    ans = solve_switch_puzzle(grid)
    print(len(ans))
    for x, y in ans:
        print(x + 1, y + 1)


if __name__ == "__main__":
    main()
