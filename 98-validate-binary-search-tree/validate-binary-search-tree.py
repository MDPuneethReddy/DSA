# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recurr(root,mini,maxi):
            if root is None:
                return True
            if root.val<=mini or root.val>=maxi:
                return False
            return recurr(root.left,mini,root.val) and recurr(root.right,root.val,maxi)
        return recurr(root,-math.inf,math.inf)
        