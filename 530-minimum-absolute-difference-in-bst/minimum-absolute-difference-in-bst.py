# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev=None
        self.res=math.inf
        def recurr(root):
            if root is None:
                return
            recurr(root.left)
            if self.prev:
                self.res=min(self.res,abs(root.val-self.prev.val))
            self.prev=root
            recurr(root.right)
        recurr(root)
        
        return self.res