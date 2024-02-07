class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        curr=0
        total=sum(nums)
        for i in range(len(nums)):
            total-=nums[i]
            if curr==total:
                return i
            curr+=nums[i]
        return -1
        