class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        maxi=[]
        score=0
        count=Counter(nums)
        for i in range(len(nums)+1):
            if i==0:
                count_right=count[1]
                count_left=0
            elif i==len(nums):
                count_right=0
                count_left=count[0]
            
            elif nums[i-1]==0:
                count_left+=1
            elif nums[i-1]==1:
                count_right-=1
            curr_sum= count_left+ count_right
            if curr_sum>score:
                score=curr_sum
                maxi=[]
                maxi.append(i)
            elif curr_sum==score:
                maxi.append(i)
        return maxi
