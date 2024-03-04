# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = deque([(root, 1)])
        max_width = 0
        while que:
            width = que[-1][1] - que[0][1] + 1
            max_width = max(max_width, width)
            # print(que)
            for i in range(len(que)):
                val, pos = que.popleft()

                if val.left:
                    que.append((val.left, 2 * pos))
                if val.right:
                    que.append((val.right, 2 * pos + 1))

        return max_width