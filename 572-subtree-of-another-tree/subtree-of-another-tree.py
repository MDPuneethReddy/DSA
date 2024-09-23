# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkequal(root1,root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            if root1.val != root2.val:
                return False
            return checkequal(root1.left,root2.left) and checkequal(root1.right,root2.right)
        
        self.value=False
        def recurr(root,subRoot):
            if root is None and subRoot is None:
                return True
            if root:
                if root and subRoot and root.val==subRoot.val:
                    self.value=self.value or checkequal(root,subRoot)
                recurr(root.left,subRoot)
                recurr(root.right,subRoot)
            return
        recurr(root,subRoot)
        return self.value
        