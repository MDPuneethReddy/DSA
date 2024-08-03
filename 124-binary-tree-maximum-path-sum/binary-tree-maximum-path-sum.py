# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi=-math.inf
        def recurr(root,s):
            if root is None:
                return 0
            left=recurr(root.left,s)
            right=recurr(root.right,s)
            value=root.val+left+right
            self.maxi=max(self.maxi,value,root.val)
            v=root.val+max(left,right)
            if v<=0:
                return 0
            else:
                return v
            # return root.val+max(left,right)
        recurr(root,0)
        return self.maxi

        