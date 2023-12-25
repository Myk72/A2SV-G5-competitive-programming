class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        res=defaultdict(list)
        ans=[]
        for i in range(row):
            for j in range(col):
                res[i+j].append(matrix[i][j])
    # {0: [1], 1: [2, 4], 2: [3, 5, 7], 3: [6, 8], 4: [9]}
        flag=False
        for value in res.values():
            if not flag:
                for item in value[::-1]:
                    ans.append(item)
                flag=True
            else:
                for item in value:
                    ans.append(item)
                flag=False
        return ans