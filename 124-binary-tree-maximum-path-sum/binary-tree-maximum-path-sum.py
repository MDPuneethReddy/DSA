# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        value=[-math.inf]
        def recurr(root):
            if root is None:
                return 0
            if root.left is None and root.right is None:
                value[0]=max(value[0],root.val)
                return root.val
            left=recurr(root.left)
            right=recurr(root.right)
            value[0]=max(value[0],root.val,left+right+root.val,max(left,right)+root.val)
            return max(left,right,0)+root.val
        recurr(root)

        return value[0]
        