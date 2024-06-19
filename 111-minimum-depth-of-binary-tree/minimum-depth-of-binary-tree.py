# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        def recurr(root,level,mini):
            if root is None:
                return mini
            if root.left is None and root.right is None:
                mini[0]=min(mini[0],level)
                return mini
            recurr(root.left,level+1,mini)
            recurr(root.right,level+1,mini)
            return mini
        return recurr(root,0,[math.inf])[0]+1
        