# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        m=[]
        def recurr(root,path):
            if root is None:
                return
            # Append the current node's value to the path
            path += str(root.val)

            # If it's a leaf node, add the path to the result
            if not root.left and not root.right:
                m.append(path)
            else:
                path += '->'  # Add an arrow separator for non-leaf nodes

            # Recur for the left and right subtrees
            recurr(root.left, path)
            recurr(root.right, path)
            
        recurr(root,"")
        return m