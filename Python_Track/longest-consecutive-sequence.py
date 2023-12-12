class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dic={i for i in nums}
        mx=0
        for item in dic:
            count=0 # initialization of length
            # we need to find the smallest number of the consecutive numbers
            if item - 1 not in dic:
                count+=1
                num=item # this will be the current smallest number
                while num+1 in dic:
                    count+=1
                    num+=1
                mx=max(mx,count)
        return mx