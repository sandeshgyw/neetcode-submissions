# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None

        current=head

        while current:
            #till we reach end of the list

            temp=current.next # we will ned this cause this is the next one to loop
            current.next=prev
            prev=current
            current=temp
        
        return prev
        