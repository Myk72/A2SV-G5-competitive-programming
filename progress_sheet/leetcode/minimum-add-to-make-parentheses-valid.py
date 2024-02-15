class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        count=0
        r=0
        for char in s:
            if char=="(":
                r+=1
            else:
                if r>0:
                    r-=1
                else:
                    count+=1
        count+=r
        return count
