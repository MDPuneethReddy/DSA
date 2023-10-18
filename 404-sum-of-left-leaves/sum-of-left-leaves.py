# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.su=0
        def recurr(root):
            if root is None:
                return
            if root.left and root.left.left is None and root.left.right is None:
                self.su+=root.left.val
            recurr(root.left)
            recurr(root.right)
        recurr(root)
        return self.su
        