class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
            m, n = len(grid), len(grid[0])
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            visited = [[False] * n for _ in range(m)]

            # max heap - store as negative  
            heap = [(-grid[0][0], 0, 0)]            # val, i, j
            visited[0][0] = True
            res = grid[0][0]

            while heap:
                val, i, j = heapq.heappop(heap)
                val = -val
                res = min(res, val)

                if (i, j) == (m-1, n-1):
                    return res
                
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj]:
                        visited[ni][nj] = True
                        heapq.heappush(heap, (-grid[ni][nj], ni, nj))
            return res        
        
        
        
        # BINARY SEARCH + BFS APPROACH
        # TC: O(MN x LOG V)     # little slow because of log v where v = range of possible cell values in the grid
        # we can optimize using max-heap 
        # SC: O(MN)
        # m, n = len(grid), len(grid[0])
        # directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # def canReach(t):
        #     if grid[0][0] < t:
        #         return False

        #     q = deque([(0, 0)])
        #     visited = [[False]*n for _ in range(m)]
        #     visited[0][0] = True

        #     while q:
        #         i, j = q.popleft()
        #         if (i, j) == (m-1, n-1):
        #             return True
        #         for dr, dc in directions:
        #             ni, nj = i + dr, j + dc
        #             if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj] and grid[ni][nj] >= t :
        #                 visited[ni][nj] = True
        #                 q.append((ni, nj))
        #     return False

        # low, high = 0, max(max(row) for row in grid)            # find mid of max and min value in the grid
        # ans = 0
        # while low <= high:
        #     mid = (low + high) // 2           #mid will act as my threshold
        #     if canReach(mid):               # check if we can reach our target with curr threshold
        #         ans = mid
        #         low = mid + 1               # will try to find a higher value then prev threshold
        #     else:
        #         high = mid - 1              # lower the threshold if we cant reach target with prev threshold
        # return ans            