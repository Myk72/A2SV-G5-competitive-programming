class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res=""
        l=0
        for item in spaces:
            res+=s[l:item]+" "
            l=item
        res+=s[l:]
        return res