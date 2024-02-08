class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        uniq=len(set(nums))
        count=defaultdict(int)
        cnt=l=0
        for idx,num in enumerate(nums):
            count[num]+=1
            while len(count)==uniq:
                cnt+=len(nums)-idx
                count[nums[l]]-=1
                if count[nums[l]]==0:
                    del count[nums[l]]
                l+=1
        return cnt