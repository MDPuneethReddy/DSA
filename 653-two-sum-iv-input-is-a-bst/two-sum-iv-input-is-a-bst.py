# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def recurr(root,k,d):
            if root is None:
                return False
            if root.val in d:
                return True
            d.add(k-root.val)
            return recurr(root.left,k,d) or recurr(root.right,k,d)
        return recurr(root,k,set())

        