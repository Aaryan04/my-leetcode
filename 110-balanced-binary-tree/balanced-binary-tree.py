# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:            # base case: reached the leaf nodes
                return (True, 0)
            left_bal, lh = dfs(node.left)
            right_bal, rh = dfs(node.right)

            isbalanced = left_bal and right_bal and abs(lh - rh) <= 1

            return (isbalanced, 1 + max(lh, rh))

        return dfs(root)[0]