# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast=head

        dummy=ListNode()
        dummy.next=head

        slow=dummy
        
        for i in range(n):
            fast=fast.next
        
        while fast:
            fast=fast.next
            slow=slow.next
        
        #slow is the node beofre to be removed node
        
        slow.next=slow.next.next

        

        return dummy.next



        