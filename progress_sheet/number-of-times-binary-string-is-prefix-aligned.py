class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        arr=[0]*len(flips)
        count=0
        summ=0
        maxi=0
        for i in range(len(flips)):
            summ+=1
            maxi=max(maxi,flips[i]) 
            if summ==maxi:
                count+=1
        return count