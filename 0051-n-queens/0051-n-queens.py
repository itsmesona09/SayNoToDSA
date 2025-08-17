class Solution:
    def isSafe(self, board, row, col, n):
        # to check previous row values by reducing col
        i = col
        while i >= 0:
            if board[row][i] == "Q":
                return False
            i -= 1
        
        # to check upper diagonal
        i = col
        j = row
        while i >= 0 and j >= 0:
            if board[j][i] == "Q":
                return False
            i -= 1
            j -= 1

        # to check lower diagonal
        i = col
        j = row
        while i >= 0 and j < n:
            if board[j][i] == "Q":
                return False
            i -= 1
            j += 1

        return True

    def solve(self, board, col, n, res):
        if col >= n:
            res.append(["".join(row) for row in board])
            return

        for row in range(n):
            if self.isSafe(board, row, col, n):
                board[row][col] = "Q"
                self.solve(board, col + 1, n, res)
                board[row][col] = "."
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        self.solve(board, 0, n, res)
        return res