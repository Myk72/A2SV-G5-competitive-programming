class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      n=len(nums)+1
      totalsum=n*(n-1)//2
      return totalsum-sum(nums)
        