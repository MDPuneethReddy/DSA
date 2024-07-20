# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count=0
        def recurr(root,maxvalue):
            if root is None:
                return
            if root.val>=maxvalue:
                self.count+=1
            maxvalue=max(maxvalue,root.val)
            recurr(root.left,maxvalue)
            recurr(root.right,maxvalue)
            return
        recurr(root,root.val)
        return self.count
        