class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt=defaultdict(int)
        l=0
        maxi=0
        for i in range(len(nums)):
            cnt[nums[i]]+=1
            if cnt[0]>1:
                cnt[nums[l]]-=1
                l+=1
            maxi=max(maxi,i-l)
        return maxi