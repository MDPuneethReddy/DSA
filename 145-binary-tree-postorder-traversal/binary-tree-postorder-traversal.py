# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def recurr(root):
            if root is None:
                return
            recurr(root.left)
            recurr(root.right)
            l.append(root.val)
            return
        recurr(root)
        return l
        
        