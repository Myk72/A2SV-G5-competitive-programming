class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        l,r=0,n-k
        max_sum=sum(cardPoints[:n-k])
        min_sum=max_sum
        while r<len(cardPoints):
            max_sum+=cardPoints[r]
            max_sum-=cardPoints[l]
            min_sum=min(max_sum,min_sum)
            r+=1
            l+=1
        return sum(cardPoints)-min_sum
