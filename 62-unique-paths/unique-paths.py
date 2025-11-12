class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # f(i,j) -> no of ways to reach (0, 0) => (i, j)

        dp = [[0 for _ in range(n)] for _ in range(m)]

        # base case
        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                up = dp[i-1][j] if i > 0 else 0
                left = dp[i][j-1] if j > 0 else 0
            
                dp[i][j] = up + left
            
        return dp[m-1][n-1]

        # dp = [[-1 for _ in range(n)] for _ in range(m)]

        # def dfs(i, j):
        #     # BASE CASES
        #     # reached destination
        #     if i == 0 and j == 0:
        #         return 1

        #     # out of bound condition
        #     if i < 0 or j < 0:
        #         return 0

        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     # do all stuff on i, j
        #     up = dfs(i-1,  j)
        #     left = dfs(i, j-1)
        #     dp[i][j] = up + left

        #     return dp[i][j]        # cnt ways by summing

        # return dfs(m-1,n-1)