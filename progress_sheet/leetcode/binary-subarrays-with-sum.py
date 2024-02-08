class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mp=defaultdict(int)
        mp[0]=1
        res,curr=0,0
        for num in nums:
            curr += num
            res+= mp[curr - goal]
            mp[curr] += 1
        return res