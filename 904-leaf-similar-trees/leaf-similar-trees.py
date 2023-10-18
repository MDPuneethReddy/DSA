# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.l1=[]
        self.l2=[]
        def recurr(root,l):
            if root is None:
                return
            if root.left is None and root.right is None:
                l.append(root.val)
            recurr(root.left,l)
            recurr(root.right,l)
            return
        recurr(root1,self.l1)
        recurr(root2,self.l2)
        return self.l1==self.l2
        
            
        