# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def dfs(node, path, currSum):
            if not node:
                return
            
            # 1. add curr node to path and update the sum
            path.append(node.val)
            currSum += node.val

            # 2. check if leaf and sum matches
            if not node.left and not node.right:
                if currSum == targetSum:
                    res.append(list(path))          # append a copy
            
            # 3. recurse to left and right nodes
            else:
                dfs(node.left, path, currSum)
                dfs(node.right, path, currSum)

            # 4. backtrack (remove the node we added in step 1)
            path.pop()
        
        dfs(root, [], 0)
        return res


