class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr=0
        minm=float('inf')
        r=l=0
        while r<len(nums) and l<len(nums):
            while r<len(nums) and curr+nums[r]<target:
                curr+=nums[r]
                r+=1
            if r==len(nums):break
            if curr+nums[r]>=target:
                minm=min(minm,r-l+1)
                curr-=nums[l]
                l+=1
        return minm if minm !=float('inf') else 0