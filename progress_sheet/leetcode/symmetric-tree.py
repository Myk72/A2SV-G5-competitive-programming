# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def Symmetric(root1,root2):
            if not root1 and not root2:
                return True
            if not root1 and root2:
                return False
            if not root2 and root1:
                return False
            if root1.val!=root2.val:
                return False
            x=Symmetric(root1.left,root2.right)
            y=Symmetric(root1.right,root2.left)
            return x and y
        return Symmetric(root,root)