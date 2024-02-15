class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count=0
        while maxDoubles>0 and target>1:
            count=count+1 if target%2==0 else count+2
            maxDoubles-=1
            target=target//2
        count+=target-1
        return count