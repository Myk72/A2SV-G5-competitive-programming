class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res=[]
        pos=[item for item in nums if item>0]
        neg=[item for item in nums if item<0]
        for i in range(len(nums)//2):
            res.append(pos[i])
            res.append(neg[i])
        return res