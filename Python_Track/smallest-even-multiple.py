class Solution(object):
    def smallestEvenMultiple(self, nums):
        """
        :type n: int
        :rtype: int
        """
        if nums%2==0:
            return nums
        else:
            return nums*2
        