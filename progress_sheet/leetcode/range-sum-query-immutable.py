class NumArray:

    def __init__(self, nums: List[int]):
        i=0
        for j in range(len(nums)):
            nums[j]=i+nums[j]
            i+=nums[j]-i
        self.array=nums
    def sumRange(self, l: int, r: int) -> int:
        if l>0:
            return self.array[r]-self.array[l-1]
        else:return self.array[r]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)