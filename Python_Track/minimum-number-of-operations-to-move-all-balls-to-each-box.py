class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        operation=0
        res=[]
        indexofOne=[]
        for index,item in enumerate(boxes):
            if item=="1":
                indexofOne.append(index)
        for i in range(len(boxes)):
            for index in indexofOne:
                operation+=abs(index-i)
            res.append(operation)
            operation=0
        return res