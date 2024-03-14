class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if target == nums[mid]:
                while r>-1 and nums[r]!=target:
                    r-=1
                while l<n and nums[l]!=target:
                    l+=1
                if r>-1 and l<n and nums[l]==nums[r]:
                    return [l,r]
            elif target<nums[mid]:
                r=mid-1
            else:
                l=mid+1
    
        return [-1,-1]
        