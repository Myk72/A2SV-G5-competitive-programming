class Bitset:

    def __init__(self, size: int):
        self.bitset={i:0 for i in range(size)}
        self.cnt=0
        self.length=size
        self.bitset2={i:1 for i in range(size)}

    def fix(self, idx: int):
        if self.bitset[idx]==0:
            self.cnt+=1
        self.bitset[idx]=1
        self.bitset2[idx]=0
        
    def unfix(self, idx: int):
        if self.bitset[idx]==1:self.cnt-=1
        self.bitset[idx]=0
        self.bitset2[idx]=1
        
    def flip(self):
        self.bitset,self.bitset2=self.bitset2,self.bitset
        self.cnt=self.length-self.cnt

    def all(self):
        if self.cnt==len(self.bitset): return True
        else:return False

    def one(self):
        if self.cnt>0:return True
        else:return False

    def count(self):
        return self.cnt

    def toString(self):
        return "".join(str(value) for value in self.bitset.values())