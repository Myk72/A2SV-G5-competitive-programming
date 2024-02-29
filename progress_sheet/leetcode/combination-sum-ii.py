class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        lst=[]
        def backtrack(i,summ):
            if summ == target:
                # if lst not in res:
                res.append(lst[:])
                return
            if i>=len(candidates):return
            # print(candidates)
            j=i
            while j<len(candidates):

                if summ+candidates[j]<=target:
                    lst.append(candidates[j])
                    backtrack(j+1,summ+candidates[j])
                    lst.pop()
                while j+1<len(candidates) and candidates[j]==candidates[j+1]:
                    j+=1
                j+=1
                # backtrack(j+1,summ+candidates[j])
                # summ=0

        backtrack(0,0)
        return res