# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])

        while q:
            qLen = len(q)
            rhs = None
            for i in range(qLen):
                node = q.popleft()
                if node:
                    rhs = node
                    q.append(node.left)
                    q.append(node.right)   
            if rhs:
                res.append(rhs.val)

        return res                     