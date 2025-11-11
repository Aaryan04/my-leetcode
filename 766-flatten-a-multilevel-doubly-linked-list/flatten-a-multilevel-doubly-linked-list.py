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

        tail = self.flatten_dfs(head)

        return head
        
    def flatten_dfs(self, node):
        curr = node
        tail = node

        while curr:

            # check if it has a child
            if curr.child:
                original_next = curr.next                      # save the next node
                child_tail = self.flatten_dfs(curr.child)          # recurse the child node as new head

                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None 

                child_tail.next = original_next
                if original_next:
                    child_tail.next.prev = child_tail             # connecting tail with og next 

                tail = child_tail                                 # update main tail to be child tail

                curr = original_next

            else:
                tail = curr
                curr = curr.next

        return tail

                
