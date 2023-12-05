class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        key1="qwertyuiop"
        key2="asdfghjkl"
        key3="zxcvbnm"
        res=[]
        for item in words:
            s=item[0]
            if item[0].lower() in key2:
                for i in range(1,len(item)):
                    if item[i].lower() not in key2:
                        break
                    else:
                        s+=item[i]
                if s==item:
                    res.append(s)
            elif item[0].lower() in key1:
                for i in range(1,len(item)):
                    if item[i].lower() not in key1:
                        break
                    else:
                        s+=item[i]
                if s==item:
                    res.append(s)
            elif item[0].lower() in key3:
                for i in range(1,len(item)):
                    if item[i].lower() not in key3:
                        break
                    else:
                        s+=item[i]
                if s==item:
                    res.append(s)
        return res
        