class Solution:
    def intervalIntersection(self, fir: List[List[int]], sec: List[List[int]]) -> List[List[int]]:
        f,s=0,0
        res=[]
        while f<len(fir) and s<len(sec):
            inti=max(fir[f][0],sec[s][0])
            nxt=min(fir[f][1],sec[s][1])
            if inti<=nxt:
                res.append([inti,nxt])
            if fir[f][1]>=sec[s][1]:
                s+=1
            else:
                f+=1
        return res