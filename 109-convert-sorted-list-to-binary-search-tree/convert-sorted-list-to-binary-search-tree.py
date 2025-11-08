# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        # converting linked list to array and then running pre order traversal
        def to_list(head:ListNode) -> list:
            vals = []
            while head:
                vals.append(head.val)
                head = head.next
            return vals

        values = to_list(head)

        def helper(l, r):
            if l > r:
                return None
            
            # always choose left middle left node
            m = (l + r) // 2

            # preorder traversal : node -> left -> right
            root = TreeNode(values[m])

            if l == r:
                return root

            root.left = helper(l, m-1)
            root.right = helper(m+1, r)
            return root

        return helper(0, len(values)-1)