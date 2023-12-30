class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        count=0
        cost=0
        for item in costs:
            cost+=item
            count+=1
            if cost>coins:
                return count-1
            if count==len(costs):
                return count
        