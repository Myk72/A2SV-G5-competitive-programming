# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class MyCircularQueue:

    def __init__(self, k: int):
        # using linked list
        self.head=None
        self.tail=None
        self.k=k
        self.lenght=0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): 
            return False
        root=ListNode(value)
        if self.isEmpty():
            self.head=root
            self.tail=root
            self.lenght+=1
        else:
            self.tail.next=root
            self.tail=self.tail.next
            self.lenght+=1
        return True

    def deQueue(self) -> bool:
        if not self.isEmpty():
            self.head = self.head.next
            self.lenght-=1
            return True
        return False

    def Front(self) -> int:
        if not self.isEmpty():
            return self.head.val  
        return -1
        
    def Rear(self) -> int:
        if not self.isEmpty():
            return self.tail.val
        return -1

    def isEmpty(self) -> bool:
        return self.lenght==0

    def isFull(self) -> bool:
        return self.lenght==self.k

 
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()