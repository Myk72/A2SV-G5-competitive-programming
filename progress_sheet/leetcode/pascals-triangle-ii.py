class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        self.i=0
        def get(prev):
            res = [1]
            if self.i==rowIndex:
                return prev
            for i in range(0,len(prev)-1):
                res.append(prev[i] + prev[i+1])
            res.append(1)
            self.i+=1
            return get(res)
        
        return get([1])