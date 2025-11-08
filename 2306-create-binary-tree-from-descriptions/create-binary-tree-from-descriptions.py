# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        child_set = set()                    # track child for finding root as root cannot be child
        node_map = {}                       # {node val: tree object} to avoid creating duplicate nodes

        # iterate through descriptions
        for parent, child, isLeft in descriptions:
            child_set.add(child)

            # check if parent not in node_map: add parent and create tree node
            if parent not in node_map:
                node_map[parent] = TreeNode(parent)
            # get the parent node from node_map
            parent_node = node_map[parent]

            # similarly for child
            if child not in node_map:
                node_map[child] = TreeNode(child)
            child_node = node_map[child]

            # connect parent nodes and child nodes            
            if isLeft:
                parent_node.left = child_node
            else:
                parent_node.right = child_node

        
        root_val = -1
        # iterate again through descriptions
        for parent, _, _ in descriptions:
            # if parent is not in child set, it means we have found the root
            if parent not in child_set:
                return node_map[parent]         # return directly the root node from node map as we have already connected all the nodes
                
        
