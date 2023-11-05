# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        if head and head.next is None:
            return head
        curr1=head
        curr2=head.next
        while(curr1 and curr2):
            # print(curr1.val, curr2.val)
            if curr1.val==curr2.val:
                temp=curr2.next
                curr1.next=temp
                curr2=temp
            else:
                curr1=curr1.next
                curr2=curr2.next
        return head
        