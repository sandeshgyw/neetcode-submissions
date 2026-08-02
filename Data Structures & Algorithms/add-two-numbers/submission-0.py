# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        first=l1
        second=l2
        dummy=newList=ListNode()
        carry=0

        while l1:
            newList.next=ListNode()
            newList=newList.next
            
            if l1 and l2 and l1.val+l2.val >=10:
                carry= math.floor((l1.val+l2.val)/10)

            newList.val=((l1.val+l2.val)%10)
            l1,l2=l1.next,l2.next
        
        if carry:
            newList.next=ListNode(carry)
        
        return dummy.next

        


