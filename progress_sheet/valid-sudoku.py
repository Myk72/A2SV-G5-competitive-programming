class Solution:
    def isValidSudoku(self, matrix: List[List[str]]) -> bool:
        for i in range(9):
            rs=[]
            rs2=[]
            for j in range(9):
                if matrix[i][j]!="." and matrix[i][j] not in rs:
                    rs.append(matrix[i][j])
                elif matrix[i][j]!="." and matrix[i][j] in rs:
                    return False
                if matrix[j][i]!="." and matrix[j][i] not in rs2:
                    rs2.append(matrix[j][i])
                elif matrix[j][i]!="." and matrix[j][i] in rs2:
                    return False
        c,r=0,0
        for i in range(3):
            for j in range(3):
                res=[]
                for k in range(3):
                    for l in range(3):
                        mat=matrix[k+r][c+l]
                        if mat!="." and mat not in res:
                            res.append(mat)
                        
                        elif mat!="." and mat in res:
                            return False
                c+=3
            r+=3
            c=0
        return True   