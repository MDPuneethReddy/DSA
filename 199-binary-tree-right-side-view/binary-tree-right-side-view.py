#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        def recurr(root,level,mainList,dlevel):
            if root is None:
                return mainList
            if level not in dlevel:
                mainList.append(root.val)
                dlevel.add(level)
            recurr(root.right,level+1,mainList,dlevel)
            recurr(root.left,level+1,mainList,dlevel)
            return mainList
        return recurr(root,0,[],set())


        