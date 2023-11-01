# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        l=[]
        newTree=TreeNode()
        self.curr=newTree
        def recurr(root):
            if root is None:
                return 
            recurr(root.left)
            l.append(root.val)
            self.curr.right=TreeNode(root.val)
            self.curr=self.curr.right
            recurr(root.right)
            return
        recurr(root)
        
        return newTree.right
        