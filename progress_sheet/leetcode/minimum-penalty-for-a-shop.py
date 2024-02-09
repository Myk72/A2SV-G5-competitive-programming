class Solution:
    def bestClosingTime(self, customers: str) -> int:
        mp={"N":0,"Y":customers.count("Y")}
        min_=float('inf')
        l=0
        for idx in range(len(customers)+1):
            penalty=mp["Y"]+mp["N"]
            if idx<len(customers) and customers[idx]=="Y":
                mp["Y"]-=1
            else:
                mp["N"]+=1
            if penalty<min_:
                min_=penalty
                l=idx
        return l

