# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current1=l1
        current2=l2
        dummy=result=ListNode(0)
        carry=0

        while current1 or current2 or carry:
            total=(current1.val if current1 else 0) + (current2.val if current2 else 0) + carry
            carry=total//10
            digit=total%10
            
           
            result.next=ListNode(digit)
            
            current1=current1.next if current1 else None
            current2=current2.next if current2 else None
            result=result.next

 
        return dummy.next





                