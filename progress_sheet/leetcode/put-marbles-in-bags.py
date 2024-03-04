class Solution:
    def putMarbles(self, weight: List[int], k: int) -> int:
        n=len(weight)
        pair=[0]*(n-1)
        for i in range(1,n):
            pair[i-1]=weight[i]+weight[i-1]
        pair.sort()
        min_=max_=0
        for i in range(k-1):
            min_+=pair[i]
            max_+=pair[n-i-2]
        return max_-min_