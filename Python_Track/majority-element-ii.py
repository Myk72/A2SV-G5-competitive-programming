class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x=len(nums)/3
        num=Counter(nums)
        res=[]
        for freq in num.keys():
            if num[freq]>x:
                res.append(freq)
        return res
            