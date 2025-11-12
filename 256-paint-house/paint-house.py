class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # this problem is similar to ninja training problem
        
        n = len(costs)            # num of houses we have
        dp = [[-1] * 4 for _ in range(n)]

        def calc_cost(h, last):
            if dp[h][last] != -1:
                return dp[h][last]

            if h == 0:
                min_cost = math.inf
                for i in range(3):
                    if i != last:
                        min_cost = min(min_cost, costs[0][i])
                        dp[h][last] = min_cost
                return dp[h][last]

            min_cost = math.inf
            for i in range(3):
                if i != last:
                    cost = costs[h][i] + calc_cost(h-1, i)           # recurse to prev house and last = i
                    min_cost = min(min_cost, cost)
                    dp[h][last] = min_cost    
            return dp[h][last]

        return calc_cost(n-1, 3)
