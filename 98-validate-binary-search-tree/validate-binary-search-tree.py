# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recurr(root,left,right):
            if root is None:
                return True
            if root.val>left and root.val<right:
                return recurr(root.left,left,root.val) and recurr(root.right,root.val,right)
            else:
                return False


        return recurr(root.left,-math.inf,root.val) and recurr(root.right,root.val,math.inf)
        