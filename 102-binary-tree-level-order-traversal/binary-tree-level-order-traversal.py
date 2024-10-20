
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        queue=[root,None]
        mainValues=[]
        levelValues=[]
        while(True):
            v=queue.pop(0)
            if v==None:
                mainValues.append(levelValues)
                if len(queue)==0:
                    return mainValues
                else:
                    queue.append(None)
                levelValues=[]
            else:
                levelValues.append(v.val)
                if v.left:
                    queue.append(v.left)
                if v.right:
                    queue.append(v.right)
        return mainValues




        
        