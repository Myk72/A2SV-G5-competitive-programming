class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n=len(blocks)
        count=0
        if n <k:return 0
        l,r=0,0
        minm=float('inf')
        while r<n:
            if r>=k:
                minm=min(count,minm)
                if blocks[l]=='W':
                    count-=1
                if blocks[r]=="W":
                    count+=1
                l+=1
            else:
                if blocks[r]=='W':
                    count+=1
            r+=1
        return min(minm,count)
