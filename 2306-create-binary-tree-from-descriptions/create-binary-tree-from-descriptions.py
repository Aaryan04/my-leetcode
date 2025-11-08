# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        child_set= set()
        node_map = {}                       # {node val: tree object}

        for parent, child, isLeft in descriptions:
            child_set.add(child)
            if parent not in node_map:
                node_map[parent] = TreeNode(parent)
            parent_node = node_map[parent]
            if child not in node_map:
                node_map[child] = TreeNode(child)
            child_node = node_map[child]
            
            if isLeft:
                parent_node.left = child_node
            else:
                parent_node.right = child_node


        root_val = -1
        for parent, _, _ in descriptions:
            if parent not in child_set:
                return node_map[parent]
                
        
