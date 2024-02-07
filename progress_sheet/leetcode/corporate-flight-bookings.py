class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        arr=[0]*(n+1)
        for a,b,c in bookings:
            arr[a-1]+=c
            arr[b]-=c
        for i in range(1,n):
            arr[i]+=arr[i-1]
        return arr[:-1]