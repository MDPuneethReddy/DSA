# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.maxi=0
        def recurr(root,minvalue,maxvalue):
            
            if root is None:
                return 
            # print(root.val,minvalue,maxvalue)
            leftvalue=min(root.val,minvalue)
            rightvalue=max(root.val,maxvalue)
            recurr(root.left,leftvalue,rightvalue)
            recurr(root.right,leftvalue,rightvalue)
            self.maxi=max(self.maxi,abs(rightvalue-leftvalue))
            return 
        recurr(root,root.val,root.val)
        return self.maxi