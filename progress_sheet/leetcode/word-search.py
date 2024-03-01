class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        visited = [[False] * col for i in range(row)]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        def check(x, y, idx):
            if idx==len(word):
                return True
            for a,b in directions:
                a=a+x
                b=b+y
                if 0 <= a < row and 0 <= b < col:
                    if not visited[a][b] and board[a][b]==word[idx]:
                        visited[a][b]=True
                        # print(a+x,b+y,idx)
                        if check(a, b, idx+1):
                            return True
                        visited[a][b]=False
            return False
        for i in range(row):
            for j in range(col):
                if board[i][j]==word[0]:
                    visited[i][j] = True
                    if check(i, j, 1): 
                        return True
                visited[i][j] = False

        return False
