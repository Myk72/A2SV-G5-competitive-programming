class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res=0
        count=Counter(nums)
        for item in count:
            res+=count[item]*(count[item]-1)//2
        return res
        