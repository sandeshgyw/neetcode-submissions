# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1=list1
        current2=list2
        dummy=ListNode()
        merged=dummy
 

        while current1 and current2:
            if current1.val<=current2.val:
                dummy.next=current1
                current1=current1.next
            else:
                dummy.next=current2
                current2=current2.next
            dummy=dummy.next
        
        if not current1:
            dummy.next=current2
        if not current2:
            dummy.next=current1
        
        return merged.next




        