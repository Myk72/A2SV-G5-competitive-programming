# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        res=[None]*k
        curr=head
        def get_length(head):
            temp = head
            count = 0
            while temp:
                count += 1
                temp = temp.next
            return count
        n=get_length(head)
        mod=n%k
        div=n//k
        rang= k if n>k else n
        for i in range(rang):
            new=ListNode()
            tmp=new
            if mod>0:
                length=div+1 if n>k else 1
            else:length=div
            j=0
            while curr and j<length:
                tmp.next = ListNode(curr.val)
                tmp=tmp.next
                curr=curr.next
                j+=1
            mod=mod-1 if mod>0 else 0
            res[i]=new.next
        return res