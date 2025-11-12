class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # this problem is similar to ninja training problem
        
        n = len(costs)            # num of houses we have
        if n == 0 :
            return 0

        # 1. Create the DP table
        #    dp[h][0] = min cost ending with Red at house h
        #    dp[h][1] = min cost ending with Blue at house h
        #    dp[h][2] = min cost ending with Green at house h
        dp = [[0] * 3 for _ in range(n)]
        
        # 2. base case (house 0)
        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]

        for h in range(1, n):
            dp[h][0] = costs[h][0] + min(dp[h-1][1], dp[h-1][2])
            dp[h][1] = costs[h][1] + min(dp[h-1][0], dp[h-1][2])
            dp[h][2] = costs[h][2] + min(dp[h-1][0], dp[h-1][1])
        
        return min(dp[n-1][0], dp[n-1][1], dp[n-1][2])









        # dp = [[-1] * 4 for _ in range(n)]

        # def calc_cost(h, last):
        #     if dp[h][last] != -1:
        #         return dp[h][last]

        #     if h == 0:
        #         min_cost = math.inf
        #         for i in range(3):
        #             if i != last:
        #                 min_cost = min(min_cost, costs[0][i])
        #                 dp[h][last] = min_cost
        #         return dp[h][last]

        #     min_cost = math.inf
        #     for i in range(3):
        #         if i != last:
        #             cost = costs[h][i] + calc_cost(h-1, i)           # recurse to prev house and last = i
        #             min_cost = min(min_cost, cost)
        #             dp[h][last] = min_cost    
        #     return dp[h][last]

        # return calc_cost(n-1, 3)
