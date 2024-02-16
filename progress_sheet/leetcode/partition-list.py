# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        great=ListNode()
        less=ListNode()
        curr1=great
        curr2=less
        while head:
            if head.val<x:
                curr2.next=head
                curr2=curr2.next
            else:
                curr1.next=head
                curr1=curr1.next
            head=head.next

        curr1.next=None
        curr2.next=great.next
        return less.next