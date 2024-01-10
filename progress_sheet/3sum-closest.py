class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        init = nums[1] + nums[2] + nums[0]
        for index, item in enumerate(nums):

            if item == nums[index-1] and index>0:
                continue
            l,r=index+1,len(nums)-1

            while l<r:
                summ=nums[l]+nums[r]+item
                clos=abs(target-summ)
                if clos < abs(target-init):
                    init = summ
                if summ>target:
                    r-=1
                elif summ<target:
                    l+=1
                else:
                    return summ

        return init
        