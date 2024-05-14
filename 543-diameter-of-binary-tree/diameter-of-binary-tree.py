# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiamter=0
        def recurrsion(root):
            if root is None:
                return 0
            leftVal=recurrsion(root.left)
            rightVal=recurrsion(root.right)
            height=1+max(leftVal,rightVal)
            diameter=1+leftVal+rightVal
            self.maxDiamter=max(self.maxDiamter,diameter)
            # print(self.maxDiamter,diameter)
            return height
        recurrsion(root)
        return self.maxDiamter-1
        