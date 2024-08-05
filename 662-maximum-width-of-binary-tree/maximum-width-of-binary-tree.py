# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d={}
        def recurr(root,level,val):
            if root is None:
                return
            recurr(root.left,level+1,2*val)
            recurr(root.right,level+1,(2*val)+1)
            if level not in d:
                d[level]=[val,val]
            else:
                d[level][0]=min(d[level][0],val)
                d[level][1]=max(d[level][0],val)
            return
        recurr(root,0,0)
        maxi=-math.inf
        for i in d:
            maxi=max(maxi,abs(d[i][1]-d[i][0])+1)
        return maxi
        