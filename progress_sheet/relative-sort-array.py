class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count=Counter(arr1)
        res=[]
        for item in arr2:
            ext=[item for i in range(count[item])]
            res.extend(ext)
        notin=[]
        for item in arr1:
            if item not in arr2:
                notin.append(item)
        notin.sort()
        return res + notin

    