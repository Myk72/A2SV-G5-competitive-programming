class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n=len(nums)
        for i in range(n):
            direction = 1 if nums[i] >= 0 else -1
            j = 0
            curr = i

            for j in range(n):
                if direction == -1 and nums[curr] == 0:
                    break
                if nums[curr] * direction < 0 :
                    break
                curr = (curr+nums[curr])%n
                if j == 0 and curr ==i:
                    # [1] -> false
                    break
                elif curr == i:
                    # there is cycle
                    return True

        return False