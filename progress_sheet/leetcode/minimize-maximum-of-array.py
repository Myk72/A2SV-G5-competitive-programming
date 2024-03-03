class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = min(nums), max(nums)

        def check(k,arr):
            for i in range(n - 1, 0, -1):
                if arr[i] <= k: continue
                tmp = arr[i] - k
                arr[i] -= tmp
                arr[i - 1] += tmp
            if max(arr)>k:return False
            return True

        while left < right:
            mid = (left + right)//2

            if check(mid,nums[:]):
                right = mid
            else:
                left = mid + 1

        return left