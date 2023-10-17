# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d={}
        def recurr(root):
            if root is None:
                return
            if root.val in d:
                d[root.val]+=1
            else:
                d[root.val]=1
            recurr(root.left)
            recurr(root.right)
            return
        recurr(root)
        c=0
        for i in d:
            c=max(c,d[i])
        val=[]
        for i in d:
            if d[i]==c:
                val.append(i)
        return val


        