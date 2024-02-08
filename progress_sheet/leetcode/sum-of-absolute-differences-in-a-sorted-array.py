class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        left,right=0,sum(nums)
        for idx,num in enumerate(nums):
            tot=right-num*(n-idx)-(left-num*idx)
            res[idx]=tot
            right-=num
            left+=num
        return res
