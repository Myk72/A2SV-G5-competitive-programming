class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(1, n):
            tmp = nums[i]
            prev = i - 1
            while prev >= 0 and nums[prev] > tmp:
                nums[prev + 1] = nums[prev]
                prev -= 1

            nums[prev+ 1] = tmp
        