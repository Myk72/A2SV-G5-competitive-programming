class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        # [[7, 4], [8, 7], [9, 7], [9, 9]]
        max_area=0
        for i in range(len(points)-1):
            area=abs(points[i][0]-points[i+1][0])
            max_area=max(max_area,area)
        return max_area