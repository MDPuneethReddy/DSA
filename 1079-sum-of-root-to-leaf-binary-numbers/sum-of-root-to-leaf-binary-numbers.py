# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def recurr(root,bstr,totalValue):
            if root is None:
                return totalValue
            bstr+=str(root.val)
            if root.left is None and root.right is None:
                # print(bstr)
                totalValue[0]=totalValue[0]+int(bstr,2)
                return totalValue
            recurr(root.left,bstr,totalValue)
            recurr(root.right,bstr,totalValue)
            return totalValue
        return recurr(root,"",[0])[0]
