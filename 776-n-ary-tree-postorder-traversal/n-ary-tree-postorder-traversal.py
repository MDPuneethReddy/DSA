"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        self.values=[]
        def recurr(root):
            if root is None:
                return
            if root.children:
                for i in range(len(root.children)):
                    recurr(root.children[i])
            self.values.append(root.val)
            return
        recurr(root)
        return self.values

        