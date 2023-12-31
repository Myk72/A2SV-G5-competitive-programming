class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points.sort(key= lambda c: sqrt(c[0]**2+c[1]**2))
        return points[:k]