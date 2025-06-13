# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isbalanced=True
        def recurr(root):
            if root is None:
                return 0
            left=recurr(root.left)
            right=recurr(root.right)
            if abs(left-right)>1:
                self.isbalanced=False
            # print(self.isbalanced)
            return 1+max(left,right)
        recurr(root)
        return self.isbalanced
            
        