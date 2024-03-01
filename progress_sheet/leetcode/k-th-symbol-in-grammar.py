class Solution:
        def kthGrammar(self, n: int, k: int) -> int:
            if n == 1:
                return 0
            prevK = (k + 1) // 2
            prev = self.kthGrammar(n-1, prevK)
            if k % 2:
                return prev
            return 1 - prev