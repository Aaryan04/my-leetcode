# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findClosestLeaf(self, root: Optional[TreeNode], k: int) -> int:
        
        # convert tree to graph
        graph = defaultdict(list)
        leaves = set()

        def dfs(root):
            if not root:
                return    
            
            if not root.left and not root.right:
                leaves.add(root.val)
            
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)

            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)

            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        # print(graph)

        q = deque([k])
        visited = {k}
        while q:
            curr_node = q.popleft()

            if curr_node in leaves:
                return curr_node
            
            for neighbor in graph[curr_node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)





