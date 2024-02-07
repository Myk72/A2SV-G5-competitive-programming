class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row=len(matrix)
        col=len(matrix[0])
        arr= [[0 for x in range(col)] for y in range(row)] 
        arr[0][0] = matrix[0][0]
        for i in range(1, col) :
            arr[0][i] = (arr[0][i - 1] + matrix[0][i])
        for i in range(1, row) :
            arr[i][0] = (arr[i - 1][0] + matrix[i][0])
        for i in range(1, row) :
            for j in range(1, col) :
                arr[i][j] = (arr[i - 1][j] + arr[i][j - 1] -arr[i - 1][j - 1] +
                            matrix[i][j])
        self.array=arr

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 != 0 and col1 != 0:
            return self.array[row2][col2] - self.array[row1 - 1][col2] - self.array[row2][col1 - 1] + self.array[row1 - 1][col1 - 1]
            
        elif row1 == 0 and col1 == 0:
            return self.array[row2][col2]

        elif row1 == 0:
            return self.array[row2][col2] - self.array[row2][col1 - 1] 

        elif col1 == 0:
            return self.array[row2][col2] - self.array[row1 - 1][col2]            

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)