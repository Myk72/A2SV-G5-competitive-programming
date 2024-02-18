# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        reverse = None
        dummy = ListNode(0, head)
        curr=head
        curr2=dummy
        i=j=0
        while i < left - 1:
            curr2=curr2.next
            curr=curr.next
            i += 1
        while j < right-left+1:
            tmp=curr.next
            curr.next=reverse
            reverse,curr=curr,tmp
            j += 1

        curr2.next.next=curr
        curr2.next=reverse
        return dummy.next

        