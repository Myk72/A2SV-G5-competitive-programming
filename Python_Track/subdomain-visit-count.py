class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res=defaultdict(int)
        ans=[]
        for item in cpdomains:
            x=item.split(" ")
            occurance=int(x[0])
            domain=x[1]
            res[domain]+=occurance
            for i in range(len(domain)):
                if domain[i]==".":
                    res[domain[i+1:]]+=occurance
        for a,b in res.items():
            ans.append(str(b)+" "+a)
        return ans
        