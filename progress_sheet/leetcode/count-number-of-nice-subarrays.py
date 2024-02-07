class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res =l = count = 0
        x=0
        n = len(nums)
        for i in range(n):
            if nums[i] % 2 == 1:
                x+= 1
                count = 0
            while k == x:
                if nums[l]%2==1:
                    x-=1
                l+= 1
                count += 1
            res += count
        return res