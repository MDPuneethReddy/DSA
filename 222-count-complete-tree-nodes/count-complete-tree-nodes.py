# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        self.s=0
        def recurr(root):
            if root is None:
                return
            self.s+=1
            recurr(root.left)
            recurr(root.right)
            return
        recurr(root)
        return self.s
        