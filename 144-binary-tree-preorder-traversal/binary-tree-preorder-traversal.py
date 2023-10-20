# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l=[]
        def recurr(root):
            if root is None:
                return
            l.append(root.val)
            recurr(root.left)
            recurr(root.right)
            return
        recurr(root)
        return l
        