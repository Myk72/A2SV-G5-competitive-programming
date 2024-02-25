# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.count=0
        def pre(root):
            if not root: 
                return
            if low<=root.val<=high:
                self.count+=root.val
            pre(root.left)
            pre(root.right)
        
        pre(root)
        return self.count