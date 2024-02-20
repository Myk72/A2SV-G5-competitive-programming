class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        count=0
        arr.append(0)
        stack=[]
        for idx, num in enumerate(arr):
            while stack and num < arr[stack[-1][1]]:
                tmp=stack.pop()
                pre = stack[-1][1] if stack else -1
                count+=(idx-tmp[1])*(tmp[1]-pre)*tmp[0]
            stack.append((num,idx))
        return count%(10**9 + 7)