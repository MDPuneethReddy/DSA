# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        main=[]
        def recurr(root,s):
            if root is None:
                return
            if root.left is None and root.right is None:
                main.append(s+str(root.val))
            recurr(root.left,s+str(root.val))
            recurr(root.right,s+str(root.val))
            return
        recurr(root,"")
        ts=0
        for i in main:
            ts+=int(i)
        return ts
        