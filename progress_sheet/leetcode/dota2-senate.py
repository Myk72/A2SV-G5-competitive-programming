class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        que=deque(senate)
        mp=Counter(senate)
        R=D=0
        while mp["R"]>0 and mp["D"]>0:
            val = que.popleft()
            if val=="D":
                if D==0:
                    R+=1
                    que.append(val)
                else:
                    mp["D"]-=1
                    D-=1
            else:
                if R==0:
                    D+=1
                    que.append(val)
                else:
                    mp["R"]-=1
                    R-=1 
        return "Radiant" if que[0]=="R" else "Dire"