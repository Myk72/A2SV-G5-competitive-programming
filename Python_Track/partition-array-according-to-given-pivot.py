class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        greater=[]
        less=[]
        equal=[]
        for item in nums:
            if item>pivot:
                greater.append(item)
            elif item<pivot:
                less.append(item)
            else:
                equal.append(item)
    
        return less+equal+greater