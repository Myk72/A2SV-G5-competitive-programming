# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dic={}
        first=headA
        second=headB
        while first:
            dic[first]=1
            first=first.next
        while second:
            if second in dic:
                return second
            second=second.next
        