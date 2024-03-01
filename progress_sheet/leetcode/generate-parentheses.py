class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def backtrack(opened, clos,string):
            if clos==opened==n:
                res.append(string)
                return
            if clos<opened:
                backtrack(opened,clos+1,string+")")
            if opened<n:
                backtrack(opened+1,clos,string+"(")
        backtrack(0, 0,"")
        return res