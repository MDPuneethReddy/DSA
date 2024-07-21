# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def recurr(self,root):
        if root is None:
            return
        self.stack.append(root)
        if root.left:
            self.recurr(root.left)
        return

    def __init__(self, root: Optional[TreeNode]):
        self.root=root
        self.stack=[]
        self.recurr(root)
        

    def next(self) -> int:
        value=self.stack.pop()
        self.recurr(value.right)
        return value.val
        

    def hasNext(self) -> bool:
        if len(self.stack)>0:
            return True
        else:
            return False
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()