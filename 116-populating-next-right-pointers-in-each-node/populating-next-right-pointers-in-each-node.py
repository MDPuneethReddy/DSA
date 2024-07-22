"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.levels={}
        def recurr(root,level):
            if root is None:
                return
            if level in self.levels:
                v=self.levels[level]
                v.next=root
                self.levels[level]=root
            else:
                self.levels[level]=root
            recurr(root.left,level+1)
            recurr(root.right,level+1)
            return
        recurr(root,0)
        for i in self.levels:
            self.levels[i].next=None
        return root
            

        