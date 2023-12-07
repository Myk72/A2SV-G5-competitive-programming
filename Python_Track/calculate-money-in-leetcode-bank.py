class Solution:
    def totalMoney(self, n: int) -> int:
        curr=0
        res=[0]*7
        for i in range(n):
            if i<7:
                curr+=1
                res[i]+=curr
                if i==6:
                    tmp=res.copy()
            else:
                index=i%7
                x=i//7
                if index==0:
                    curr=tmp[0]+x
                else:
                    curr+=1
                res[index]+=curr
        return sum(res)
        