class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        ave=(sum(nums[:k]))/k
        tmp=ave
        for i in range(k,len(nums)):
            tmp-=(nums[l]/k)
            tmp+=(nums[i]/k)
            ave=max(tmp,ave)
            l+=1
        return ave