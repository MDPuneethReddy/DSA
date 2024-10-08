# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is not None:
            return False
        if root.right is None and root.left is not None:
            return False
        def recurr(root1,root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None and root2 is not None:
                return False
            if root1 is not None and root2 is None:
                return False
            if root1.val!=root2.val:
                return False
            return recurr(root1.left,root2.right) and recurr(root1.right,root2.left)
        return recurr(root.left,root.right)
        