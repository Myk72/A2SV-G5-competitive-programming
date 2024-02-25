class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        if n<3:
            return 0
        nums.sort(reverse=True)
        count,j=0,1
        k=n-1
        for i in range(n-2):
            while j<k:
                if nums[k] + nums[j] > nums[i]:
                    count+=k-j
                    j+=1
                else:
                    k-=1
            j=i+2
            k=n-1
        return count
