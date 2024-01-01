class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = []
        for i in range(n):
            large=max(arr[:n-i])
            k=arr.index(large)+1
            arr[:k]=reversed(arr[:k])
            result.append(k)
            arr[:n - i] =reversed(arr[:n - i])
            result.append(n - i)
        return result
        