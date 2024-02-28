# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # For each subtree, find the minimum value and maximum value of its descendants.
        mx_diff =0
        def max_(root, mx,mn):
            nonlocal mx_diff
            if not root:
                return 0
            mn = min(mn, root.val)
            mx = max(mx, root.val)
            mx_diff = max(mx_diff,mx - mn)

            max_(root.left, mx, mn)
            max_(root.right, mx, mn)

        max_(root, 0, root.val)
        return mx_diff