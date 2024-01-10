class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(p)
        count=Counter(p)
        res=[]
        window=Counter(s[:n])
        if count == window:
            res.append(0)
        for i in range(n,len(s)):
            window[s[i]] += 1
            window[s[i-n]] -= 1
            if count == window:
                res.append(i-n+1)   
        return res
