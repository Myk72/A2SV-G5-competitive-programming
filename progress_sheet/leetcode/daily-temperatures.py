class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        mp=[0]*len(temperatures)
        for idx,temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]]<temp:
                tmp=stack[-1]
                mp[tmp]=idx-stack.pop()
            stack.append(idx)
        return mp
