class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set()
        visited.add(source)

        def dfs(node):
            if node == destination:
                return True
            
            for neigh in adj_list[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    if dfs(neigh):
                        return True

            return False

        return dfs(source)

