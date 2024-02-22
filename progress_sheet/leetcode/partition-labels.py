class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp={}
        result=[]
        idx=0
        l=0
        for i,item in enumerate(s):
            mp[item]=i
        for j,char in enumerate(s):
            idx=max(idx,mp[char])
            if idx==j:
                result.append(j+1-l)
                l=j+1
        return result  