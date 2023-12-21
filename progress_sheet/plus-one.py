class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=0
        for item in digits:
            res=res*10+item
        res+=1
        return [int(item) for item in str(res)]
            