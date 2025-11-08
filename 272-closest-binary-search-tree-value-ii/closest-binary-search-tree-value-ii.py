# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:

        # Step 1: init stacks
        preds, succs = [], []
        self.init_stack(root, target, k, preds, succs)

        res = []

        # Step 2: pick k closest
        for _ in range(k):
            if not preds:
                res.append(self.get_next_succs(succs))
            elif not succs:
                res.append(self.get_next_preds(preds))
            else:
                if abs(preds[-1].val - target) <= abs(succs[-1].val - target):
                    res.append(self.get_next_preds(preds))
                else:
                    res.append(self.get_next_succs(succs))
        return res


    def init_stack(self, root, target, k, preds, succs):
        while root:
            if root.val <= target:
                preds.append(root)
                root = root.right
            else:
                succs.append(root)
                root = root.left
            
    def get_next_preds(self, preds):
        node = preds.pop()
        val = node.val
        node = node.left
        while node:
            preds.append(node)
            node = node.right
        return val
    
    def get_next_succs(self, succs):
        node = succs.pop()
        val = node.val
        node = node.right
        while node:
            succs.append(node)
            node = node.left
        return val


