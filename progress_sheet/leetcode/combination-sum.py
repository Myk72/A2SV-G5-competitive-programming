class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        lst=[]
        def backtrack(i,summ):
            if i>=len(candidates):return
            if summ == target:
                res.append(lst[:])
                return
            for i in range(i,len(candidates)):
                if summ+candidates[i]<=target:
                    lst.append(candidates[i])
                    backtrack(i,summ+candidates[i])
                    lst.pop()
                # backtrack(i+1,candidates[i])
        backtrack(0,0)
        return res