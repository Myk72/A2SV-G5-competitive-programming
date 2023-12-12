class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashm={}
        for index,item in enumerate(nums):
            if target-item in hashm:
                return [hashm[target-item],index]
            hashm[item]=index
        