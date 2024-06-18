# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def recurr(root,level,isLeft,value):
            if root is None:
                return value
            if isLeft and root.left is None and root.right is None:
                value[0]+=root.val
            recurr(root.left,level+1,True,value)
            recurr(root.right,level+1,False,value)
            return value
        return recurr(root,0,False,[0])[0]
        