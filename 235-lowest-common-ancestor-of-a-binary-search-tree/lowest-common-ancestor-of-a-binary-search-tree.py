# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        value=[]
        def recurr(root,p,q):
            if root is None:
                return [False,False]
            left=recurr(root.left,p,q)
            right=recurr(root.right,p,q)
            value1=False
            value2=False
            if root.val==p:
                value1=True
            if root.val==q:
                value2=True
            if left[0]==True or right[0]==True:
                value1=True
            if left[1]==True or right[1]==True:
                value2=True
            if value1==True and value2==True and len(value)==0:
                value.append(root.val)
            # print(value1,value2,root.val)
            return [value1,value2]
        recurr(root,p.val,q.val)
        return TreeNode(value[0])

        