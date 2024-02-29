class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        arr=[]
        nums.sort() #if not sorted nums
        def backtrack(idx):
            nonlocal res,arr
            if len(nums)==idx:
                if arr:
                    res.append(arr[:])
                return
            arr.append(nums[idx])
            backtrack(idx+1)
            arr.pop()

            while idx+1<len(nums) and nums[idx]==nums[idx+1]:
                idx+=1
            backtrack(idx+1)

        backtrack(0)
        return res