class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)         # a -> list of pairs[b, a/b]

        for i, eqn in enumerate(equations):
            a, b = eqn
            adj[a].append([b, values[i]])
            adj[b].append([a, 1/values[i]])

        # a/b, a(src) -> b(target)
        def bfs(src, target):
            if src not in adj or target not in adj:
                return -1
            
            q = deque()
            visit = set()
            q.append([src, 1])
            visit.add(src)

            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for nei, weight in adj[n]:
                    if nei not in visit:
                        q.append([nei, w * weight])
                        visit.add(nei)
            return -1
        return [bfs(src, target) for src, target in queries]