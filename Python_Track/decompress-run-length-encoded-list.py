class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        l,r=0,1
        res=[]
        while r<len(nums):
            arr=[nums[r]]*nums[l]
            res.extend(arr)
            l=r+1
            r+=2
        return res