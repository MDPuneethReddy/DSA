# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxi=[0]
        def recurr(root):
            if root is None:
                return 0
            left=recurr(root.left)
            right=recurr(root.right)
            maxi[0]=max(maxi[0],left+right)
            return 1+max(left,right)
        recurr(root)
        return maxi[0]
        
        
        