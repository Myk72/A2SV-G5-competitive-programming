# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp=head
        reverse = None
        cur = reverse
        
        while head:
            cur = ListNode(head.val,reverse)
            reverse = cur
            head = head.next
        while reverse:
            if reverse.val!=tmp.val:
                return False
            reverse=reverse.next
            tmp=tmp.next
        return True