class Solution:
    def numberOfWays(self, s: str) -> int:
        res=0
        pre1=pre0=0
        post0=post1=0
        for char in s:
            if char=="0":
                post0+=1
            else:
                post1+=1
        for idx,char in enumerate(s):
            if char=="0":
                res+=pre1*(post1)
                pre0+=1
                post0-=1
            else:
                res+=pre0*(post0)
                pre1+=1
                post1-=1
        return res