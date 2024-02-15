class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        count=pref=i=0
        for i in range(len(nums)):
            while nums[i]>pref+1:
                count+=1
                pref+=(pref+1)
                if pref>=n:
                    return count
            else:
                pref+=nums[i]
            
            if pref>=n:
                return count
        while pref<n:
            count+=1
            pref+=(pref+1)
        return count