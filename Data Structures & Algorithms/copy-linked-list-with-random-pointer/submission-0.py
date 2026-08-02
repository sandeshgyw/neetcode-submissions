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
        hashmap={None:None}


        while current:
            if current not in hashmap:
                node=Node(current.val)
                hashmap[current]=node
            current=current.next
        #we have all new nodes now in hashmap
        #now lets map

        current=head
        while current:

            hashmap[current].next=hashmap[current.next]
            hashmap[current].random=hashmap[current.random]
            current=current.next
        
        return hashmap[head]
            
       



        


        