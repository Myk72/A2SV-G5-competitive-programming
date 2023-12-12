class Solution:
    def reverseWords(self, s: str) -> str:
        x=s.split()
        res=""
        for i in range(len(x)-1,-1,-1):
            if i!=0:
                res+=x[i]+" "
            else:
                res+=x[i]
        return res.strip()