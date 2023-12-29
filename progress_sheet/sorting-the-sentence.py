class Solution:
    def sortSentence(self, s: str) -> str:
        splt=s.split(" ")
        dct={}
        for i in splt:
            dct[int(i[-1])]=i[:-1]
        return " ".join(dct[i]for i in range(1,len(splt)+1))
        