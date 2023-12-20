class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count=0
        dict=defaultdict(list)
        for a,b in enumerate(nums):
            dict[b].append(a)
        for arr in dict.values():
            for index,i in enumerate(arr):
                for j in arr[index+1:]:
                    if (i*j)%k==0:count+=1
        return count