class Solution:
    def minimumSteps(self, s: str) -> int:
        l=0
        ones=swaps=0
        while l<len(s):
            if s[l]=="1":
                ones+=1
            else:
                swaps+=ones
            l+=1
        return swaps