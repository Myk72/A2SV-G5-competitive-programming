class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        l,r=1,len(arr)-1
        if r<2:
            return False
        if arr[0]>=arr[1]:return False
        while l<r:
            if arr[l-1]>arr[l]:
                break
            if arr[l-1]==arr[l]:
                return False
            l+=1
        if l==r and arr[l-1]<=arr[l]:
            return False
        while l<r:
            if arr[l]<=arr[l+1]:
                return False
            l+=1
        return True 