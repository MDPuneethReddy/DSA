# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        mainTree=TreeNode()
        self.curr=mainTree
        def recurr(root):
            # print(mainTree)
            if root is None:
                return 
            recurr(root.left)
            self.curr.right=TreeNode(root.val)
            self.curr=self.curr.right
            recurr(root.right)
            return 
        recurr(root)
        return mainTree.right
        
            
        