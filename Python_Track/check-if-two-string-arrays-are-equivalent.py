class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1=""
        w2=""
        for item in word1:
            w1+=item
        for item in word2:
            w2+=item
        if w1==w2:return True
        else:return False
        