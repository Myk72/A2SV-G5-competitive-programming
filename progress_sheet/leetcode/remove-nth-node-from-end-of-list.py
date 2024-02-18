# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        curr=dummy
        def get_length(head):
            temp = head
            count = 0
            while temp:
                count += 1
                temp = temp.next
            return count
        k=get_length(curr)-1
        i=k-n
        j=0
        while curr.next and j<i:
            curr = curr.next
            j+=1
        if curr.next:
            curr.next = curr.next.next
        else:
            return None
        return dummy.next