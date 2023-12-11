class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        arr = []
        even_sum=0
        for i in nums:
            if i%2==0:even_sum+=i
        for a,b in queries:
            if nums[b]%2==0:even_sum-=nums[b]
            nums[b]+=a
            if nums[b]%2==0:even_sum+=nums[b]
            arr.append(even_sum)
        return arr