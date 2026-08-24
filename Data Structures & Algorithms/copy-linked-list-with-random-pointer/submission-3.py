"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current=head
        if not head:
            return None

        while current:
            copy=Node(current.val)
            copy.next=current.next
            current.next=copy
            current=copy.next
        
        current=head

        newHead=current.next

        while current:
            copy=current.next
            copy.random=current.random.next if current.random else None
            current=copy.next
        
        current=head

        while current:
            copy=current.next
            current.next=current.next.next if current.next else None
            copy.next=copy.next.next if copy.next else None
            current=current.next
            
            
        return newHead
        
        

                

            
            
                

        
        