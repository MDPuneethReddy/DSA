# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.d=set()
        def recurr(root,level,avgs):
            if root is None:
                return avgs
            if level not in self.d:
                self.d.add(level)
                avgs.append([root.val,1])
            else:
                avgs[level][0]+=root.val
                avgs[level][1]+=1
            recurr(root.left,level+1,avgs)
            recurr(root.right,level+1,avgs)
            return avgs
        values =recurr(root,0,[])
        mainValues=[]
        for i in values:
            mainValues.append(i[0]/i[1])
        return mainValues


        
        