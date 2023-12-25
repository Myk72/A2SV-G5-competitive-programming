class Solution:
    def maxSum(self, matrix: List[List[int]]) -> int:
        maxsum=-1
        for i in range(len(matrix)-2):
            for j in range(len(matrix[0])-2):
                summ=matrix[i][j]+matrix[i][j+1]+matrix[i][j+2]+matrix[i+1][j+1]+matrix[i+2][j]+matrix[i+2][j+1]+matrix[i+2][j+2]
                maxsum=max(maxsum,summ)
        return maxsum
        