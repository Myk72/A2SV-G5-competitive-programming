# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def ancestor(root):
            if not root:
                return
            if root.val > p.val and root.val > q.val:
                return ancestor(root.left)
            elif root.val < p.val and root.val < q.val:
                return ancestor(root.right)
            else:
                return root

        return ancestor(root)
        