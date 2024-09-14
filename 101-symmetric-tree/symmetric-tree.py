# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recurr(leftroot,rightroot):
            if leftroot is None and rightroot is None:
                return True
            if not leftroot or not rightroot:
                return False
            if leftroot.val!=rightroot.val:
                return False
            return recurr(leftroot.left,rightroot.right) and recurr(leftroot.right,rightroot.left)
        return recurr(root.left,root.right)
        