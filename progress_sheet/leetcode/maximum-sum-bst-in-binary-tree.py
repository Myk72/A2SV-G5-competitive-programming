# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        #(sum, isBST, maxLeft, minRight)
        res = 0
        def check_sum_BST(root):
            nonlocal res
            if root:
                leftmax = check_sum_BST(root.left)
                rightmin = check_sum_BST(root.right)
                curr=root.val+leftmax[3]+rightmin[3]
                if leftmax[0] < root.val < rightmin[1]:
                    if leftmax[2] and rightmin[2]:
                        res = max(res,curr)
                    return max(leftmax[0],rightmin[0],root.val), min(rightmin[1],leftmax[1],root.val), leftmax[2] and rightmin[2],curr
                return max(leftmax[0],rightmin[0],root.val), min(rightmin[1],leftmax[1],root.val), False,curr
            return float('-inf'),float('inf'),True,0
        check_sum_BST(root)
        return res