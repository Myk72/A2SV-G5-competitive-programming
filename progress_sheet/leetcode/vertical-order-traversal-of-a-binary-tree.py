# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        coord=defaultdict(list)
        res=[]
        tmp=[]
        def carte(root,row,col):
            if not root:
                return
            coord[col].append((row,root.val))
            carte(root.left,row+1,col-1)
            carte(root.right,row+1,col+1)

        carte(root,0,0)
        for key in coord:
            tmp.append(key)
        tmp.sort()
        # print(tmp)
        for num in tmp:
            x=coord[num]
            x.sort()
            arr=[item[1] for item in x]
            res.append(arr)
            # print(arr)
        # new=sorted(coord.keys(),key=lambda x:x[1])
        # print(new)
        return res