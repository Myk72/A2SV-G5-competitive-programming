class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        
        for i in range(1, cols) :
            matrix[0][i]+=matrix[0][i - 1]
        for i in range(1, rows) :
            matrix[i][0] += matrix[i - 1][0]
        for i in range(1, rows) :
            for j in range(1, cols) :
                matrix[i][j] += matrix[i - 1][j] + matrix[i][j - 1] -matrix[i - 1][j - 1]
        
        res = 0
        for i in range(rows):
            for j in range(i, rows):

                mp = defaultdict(int)
                curr, mp[0] = 0, 1

                for k in range(cols):
                    curr = matrix[j][k] - (matrix[i - 1][k] if i > 0 else 0)
                    res += mp[curr - target]
                    mp[curr] += 1

        return res