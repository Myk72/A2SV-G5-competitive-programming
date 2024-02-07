class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr_sum=0
        for i in range(len(nums)):
            nums[i]+=curr_sum
            curr_sum=nums[i]
        return nums