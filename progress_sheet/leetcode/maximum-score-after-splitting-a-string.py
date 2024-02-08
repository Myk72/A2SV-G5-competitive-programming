class Solution:
    def maxScore(self, s: str) -> int:
        res=0
        count=s.count('1')
        zero=0
        for num in s[:-1]:
            if num=="0":
                zero+=1
            else:
                count-=1
            res=max(res,zero+count)
        return res