class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(c + 1)]
        visit = [False] * (c + 1)
        for u, v in connections:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, comp):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    comp.add(nei)
                    dfs(nei, comp)

        offOnMap = {}
        nodeToId = {} 
        comp_id = 0 
        for node in range(1, c + 1):
            if not visit[node]:
                visit[node] = True
                comp = {node}
                dfs(node, comp)
                offOnMap[comp_id] = [SortedList(comp), SortedList()]
                for node in comp:
                    nodeToId[node] = comp_id
                comp_id += 1
        
        res = [] 
        for x, n in queries:
            comp_id = nodeToId[n]
            online, offline = offOnMap[comp_id]

            if x == 1:    
                # now we check if this station is online
                if n in online:
                    res.append(n)
                elif online and n in offline:
                    res.append(online[0])
                else:
                    res.append(-1)
            else:
                if online and n in online:
                    online.remove(n)
                    offline.add(n)
        
        return res