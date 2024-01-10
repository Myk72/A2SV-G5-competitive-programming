class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n=0
        t=0
        if name[0]!=typed[0]:return False
        while n<len(name) and t<len(typed):
            if name[n]==typed[t]:
                n+=1
            elif n>0 and name[n]!=typed[t] and typed[t]!=name[n-1]:
                return False
            t+=1
        if n==len(name):
            for item in typed[t:]:
                if item!=name[-1]:return False
            return True
        return False