class Node:
    def __init__(self, val=0, next = None):

        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head=Node()

    def get(self, index: int) -> int:
        i=-1
        curr=self.head
        while curr:
            if  i==index:
                return curr.val
            curr=curr.next
            i+=1
        return -1

    def addAtHead(self, val: int) -> None:
        curr=self.head
        new=Node(val,curr.next)
        curr.next = new

    def addAtTail(self, val: int) -> None:
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        i=0
        curr = self.head
        while curr.next:
            if i==index:
                break
            curr = curr.next
            i+=1
        if not curr.next and i<index:
            return -1
        new = Node(val, curr.next)
        curr.next= new
    
    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        i=0
        while curr.next and i<index:
            curr = curr.next
            i+=1
        if not curr.next:
            return -1
        curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)