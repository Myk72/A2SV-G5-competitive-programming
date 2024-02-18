# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        st=ListNode(head.val)
        res = ListNode(float("-inf"),st)
        curr=head.next
        while curr:
            temp = res
            while temp.next and temp.next.val < curr.val:
                temp = temp.next
            temp.next = ListNode(curr.val, temp.next)
            curr = curr.next
        res=res.next
        return res