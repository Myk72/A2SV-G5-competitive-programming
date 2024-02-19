class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        stack=[]
        mp=[-1]*n
        for i in range(2*n):
            idx=i%n
            while stack and nums[stack[-1]]<nums[idx]:
                tmp=stack.pop()
                if tmp<n:
                    mp[tmp]=nums[idx]
            stack.append(idx)
        return mp