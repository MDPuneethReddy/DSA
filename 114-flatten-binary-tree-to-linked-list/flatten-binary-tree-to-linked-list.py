# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def recurr(root):
            if root is None:
                return root 
            if root.left is None and root.right is None:
                return root
            if root.left is not None and root.right is None:
                root.right=root.left
                root.left=None       
            left=recurr(root.left)
            right=recurr(root.right)
            temp=right
            root.right=left
            # root.right.right=temp
            curr=root
            while(curr.right):
                if curr is None:
                    break
                curr=curr.right
            curr.right=temp
            root.left=None
            return root
        recurr(root)
        
            
        