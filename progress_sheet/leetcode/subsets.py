class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[[]]
        arr=[]
        def backtrack(idx):
            nonlocal res,arr
            if len(nums)==idx:
                if arr:
                    res.append(arr[:])
                return
            arr.append(nums[idx])
            backtrack(idx+1)
            arr.pop()
            backtrack(idx+1)

        backtrack(0)
        return res