class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res=""
        for i in range(len(s)):
            idx=indices.index(i)
            res+=s[idx]
        return res