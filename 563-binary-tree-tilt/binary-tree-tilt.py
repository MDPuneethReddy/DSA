# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.sum=0
        def recurr(root):
            if root is None:
                return 0
            leftValue=recurr(root.left)
            rightValue=recurr(root.right)
            self.sum=self.sum+abs(leftValue-rightValue)
            # print(root.val,leftValue,rightValue,abs(leftValue-rightValue))
            return root.val+leftValue+rightValue
        recurr(root)
        return self.sum
        
        
        