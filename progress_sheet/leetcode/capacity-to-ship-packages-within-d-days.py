class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        tot = sum(weights)

        def GoodToGo(target):
            curr=0
            day = 1

            for x in weights:
                if curr + x > target:
                    curr=0
                    day += 1
                curr += x

            return day <= days and curr<=target

        left, right = max(weights), tot

        while left < right:
            mid = (right + left) // 2

            if GoodToGo(mid):
                right = mid
            else:
                left = mid + 1

        return left