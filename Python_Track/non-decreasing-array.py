class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:


        for i in range(len(nums)-1):
            if i<len(nums)-2 and nums[i]>nums[i+1] and nums[i]>nums[i+2]:
                nums.pop(i)
                break
            elif nums[i]>nums[i+1]:
                nums.pop(i+1)
                break
        tmp=nums.copy()
        tmp.sort()
        return nums==tmp