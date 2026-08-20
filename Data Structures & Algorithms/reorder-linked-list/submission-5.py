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
        list2=slow.next#list2
        slow.next=None
        list1=head#list1

        #now reverse list2
        prev=None
        curr=list2
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        list2=prev

        #now we merge list1 and list2
        dummy=ListNode()
        store=dummy
  
        while list1 and list2:
            if dummy.next==list1:
                dummy.next=list2
                list2=list2.next
            else:
                dummy.next=list1
                list1=list1.next
            dummy=dummy.next
        
        dummy.next=list1 if list1 else list2

            





