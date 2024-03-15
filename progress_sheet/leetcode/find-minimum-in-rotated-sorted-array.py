class Solution:
    def findMin(self, nums: List[int]) -> int:
        #binary search
        l,r=0,len(nums)-1
        mini_=nums[0]
        while l<r:
            mid=(l+r)//2
            if nums[mid]>=mini_:
                l=mid+1
            else:
                r=mid
        return nums[l] if mini_>nums[l] else mini_