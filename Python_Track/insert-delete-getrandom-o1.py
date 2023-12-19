class RandomizedSet:

    def __init__(self):
        self.dict={}
        self.arr=[]
        self.point=-1

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.point+=1
            self.dict[val]=self.point
            self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            i=self.dict[val]
            self.dict[self.arr[self.point]]=i
            self.arr[i],self.arr[self.point]=self.arr[self.point],self.arr[i]
            self.point-=1
            del self.dict[val]
            self.arr.pop()
            return True
        return False

    def getRandom(self) -> int:
        return self.arr[randint(0,self.point)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()