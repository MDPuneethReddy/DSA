# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.bool=True
        def recurr(root):
            if root is None:
                return 0
            v=recurr(root.left)
            v1=recurr(root.right)
            if(abs(v-v1)>1):
                self.bool=False
            return 1+max(v,v1)
        recurr(root)
        return self.bool
        