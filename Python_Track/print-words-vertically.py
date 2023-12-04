class Solution:
    def printVertically(self, s: str) -> List[str]:
        res=[]
        st=""
        for i in range(len(s)):
            if s[i]!=" ":
                st+=s[i]
            if s[i]==" " or i==len(s)-1:
                res.append(st)
                st=""
        tmp = len(sorted(res, key=len)[-1])
        sec = [""] * tmp
        st = ""
        for i in range(tmp):
            for j in range(len(res)):
                if i >= len(res[j]):
                    st += " "
                else:
                    st += res[j][i]
            l = len(st) - 1
            while st[l] == " ":
                l -= 1
            sec[i] += st[:l + 1]
            st = ""
        return sec
        