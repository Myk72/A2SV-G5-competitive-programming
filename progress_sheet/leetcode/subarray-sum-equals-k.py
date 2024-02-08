class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count =Counter({0:1})
        pres = res = 0
        for num in nums:
            pres += num
            if count[pres-k]>0:
                res+=count[pres-k]
            count[pres]+=1
        return res