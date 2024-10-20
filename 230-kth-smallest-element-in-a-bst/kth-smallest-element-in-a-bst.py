# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        mainValue=[]
        def recurr(root,k):
            if root is None:
                return
            recurr(root.left,k)
            mainValue.append(root.val)
            recurr(root.right,k)
            return
        recurr(root,k)
        return mainValue[k-1]

        
        