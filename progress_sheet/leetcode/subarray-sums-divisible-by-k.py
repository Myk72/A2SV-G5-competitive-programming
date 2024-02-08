class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count =Counter({0:1})
        pres = res = 0
        for num in nums:
            pres=(pres+num)%k
            res+=count[pres]
            count[pres]+=1
        return res