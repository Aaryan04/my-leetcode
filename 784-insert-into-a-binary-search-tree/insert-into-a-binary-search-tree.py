# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # RECURSION
        # if not root:
        #     return TreeNode(val)

        # if root.val > val:
        #     root.left = self.insertIntoBST(root.left, val)
        # else:
        #     root.right = self.insertIntoBST(root.right, val)

        # return root

        # ITERATION
        node = root
        if not node:
            return TreeNode(val)
        while node:
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                    return root
                else:
                    node = node.left
            else:
                if not node.right:
                    node.right = TreeNode(val)
                    return root
                else:
                    node = node.right

        
