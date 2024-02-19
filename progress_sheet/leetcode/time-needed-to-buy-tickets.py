class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time=0
        que=tickets
        while que[k]>0:
            i=0
            while i<len(que):
                que[i]-=1
                time+=1
                if que[i]==0:
                    if i==k:
                        return time
                    elif i<k:
                        k-=1
                    que.pop(i)
            
                else:i+=1

