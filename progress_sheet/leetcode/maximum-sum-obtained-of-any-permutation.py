class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        curr = [0]*(n+1)
        nums.sort()
        # [1, 2, 3, 4, 5]
        for a,b in requests: 
            curr[a]+= 1 
            curr[b+1]-= 1
        for i in range(1,n): 
            curr[i] += curr[i-1]
        curr.sort()
        # [0, 0, 1, 1, 1, 2]
        res= 0 
        
        for idx,num in enumerate(nums):
            res+=num*curr[idx+1]
        return res%(10**9 + 7)