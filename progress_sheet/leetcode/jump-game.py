class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res=0
        n=len(nums)
        for idx in range(n):
            if idx <= res:
                res = max(res, idx + nums[idx])
            else:
                return False 
        return res >= n - 1