class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m,n=0,0
        res=""
        for i in range(max(len(word1),len(word2))):
            if n<len(word1):
                res+=word1[n]
                n+=1
            if m<len(word2):
                res+=word2[m]
                m+=1
        return res
            
        