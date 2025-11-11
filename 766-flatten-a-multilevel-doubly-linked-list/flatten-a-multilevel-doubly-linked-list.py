"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        curr = head
        
        while curr:
            if curr.child:
                # flatten child nodes
                og_next = curr.next                     # save the og next node before recursion
                curr.next = self.flatten(curr.child)         # returns the head of the child after flattening    
                curr.next.prev = curr
                curr.child = None

                # find tail
                while curr.next:
                    curr = curr.next                    # now curr points to the tail
                    
                # attach tail with next og_next
                if og_next:
                    curr.next = og_next
                    og_next.prev = curr

            curr = curr.next
        
        return head
