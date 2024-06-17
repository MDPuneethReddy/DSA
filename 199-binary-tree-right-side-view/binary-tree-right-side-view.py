#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        l=[root,None]
        mainList=[]
        while(True):
            value=l.pop(0)
            if value==None:
                if len(l)==0:
                    break
                else:
                    l.append(None)
            else:
                if len(l) > 0 and l[0] is None:
                    mainList.append(value.val)
                if value.left:
                    l.append(value.left)
                if value.right:
                    l.append(value.right)
        return mainList

            


        