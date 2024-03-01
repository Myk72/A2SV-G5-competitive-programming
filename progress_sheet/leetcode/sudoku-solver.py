class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        lst=["1","2","3","4","5","6","7","8","9"]
        def backtrack(board):
            for row in range(9):
                for col in range(9):
                    if board[row][col] == '.':
                        for num in lst:
                            if isValid(row, col, num):
                                board[row][col] = num
                                if backtrack(board): 
                                    return True
                                board[row][col] = '.'

                        return False

            return True

        def isValid(row, col, x):
            for k in range(9):
                if board[k][col] == x: 
                    return False
                if board[row][k] == x: 
                    return False
            r = row//3*3
            c = col//3*3
            for i in range(r,r+3):
                for j in range(c,c+3):
                    if board[i][j] == x: return False
            return True

        backtrack(board)
        return board
        