class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        left=0
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,'C': 100, 'D': 500, 'M': 1000}
        for i in reversed(s):
            element = roman[i]
            if left > element :
                res -= element 
            else:
                res += element 
            left = element 
        return res
        