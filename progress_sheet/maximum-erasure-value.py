class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=r=0
        summ=0
        dic=defaultdict(int)
        mx=0
        while r<len(nums):
            dic[nums[r]]+=1
            summ+=nums[r]
            while dic[nums[r]]>1:
                summ-=nums[l]
                dic[nums[l]]-=1
                l+=1
            mx=max(mx,summ)
            r+=1
        return mx
            
                