# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lengthA=0
        lengthB=0
        curr=headA
        curr1=headB
        while(curr):
            lengthA+=1
            curr=curr.next
        while(curr1):
            lengthB+=1
            curr1=curr1.next
        if lengthA>lengthB:
            dif=lengthA-lengthB
            while(dif>0):
                headA=headA.next
                dif-=1
        
        elif lengthA<lengthB:
            dif=lengthB-lengthA
            while(dif>0):
                headB=headB.next
                dif-=1
        curr=headA
        curr1=headB
        while(curr):
            if curr1==curr:
                return curr
            curr=curr.next
            curr1=curr1.next
        return None

    
        