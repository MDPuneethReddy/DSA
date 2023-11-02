# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l=[]
        curr=head
        while(curr):
            l.append(curr.val)
            curr=curr.next
        for i in range(len(l)//2):
            if l[i]!=l[len(l)-i-1]:
                return False
        return True