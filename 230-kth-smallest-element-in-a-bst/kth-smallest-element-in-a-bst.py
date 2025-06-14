# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        output=[]
        self.ind=k
        def recurr(root):
            if root is None:
                return
            recurr(root.left)
            if self.ind==1:
                output.append(root.val)
            self.ind-=1
            recurr(root.right)
            return
        recurr(root)
        return output[0]

        