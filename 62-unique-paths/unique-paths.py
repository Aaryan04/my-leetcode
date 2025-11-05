class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # f(i, j) = num of ways to reach cell (i, j)
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = 1        # base case

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue            # base case
                
                # copy the exact same recurrence logic in this
                up = dp[i-1][j] if i > 0 else 0
                left = dp[i][j-1] if j > 0 else 0
                
                dp[i][j] = up + left

        return dp[m-1][n-1]



        # MEMOIZATION SOLUTION
        # dp = [[-1 for _ in range(n)] for _ in range(m)]

        # def dfs(i, j):
        #     if i == 0 and j == 0:
        #         return 1
        #     if i < 0 or j < 0:
        #         return 0
        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     up = dfs(i-1, j)
        #     left = dfs(i, j-1)
        #     dp[i][j] = up + left
            
        #     return dp[i][j]
        
        # return dfs(m-1, n-1)