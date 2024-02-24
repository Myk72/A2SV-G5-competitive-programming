# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count=defaultdict(int)
        self.mod=[]
        self.mx=0
        def mode(root):
            if not root: 
                return
            count[root.val]+=1
            if count[root.val]>self.mx:
                self.mod=[]
                self.mod.append(root.val)
                self.mx=count[root.val]
            elif count[root.val]==self.mx:
                self.mod.append(root.val)
            mode(root.left)
            mode(root.right)
        mode(root)
        return self.mod