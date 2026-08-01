# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return None
        curr1=list1
        curr2=list2
        newNode=ListNode()
        dummy=newNode
        while curr1 and curr2:
            #case I - equal or curr1 less
            if curr1.val<=curr2.val:
                newNode.val=curr1.val
                newNode.next=ListNode()
                curr1=curr1.next
                newNode=newNode.next
            else:
                newNode.val=curr2.val
                newNode.next=ListNode()
                curr2=curr2.next
                newNode=newNode.next

        if  curr1==None:
            newNode.val=curr2.val
            newNode.next=curr2.next
        else:
            newNode.val=curr1.val
            newNode.next=curr1.next

        
        return dummy


        