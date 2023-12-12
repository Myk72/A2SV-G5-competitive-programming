class Solution:
    def isHappy(self, n: int) -> bool:
        res = 0
        check = []
        while res != 1:
            res = 0
            for item in str(n):
                res += int(item) ** 2
            if res in check:
                return False
            check.append(res)
            n=res
        return True