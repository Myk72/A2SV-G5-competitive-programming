class OrderedStream:

    def __init__(self, n: int):
        self.arr=[""]*n
        self.initial=0

    def insert(self, idKey: int, value: str) -> List[str]:
        idKey-=1
        self.arr[idKey]=value
        if idKey>self.initial:
            return []
        while self.initial<len(self.arr) and self.arr[self.initial]!="":
            self.initial+=1
        return self.arr[idKey:self.initial]


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)