# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, temp, currSum):
            if not node:
                return
            
            temp.append(node.val)
            currSum += node.val

            # check if leaf and sum matches
            if not node.left and not node.right:
                if currSum == targetSum:
                    res.append(list(temp))          # append a copy
            else:
                dfs(node.left, temp, currSum)
                dfs(node.right, temp, currSum)

            temp.pop()
        
        dfs(root, [], 0)
        return res


