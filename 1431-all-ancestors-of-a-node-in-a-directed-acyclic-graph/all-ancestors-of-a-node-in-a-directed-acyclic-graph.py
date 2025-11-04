class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])

        print(graph)
        def get_topo(graph):
            visited = set()
            topo_order = [] 

            def dfs(node):
                visited.add(node)
                for neigh in graph[node]:
                    if neigh not in visited:
                        dfs(neigh)
                topo_order.append(node)
                
            for node in range(n):
                if node not in visited:
                    dfs(node)
            topo_order = topo_order[::-1]
            return topo_order

        topo_order = get_topo(graph)
        print(topo_order)
        ancestors = [set() for _ in range(n)]

        for u in topo_order:
            for v in graph[u]:
                ancestors[v].update(ancestors[u])
                ancestors[v].add(u)
        
        return [sorted(list(s)) for s in ancestors]










