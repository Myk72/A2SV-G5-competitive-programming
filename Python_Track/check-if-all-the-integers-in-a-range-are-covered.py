class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ran={i for i in range(left,right+1)}
        for a,b in ranges:
            st=set(range(a,b+1))
            ran=ran.difference(st)
        return len(ran)==0