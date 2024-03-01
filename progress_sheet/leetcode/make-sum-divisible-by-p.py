class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n=len(nums)
        summ=sum(nums)
        if summ%p==0:
             return 0
        remainder=summ%p
        #print(remainder,summ)
        count ={0:0}
        ans = n
        preS = 0
        for idx,num in enumerate(nums):
            preS += num
            if (preS - summ) % p in count:
                ans =min(ans,idx-count[(preS - summ) % p]+1)
            count[preS%p] =idx+1
            #print(count)
        return ans if ans!=n else -1