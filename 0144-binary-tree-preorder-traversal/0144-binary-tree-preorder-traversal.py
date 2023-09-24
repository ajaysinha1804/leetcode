# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        res_1=[root]
        while res_1:
            value=res_1.pop()
            if value:
                res.append(value.val)
                res_1.append(value.right)
                res_1.append(value.left)
        return res