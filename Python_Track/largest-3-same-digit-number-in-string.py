class Solution:
    def largestGoodInteger(self, num: str) -> str:
        l,r=0,2
        maxi=""
        while r<len(num):
            if num[l]==num[l+1]==num[r]:
                maxi=max(maxi,num[l:r+1])
            l+=1
            r+=1
        return maxi
        