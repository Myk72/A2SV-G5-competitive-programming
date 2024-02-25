class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n=len(nums)
        stack=[]
        min_=float("inf")
        for idx,num in enumerate(nums):
            if stack:
                min_=min(stack[-1][1],stack[-1][0])
            while stack and stack[-1][0]<=num:
                stack.pop()
            if stack and stack[-1][1]<num:
                return True
            stack.append((num,min_))
            # print(stack)
        return False


