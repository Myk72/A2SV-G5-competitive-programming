class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        r=max(len(list1),len(list2))
        ans=float('inf')
        res=[]
        for i in range(r):
            if i<len(list1):
                if list1[i] in list2:
                    x=list2.index(list1[i])
                    if not res:
                        ans=min(ans,list2.index(list1[i])+i)
                    if ans > list2.index(list1[i]) + i:
                        res.clear()
                        res.append(list1[i])
                        ans=list2.index(list1[i])+i
                    elif ans == list2.index(list1[i]) + i:
                        res.append(list1[i])
                        ans=list2.index(list1[i])+i

        return res