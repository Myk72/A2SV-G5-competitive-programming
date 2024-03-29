# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i=0
        self.res=0
        def small(root):
            if not root: 
                return
            small(root.left)
            self.i+=1
            if self.i==k:
                self.res=root.val
                return root.val
            small(root.right)
        small(root)
        return self.res
