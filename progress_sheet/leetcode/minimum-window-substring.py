class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        tcount=Counter(t)
        cnt=defaultdict(int)
        minm=float("inf")
        start,end,length=0,0,0
        # res=""
        for idx,char in enumerate(s):
            cnt[char]+=1
            if tcount[char]>=cnt[char]:
                # length+=tcount[char]
                length+=1
            # print(cnt)
            while end<=idx and length==len(t):
                if idx-end+1<minm:
                    minm=idx-end+1
                    start=end
                    # res=s[start:minm+start]
                cnt[s[end]]-=1
                if cnt[s[end]]<tcount[s[end]]:
                    length-=1
                end+=1
        return s[start:minm+start] if minm!=float("inf") else ""