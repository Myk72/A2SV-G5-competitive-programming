class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        tmp=nums[-1]
        count=0
        for i in range(len(nums)-2,-1,-1):
            if tmp<nums[i]:
                sp=math.ceil(nums[i]/tmp)
                count+=sp-1
                tmp=nums[i]//sp
            else:
                tmp=nums[i]
        return count