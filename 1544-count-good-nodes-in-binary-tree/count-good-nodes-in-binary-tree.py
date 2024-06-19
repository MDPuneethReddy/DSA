# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        maxi=root.val
        def recurr(root,maxi,count):
            if root is None:
                return count
            if root.val>=maxi:
                count[0]+=1
                maxi=max(maxi,root.val)
            recurr(root.left,maxi,count)
            recurr(root.right,maxi,count)
            return count
        return recurr(root,root.val,[0])[0]



        