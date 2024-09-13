# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        left=dummy
        right=head
        i=0
        while(i<n):
            right=right.next
            i+=1
        while(right):
            left=left.next
            right=right.next
        # print(left,right)
        if left is None or left.next is None:
            return head
        left.next=left.next.next
        return dummy.next
        