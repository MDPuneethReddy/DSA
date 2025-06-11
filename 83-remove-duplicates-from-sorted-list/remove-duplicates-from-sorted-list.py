# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        curr=head
        nextp=curr.next
        while(nextp):
            if curr.val==nextp.val:
                nextp=nextp.next
                curr.next=nextp
            else:
                curr=curr.next
                nextp=nextp.next
        return head
        