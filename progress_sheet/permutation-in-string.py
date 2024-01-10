class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m=len(s1),len(s2)
        if n>m:
            return False
        cnt=Counter(s1)
        wind=Counter(s2[:n-1])
        l=0
        for i in range(n-1,m):
            wind[s2[i]]+=1
            if cnt==wind:
                return True
            wind[s2[l]]-=1
            l+=1
        return False