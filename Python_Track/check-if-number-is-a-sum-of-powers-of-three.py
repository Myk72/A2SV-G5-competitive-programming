class Solution:
    def checkPowersOfThree(self, n: int) -> bool:

        for i in range(int(n**(1/3)),-1,-1):
            if n - 3**i< 0:
                continue
            n-=3**i
            if n==0:
                return True
        return False
        