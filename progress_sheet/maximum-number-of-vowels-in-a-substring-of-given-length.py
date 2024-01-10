class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        mp={'a', 'e', 'i', 'o','u'}
        l=cnt=0
        for i in range(k):
            if s[i] in mp:
                cnt+=1
        maxi=cnt
        for i in range(k,len(s)):
            if s[i] in mp:
                cnt+=1
            if s[l] in mp:
                cnt-=1
            maxi=max(maxi,cnt)
            l+=1
        return maxi