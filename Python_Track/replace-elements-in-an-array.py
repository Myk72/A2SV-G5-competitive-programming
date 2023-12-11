class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        mp={b:a for a,b in enumerate(nums)}
        for i in range(len(operations)):
            index=mp[operations[i][0]]
            nums[index]=operations[i][1]
            mp[operations[i][1]]=mp.pop(operations[i][0])                 
        return nums
        