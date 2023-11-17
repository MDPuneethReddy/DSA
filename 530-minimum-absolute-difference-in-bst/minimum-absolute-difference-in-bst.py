# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # self.mini=inf
        # def recurr(root):
        #     if root is None:
        #         return
        #     if root.left:
        #         self.mini=min(self.mini,abs(root.val-root.left.val))
        #     if root.right:
        #         self.mini=min(self.mini,abs(root.val-root.right.val))
        #     recurr(root.left)
        #     recurr(root.right)
        #     return
        # recurr(root)
        # return self.mini
        self.values=[]
        def recurr(root):
            if root is None:
                return 
            self.values.append(root.val)
            recurr(root.left)
            recurr(root.right)
            return
        recurr(root)
        self.values.sort()
        if self.values==[]:
            return []
        if len(self.values)==1:
            return self.values[0]
        else:
            val=inf
            for i in range(1,len(self.values)):
                val=min(val,abs(self.values[i]-self.values[i-1]))
            return val
        