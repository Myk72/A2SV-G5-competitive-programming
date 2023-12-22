class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix[0])-1,-1,-1):
            l,r=0,len(matrix)-1
            while l<r:
                matrix[l][i],matrix[r][i]=matrix[r][i],matrix[l][i]
                r-=1
                l+=1
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i<=j:
                    matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        