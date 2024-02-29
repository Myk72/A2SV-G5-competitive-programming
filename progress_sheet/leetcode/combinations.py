class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        lst=[]
        def backtrack(i):
            if len(lst) == k:
                res.append(lst[:])
                return
            if i>n:
                return
            lst.append(i)
            backtrack(i+1)
            lst.pop()
            backtrack(i+1)
        backtrack(1)
        return res