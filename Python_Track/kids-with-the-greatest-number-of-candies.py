class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        Max=max(candies)
        res=[]
        for item in candies:
            if item+extraCandies>=Max:
                res.append(True)
            else:
                res.append(False)
        return res
        