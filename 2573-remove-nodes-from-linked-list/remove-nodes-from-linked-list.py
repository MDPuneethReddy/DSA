# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output=ListNode()
        values=[]
        curr=head
        while(curr):
            values.append(curr.val)
            curr=curr.next
        maxiValues=[]
        maxi=-math.inf
        for i in range(len(values)):
            if values[len(values)-i-1]>maxi:
                maxi=max(maxi,values[len(values)-i-1])
            maxiValues.append(maxi)
        maxiValues=maxiValues[::-1]
        # print(maxiValues)
        curr1=head
        i=0
        curr=output
        while(curr1):
            if curr1.val==maxiValues[i]:
                curr.next=ListNode(curr1.val)
                curr=curr.next
            curr1=curr1.next
            i+=1
        return output.next



        return head


        