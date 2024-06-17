# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        leftValue=self.tree2str(root.left)
        rightValue=self.tree2str(root.right)
        if leftValue =="" and rightValue =="":
            return str(root.val)
        elif leftValue!="" and rightValue=="":
            return str(root.val)+"("+leftValue+")"
        else:
            return str(root.val)+"("+leftValue+")("+rightValue+")"
        