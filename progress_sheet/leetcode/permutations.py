class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def per(curr):
            if len(curr) == n:
                res.append(curr[:])
                return
            for num in nums:
                if num not in curr: 
                    curr.append(num)
                    per(curr)
                    curr.remove(num)

        per([])
        return res