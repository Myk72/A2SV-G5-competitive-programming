class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        mp={fronts[i] for i in range(len(fronts)) if fronts[i]==backs[i]}
        minm=float('inf')
        comb=set(fronts+backs)
        for item in comb:
            if item not in mp:
                minm=min(minm,item)
        return 0 if minm==float('inf') else minm
