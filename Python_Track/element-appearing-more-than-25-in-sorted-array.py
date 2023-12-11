class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        l1,l2,n=0,1,len(arr)
        if n==1:return arr[0]
        while l2<n:
            if arr[l1]==arr[l2]:
                l2+=1
            if l2 - l1 > n / 4:
                return arr[l1]
            if arr[l1] != arr[l2]:
                l1,l2=l2,l2+1