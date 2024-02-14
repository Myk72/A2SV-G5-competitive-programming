class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        dic=defaultdict(int)
        count=0
        for rabbits in answers:
            if rabbits==0:
                count+=1
                continue
            if rabbits not in dic:
                dic[rabbits]+=1
                count+=rabbits+1
            else:
                if rabbits==dic[rabbits]:
                    del dic[rabbits]
                else:
                    dic[rabbits]+=1

        return count
