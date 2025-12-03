class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        n = len(nums)                               # nums = [1, n]
        graph = {i:[] for i in range(1, n+1)}       # adjacency_list
        indegree = [0] * (n+1)                      # indegree_list
        indegree[0] = -1

        # updating graph and indegree's
        for seq in sequences:
            for i in range(len(seq) - 1):
                u = seq[i]
                v = seq[i+1]
                graph[u].append(v)
                indegree[v] += 1
        
        q = deque([node for node in graph if indegree[node] == 0])          # q with 0 indegrees
        idx = 0                                     # curr index of nums

        while q:
            # if we have more than two options to select from then we cannot have unique sequence
            if len(q) > 1:
                return False
            
            node = q.popleft()
            # check if nums is following the unique path
            if nums[idx] != node:
                return False
            
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
                    idx += 1
                
        return True if idx == n-1 else False