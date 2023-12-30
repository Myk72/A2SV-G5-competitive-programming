class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        l=1
        piles.sort(reverse=True)
        count=0
        for i in range(len(piles)//3):
            count+=piles[l]
            l+=2
        return count