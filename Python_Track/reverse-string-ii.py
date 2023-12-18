class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l=0
        r=len(s)
        res=""
        while l<r:
            #abcd
            if r-l>=2*k:
                res+=s[l:l+k][::-1]+s[l+k:l+2*k]
            elif r-l<2*k and r-l>=k:
                res+=s[l:l+k][::-1]+s[l+k:r]
            else:
                res+=s[l:r][::-1]
            l+=2*k
        return res