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
        
        second_list=slow.next
        slow.next=None

        prev=None

        while second_list:
            temp=second_list.next
            second_list.next=prev
            prev=second_list
            second_list=temp
        
        second_list=prev
        first_list=head

        while first_list and second_list:
            temp1,temp2=first_list.next,second_list.next
            first_list.next=second_list
            second_list.next=temp1
            second_list=temp2
            first_list=temp1
        

        
  


        