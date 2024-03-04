class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["."] * n for i in range(n)]
        res=0
        cols = set()
        def check_diag(row,col):
            a,b=row,col
            while a >= 0 and b >= 0 :
                if board[a][b] == "Q" :
                    a,b=row,col
                    return False
                a -= 1
                b -= 1
            a,b=row,col
            while a >-1 and b<n :
                if board[a][b] == "Q" :
                    return False
                a -= 1
                b += 1
            return True

        def NQueen(row):
            nonlocal res
            if row == n:
                res+=1
                return

            for col in range(n):
                if col not in cols and check_diag(row,col):
                    cols.add(col)
                    board[row][col] = "Q"
                    NQueen(row + 1)
                    board[row][col] = "."
                    cols.remove(col)

        NQueen(0)
        return res