class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        n=len(processorTime)
        maxi=0
        for i in range(n):
            maxi=max(maxi,processorTime[i]+tasks[4*(i+1)-1])
        return maxi 