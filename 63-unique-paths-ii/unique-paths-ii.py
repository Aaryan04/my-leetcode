class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def dfs(i, j):
            # BASE CASES
            # reached destination
            if obstacleGrid[i][j] == 1:
                return 0

            if i == 0 and j == 0:
                return 1

            # out of bound condition
            if i < 0 or j < 0:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]
            
            # do all stuff on i, j
            up = dfs(i-1,  j)
            left = dfs(i, j-1)
            dp[i][j] = up + left

            return dp[i][j]        # cnt ways by summing

        return dfs(m-1,n-1)