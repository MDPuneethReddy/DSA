# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head.next is None:
            return head
        curr=head.next
        prev=head
        while(curr):
            if curr.val==prev.val:
                curr=curr.next
                prev.next=curr
            else:
                curr=curr.next
                prev=prev.next
        # print(prev,curr)
        return head
        