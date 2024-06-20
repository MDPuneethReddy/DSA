"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def recurr(root):
            if root is None:
                return 0
            values=[]
            for children in root.children:
                values.append( recurr(children))
            if len(values)==0:
                return 1
            else:
                return 1+max(values)
        return recurr(root)
        