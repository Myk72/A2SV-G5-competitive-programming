class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        lst=[]
        def backtrack(i,summ):
            if summ == n and len(lst)==k:
                res.append(lst[:])
                return
            if i>=n:return
            j=i
            max_iter=min(10,n+1)
            while j<max_iter:
                if summ+j<=n:
                    lst.append(j)
                    backtrack(j+1,summ+j)
                    lst.pop()
                j+=1

        backtrack(1,0)
        return res
