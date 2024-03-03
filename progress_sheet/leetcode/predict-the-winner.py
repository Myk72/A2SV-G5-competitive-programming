class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        choosed=defaultdict()
        def winner(left,right,turn):
            if left>right:
                return 0
            if (left,right,turn) in choosed:
                return choosed[(left,right,turn)]
            res=0
            if turn==1:
                res=max(nums[left]+winner(left+1,right,2),nums[right]+winner(left,right-1,2))
            else:
                res=min(winner(left+1,right,1),winner(left,right-1,1))
            choosed[(left,right,turn)]=res
            return res
        player1=winner(0,n-1,1)
        return sum(nums)-player1<=player1