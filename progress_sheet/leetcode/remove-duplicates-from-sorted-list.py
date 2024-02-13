# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dic={head.val:1}
        curr=ListNode(head.val)
        res=curr
        while head.next:
            head=head.next
            if head.val not in dic:
                # print(head.val)
                dic[head.val]=1
                new=curr
                while new.next:
                    new = new.next
                new.next=ListNode(head.val)
        return curr