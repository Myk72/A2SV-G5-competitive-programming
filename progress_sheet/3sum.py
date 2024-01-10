class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for index, item in enumerate(nums):
            if item == nums[index-1] and index>0:
                continue
            l,r=index+1,len(nums)-1
            while l<r:
                if nums[l]+nums[r]+item>0:
                    r-=1
                elif nums[l]+nums[r]+item<0:
                    l+=1
                else:
                    result.append([item,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return result
        