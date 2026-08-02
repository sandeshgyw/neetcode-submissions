# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast=head,head

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #so slow is the mid point
        
        curr2=slow.next
        slow.next=None

        prev=None

        while curr2:
            temp=curr2.next
            curr2.next=prev
            prev=curr2
            curr2=temp
        
        curr2=prev
        curr1=head

        while curr1 and curr2:
            temp1,temp2=curr1.next,curr2.next
            curr1.next=curr2
            curr1=curr1.next
            curr2.next=temp1
            curr2=temp2
            curr1=temp1
        

        
  


        