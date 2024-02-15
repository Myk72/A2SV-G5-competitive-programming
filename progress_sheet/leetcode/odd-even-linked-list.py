# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # o(1) space, o(n)time
        if not head or not head.next or not head.next.next:
            return head
        even=head.next
        odd=head
        curr_even=even
        while odd and odd.next and even.next:
            odd.next=even.next
            even.next=odd.next.next
            odd=odd.next
            even=even.next
        odd.next=curr_even
        return head
