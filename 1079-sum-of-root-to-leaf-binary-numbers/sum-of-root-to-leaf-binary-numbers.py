# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.tsum=0
        self.s=[]
        def recurr(root):
            if root is None:
                return
            if root.left is None and root.right is None:
                val="".join(self.s)
                val+=str(root.val)
                self.tsum+=int(val,2)
                return
            self.s.append(str(root.val))
            recurr(root.left)
            recurr(root.right)
            self.s.pop()
            return
        recurr(root)
        return self.tsum
            
        
        