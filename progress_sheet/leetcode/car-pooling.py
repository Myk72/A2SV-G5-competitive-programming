class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxi=0
        res=0
        for lst in trips:
            maxi=max(maxi,lst[2])
        arr=[0]*(maxi+1)
        for psg, start, end in trips:
            arr[start] += psg
            arr[end] -= psg
        for num in arr:
            res += num
            if res > capacity:
                return False
        return True
        

        