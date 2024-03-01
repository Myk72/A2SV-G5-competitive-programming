class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""
        dic = set(s)
        for idx,char in enumerate(s):
            if char.upper() in dic and char.lower() in dic: 
                continue
            left_side = self.longestNiceSubstring(s[:idx])
            right_side = self.longestNiceSubstring(s[idx+1:])

            if len(left_side)>=len(right_side):
                return left_side
            return right_side

        return s