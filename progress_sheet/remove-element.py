class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l,r=0,len(nums)-1
        if val not in nums:return len(nums)
        while l<r:
            while l<r and nums[l]!=val:
                l+=1
            if nums[r]!=val:
                nums[r],nums[l]=nums[l],nums[r]
            else:   
                r-=1
        return l
