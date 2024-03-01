# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums=[]
        def inorder(root):
            if not root:
                return
            nums.append(root.val)
            inorder(root.left)
            inorder(root.right)
        inorder(root)
        nums.sort()
        def sortedArrayToBST(nums):
            if not nums:
                return 
            left, right = 0, len(nums)-1
            mid = (left+right)//2
            root = TreeNode(nums[mid])
            root.left = sortedArrayToBST(nums[:mid])
            root.right = sortedArrayToBST(nums[mid+1:])
            return root
        return sortedArrayToBST(nums)