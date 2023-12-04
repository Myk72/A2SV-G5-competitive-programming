class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l=0
        Max=float('-inf')
        for r in range(len(nums)):
            if nums[r]==1:
                Max=max(Max,r-l+1)
            else:
                l=r+1
        return Max if Max>0 else 0
        