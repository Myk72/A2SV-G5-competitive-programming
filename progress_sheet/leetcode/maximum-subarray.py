class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        res=mx=nums[0]
        for i in range(1, len(nums)):
            res=max(nums[i],nums[i]+res)
            if res>mx:
                mx=res
        return mx
        