class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mp= {item:index for index,item in enumerate(order)}
        for i in range(len(words)-1):
            fir=words[i]
            sec=words[i+1]
            for k in range(len(fir)):
                if k==len(sec):
                    return False
                if mp[fir[k]]<mp[sec[k]]:
                    break
                elif mp[fir[k]]>mp[sec[k]]:
                    return False
        return True