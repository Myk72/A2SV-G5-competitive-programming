class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l=2**31
        r=2**31
        for item in nums:
            if item > r:
                return True
            if item <= l:
                l = item
            else:
                r = item
        return False