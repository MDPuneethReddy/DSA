# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while(head):
            if head.val==val:
                head=head.next
            else:
                break
        if head is None:
            return head
        prev=head
        curr=head.next
        while curr:
            if curr.val==val:
                prev.next=curr.next
                curr=curr.next
            else:
                curr=curr.next
                prev=prev.next
        return head
        