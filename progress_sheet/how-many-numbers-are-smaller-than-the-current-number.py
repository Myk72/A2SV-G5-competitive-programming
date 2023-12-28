class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        srt=sorted(nums)
        mp={}
        l=0
        for num in srt:
            if num not in mp:
                mp[num]=l
            l+=1
        res=[]
        for item in nums:
            res.append(mp[item])
        return res 