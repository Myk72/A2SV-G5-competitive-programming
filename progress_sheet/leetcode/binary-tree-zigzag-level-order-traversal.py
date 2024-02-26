# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:return []
        que = deque([root])
        res = []
        flag=False
        while que:
            n =len(que)
            tmp=[]
            for i in range(n):
                node = que.popleft()
                tmp.append(node.val)
                # print(node.val,flag,n)
                if node.right:
                    que.append(node.right)
                if node.left:
                    que.append(node.left)
                # print(que)
            if flag:
                res.append(tmp)
            else:
                res.append(tmp[::-1])
            flag=not flag
        return res