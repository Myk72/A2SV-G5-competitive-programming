class Solution:
    def trap(self, height: List[int]) -> int:
        n =len(height)
        res = 0
        stack = []
        for idx,num in enumerate(height):
            while stack and stack[-1][0]< num:
                # print(stack)
                val,pos = stack.pop()
                if stack:
                    hght = min(stack[-1][0],num)-val
                    # width = idx - stack[-1][1]
                    # print((width*hght))
                    width = (idx-1) - stack[-1][1]
                    res += (width*hght)
            stack.append((num,idx))
        return res