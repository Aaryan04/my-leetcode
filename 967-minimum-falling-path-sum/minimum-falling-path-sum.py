import math
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[None] * n for _ in range(n)]
        def f(i, j):
            # base cases
            # out of bound
            if j < 0 or j >= n: return math.inf
            # destination
            if i == 0: return matrix[i][j]
            # check if already existing in dp
            if dp[i][j] is not None: return dp[i][j]

            # exploring all possible paths
            st_up = matrix[i][j] + f(i-1, j)
            left_diag = matrix[i][j] + f(i-1, j-1)
            right_diag = matrix[i][j] + f(i-1, j+1)
            
            dp[i][j] = min(st_up, left_diag, right_diag)
            # return what we need at the end (max, min, cnt)
            return dp[i][j]

        minVal = math.inf
        for j in range(n):
            minVal = min(minVal, f(n-1, j))
        return minVal
        