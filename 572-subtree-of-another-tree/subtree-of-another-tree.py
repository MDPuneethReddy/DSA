# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.boolean=False
        def checkEqual(root,subRoot):
            if root is None and subRoot is None:
                return True
            if root is not None and subRoot is None:
                return False
            if root is None and subRoot is not None:
                return False
            if root.val!=subRoot.val:
                return False
            return checkEqual(root.left,subRoot.left) and checkEqual(root.right,subRoot.right)
        def recurrsion(root,subRoot):
            if root is None:
                return True
            if root.val==subRoot.val:
                self.boolean=self.boolean or checkEqual(root,subRoot)
            recurrsion(root.left,subRoot)
            recurrsion(root.right,subRoot)
            return
        recurrsion(root,subRoot)
        return self.boolean
            
        