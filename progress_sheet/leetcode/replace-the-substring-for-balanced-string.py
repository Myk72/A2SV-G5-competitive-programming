class Solution:
    def balancedString(self, s: str) -> int:
        count={"Q":0,"E":0,"W":0,"R":0}
        n= len(s) // 4
        l = 0
        res = len(s)
        for char in s:
            count[char]+=1
        for r,char in enumerate(s):
            count[char]-= 1
            while l < len(s) and count["Q"]<=n and count["R"]<=n and count["W"]<=n and count["E"]<=n :
                count[s[l]] += 1
                res = min(res, r - l + 1)
                l += 1
        return res