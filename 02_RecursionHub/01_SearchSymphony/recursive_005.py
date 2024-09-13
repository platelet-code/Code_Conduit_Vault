class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        col = [False] * n
        diag1 = [False] * (2 * n)
        diag2 = [False] * (2 * n)
        result = []

        def dfs(row: int):
            if row == n:
                solution = [''.join(line) for line in board]
                result.append(solution)
                return
            
            for i in range(n):
                if not col[i] and not diag1[row - i + n] and not diag2[row + i]:
                    board[row][i] = 'Q'
                    col[i] = diag1[row - i + n] = diag2[row + i] = True
                    dfs(row + 1)
                    board[row][i] = '.'
                    col[i] = diag1[row - i + n] = diag2[row + i] = False
        
        dfs(0)
        return result
