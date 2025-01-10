# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        flistiter=l1
        slistiter=l2
        output=ListNode()
        curr=output
        extra=0
        while(flistiter or slistiter):
            value1=0
            value2=0
            if flistiter is not None:
                value1=flistiter.val
                flistiter=flistiter.next
            if slistiter is not None:
                value2=slistiter.val
                slistiter=slistiter.next
            total=value1+value2+extra
            v=total%10
            v1=total//10
            # print(v,v1)
            curr.next=ListNode(v)
            curr=curr.next
            extra=v1
        if extra!=0:
            curr.next=ListNode(extra)
            curr=curr.next
        return output.next

        
        