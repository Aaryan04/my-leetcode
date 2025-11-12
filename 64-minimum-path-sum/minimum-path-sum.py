class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # f(i, j) -> min sum of path to reach i, j from (0, 0)
        # TABULATION SOLUTION
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    up = grid[i][j] + dp[i-1][j]  if i > 0 else math.inf
                    left = grid[i][j] + dp[i][j-1] if j > 0 else math.inf

                    dp[i][j] = min(up, left)
            
        return dp[m-1][n-1]
        
        
        
        
        
        
        
        # MEMOIZATION SOLUTION
        # m = len(grid)
        # n = len(grid[0])
        # dp = [[-1 for _ in range(n)] for _ in range(m)]
        # def dfs(i, j):
        #     if i == 0 and j == 0:           # if we find 0, 0 then return the grid[0][0] value
        #         return grid[0][0]
            
        #     if i < 0 or j < 0:
        #         return math.inf             # return a number with is ignored while calc min path sum

        #     if dp[i][j] != -1:
        #         return dp[i][j]

        #     up = grid[i][j] + dfs(i-1, j)
        #     left = grid[i][j] + dfs(i, j-1)
        #     dp[i][j] = min(up, left)
        #     return dp[i][j]

        # return dfs(m-1, n-1)