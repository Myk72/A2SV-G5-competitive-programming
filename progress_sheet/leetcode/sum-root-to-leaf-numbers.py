# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        lst=[]
        def pre(root,res=""):
            if not root.right and not root.left:
                res+=str(root.val)
                lst.append(res)
                return
            
            res+=str(root.val)
            if root.left:
                pre(root.left,res)
            if root.right:
                pre(root.right,res)

        pre(root,"")
        return sum(int(num) for num in lst)