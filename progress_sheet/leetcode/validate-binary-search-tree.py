# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')

        def valid(root):
            nonlocal prev
            if not root:
                return True
            if not valid(root.left):
                return False
            # print(prev,root.val)
            if root.val <= prev:
                return False
            prev = root.val
            
            return valid(root.right)
        
        return valid(root)