# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # basically copy the next node val to the current node and remove the next node
        temp=node.next
        value=node.next.val
        node.val=value
        node.next=temp.next
        