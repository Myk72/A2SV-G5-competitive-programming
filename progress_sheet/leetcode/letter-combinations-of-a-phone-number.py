class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []
        hashmp={'2':('abc'),  '3': ('def'), '4': ('ghi'),  '5': ('jkl'),  '6': ('mno'),  '7': ('pqrs'), '8': ('tuv'), '9': ('wxyz')}
        res=[]
        def backtrack(word,i):
            nonlocal hashmp,res
            if len(word)==len(digits):
                res.append(word)
                return
            for letter in hashmp[digits[i]]:
                backtrack(word + letter,i+1)
        backtrack("",0)
        return res