class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1])
        # print(points)
        count=0
        tmp=points[0][1]
        for i in range(1,len(points)):
            if tmp<points[i][0]:
                count+=1
                tmp=points[i][1]
        return count+1