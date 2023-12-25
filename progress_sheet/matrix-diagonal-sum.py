class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        summ=0
        l,r=0,len(mat)-1
        row=0
        while l<=r:
            if l==r:
                summ+=mat[row][l]
            else:
                summ+=mat[row][l]+mat[row][r]
            l+=1
            r-=1
            row+=1
        while r>=0:
            summ+=mat[row][l]+mat[row][r]
            r-=1
            l+=1
            row+=1
        return summ