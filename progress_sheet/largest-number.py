class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        lists=[]
        for item in nums:
            lists.append(str(item))
        for i in range(len(lists)):
            for j in range(i,len(lists)):
                if lists[i]+lists[j]<lists[j]+lists[i]:
                    lists[i],lists[j]=lists[j],lists[i]
        result="".join(lists)
        return result if int(result)!=0 else "0"