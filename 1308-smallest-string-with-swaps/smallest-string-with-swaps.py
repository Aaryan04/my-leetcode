class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a,b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1
            
        for a, b in pairs:
            union(a,b)
            
        comps = defaultdict(list)

        for i in range(n):
            comps[find(i)].append(i)

        res = list(s)
        for idxs in comps.values():
            idxs.sort()
            chars = sorted(s[i] for i in idxs)
            for i, ch in zip(idxs, chars):
                res[i] = ch
        return ''.join(res)
