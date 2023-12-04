class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        distance= 0
        x=-1
        tmp=capacity
        for i in range(len(plants)):
            if plants[i]<=capacity:
                capacity-=plants[i]
                distance+=1
            elif plants[i] > capacity:
                capacity =tmp
                capacity-=plants[i]
                distance += i- x-1
                distance += i - x
        return distance
        