class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res=[]
        for item in image:
            tmp=item[::-1]
            for i in range(len(tmp)):
                if tmp[i]==1:tmp[i]=0
                elif tmp[i]==0:tmp[i]=1
            res.append(tmp)
        return res