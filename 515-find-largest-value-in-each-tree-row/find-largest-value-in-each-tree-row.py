# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        res = []

        while q:
            qLen = len(q)
            max_of_lvl = -math.inf
            for _ in range(qLen):
                node = q.popleft()
                max_of_lvl = max(max_of_lvl, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(max_of_lvl)

        return res