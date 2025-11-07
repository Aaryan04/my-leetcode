class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]         # keeping tracking of parents of each island
        self.island_size = [1] * n                 # stores the size of the connected island for each root
    
    # Function that finds the root of a node with path compression
    def find_root(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find_root(self.parent[node])
        return self.parent[node]

    # Function to union two sets based on size
    def union(self, node_a: int, node_b: int):
        root_a = self.find_root(node_a)
        root_b = self.find_root(node_b)

        if root_a == root_b:            # already in same set
            return
        
        # union by size - attach smaller island to bigger one
        if self.island_size[root_a] < self.island_size[root_b]:
            self.parent[root_a] = root_b
            self.island_size[root_b] += self.island_size[root_a]
        else:
            self.parent[root_b] = root_a
            self.island_size[root_a] += self.island_size[root_b]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        # both are same here since n x n
        n = len(grid)
        
        # funct to flatten 2D index to 1D index
        idx = lambda r, c: r * n + c

        # initial union find for the entire grid
        uf = UnionFind(n * n)

        # directions: up, down, left, right
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # step 1: union adjacent 1's in the grid
        for r in range(n):
            for c in range(n):
                    if grid[r][c] == 1:
                        # flatten 2D index to 1D index
                        curr_node = r * n + c
                        for dr, dc in directions:
                            nr, nc = r+dr, c+dc
                            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                                neighbor = nr * n + nc
                                uf.union(curr_node, neighbor)

        # Step 2: Calc max possible island size
        max_island = 0
        # flag to check if there are any zeros in the grid
        has_zero = False

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    has_zero = True
                    seen = set()
                    new_size = 1        # flipping this zero

                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:   
                            root = uf.find_root(nr * n + nc)
                            
                            if root not in seen:
                                seen.add(root)
                                new_size += uf.island_size[root]
                            
                    max_island = max(max_island, new_size)

        if not has_zero:
            return n*n

        return max_island




