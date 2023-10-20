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
        s=0
        self.mv=math.inf
        def recurr(root,s):
            if root is None:
                return 
            s+=1
            if root.left is None and root.right is None:
                self.mv=min(self.mv,s)
            recurr(root.left,s)
            recurr(root.right,s)
            return
        recurr(root,s)
        return self.mv
        