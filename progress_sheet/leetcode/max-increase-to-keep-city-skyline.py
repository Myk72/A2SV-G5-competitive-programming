class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n=len(grid)
        res=[0]*n
        ans=[0]*n
        count=0
        for i in range(n):
            res[i]=max(grid[i])
            max_=0
            for j in range(n):
                max_=max(grid[j][i],max_)
            ans[i]=max_

        for i in range(n):
            for j in range(n):
                # print(min(ans[j],res[i]))
                count+=min(ans[j],res[i])-grid[i][j]
        # print(ans)
        return count
