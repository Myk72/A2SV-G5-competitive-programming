class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def myPow(x,n):
            if n == 0: 
                return 1 
            if n % 2 == 0:
                return (myPow(x * x, n // 2))
            else:
                return (x%(10**9 + 7) * myPow(x%(10**9 + 7) * x%(10**9 + 7), n // 2))
        if n%2==0:
            return (myPow(5,n//2)*myPow(4,n//2))%(10**9 + 7)
        else:
            return myPow(5,n//2+1)*myPow(4,n//2)%(10**9 + 7)