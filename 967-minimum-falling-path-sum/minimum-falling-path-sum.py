import math
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # TABULATION - BOTTOM UP
        n = len(matrix)
        dp = [[None] * n for _ in range(n)]

        # filling the 0th row of the dp matrix
        for j in range(n):
            dp[0][j] = matrix[0][j]

        # now for each row starting at row = 1
        for i in range(1, n):
            for j in range(n):      # and for each column 
                up = matrix[i][j] + dp[i-1][j]
                left_d = matrix[i][j] + dp[i-1][j-1] if j-1 >= 0 else math.inf      # with OOB condition
                right_d = matrix[i][j] + dp[i-1][j+1] if j+1 < n else math.inf      # with OOB condition

                dp[i][j] = min(up, left_d, right_d)

        # finding the min of last row of dp matrix
        min_res = dp[n-1][0]
        for j in range(1, n):
            min_res = min(min_res, dp[n-1][j])

        return min_res




        
        
        
        # RECURSION + MEMOIZATION

        # n = len(matrix)
        # dp = [[None] * n for _ in range(n)]
        # def f(i, j):
        #     # base cases
        #     # out of bound
        #     if j < 0 or j >= n: return math.inf
        #     # destination
        #     if i == 0: return matrix[i][j]
        #     # check if already existing in dp
        #     if dp[i][j] is not None: return dp[i][j]

        #     # exploring all possible paths
        #     st_up = matrix[i][j] + f(i-1, j)
        #     left_diag = matrix[i][j] + f(i-1, j-1)
        #     right_diag = matrix[i][j] + f(i-1, j+1)
            
        #     dp[i][j] = min(st_up, left_diag, right_diag)
        #     # return what we need at the end (max, min, cnt)
        #     return dp[i][j]

        # minVal = math.inf
        # for j in range(n):
        #     minVal = min(minVal, f(n-1, j))
        # return minVal
        