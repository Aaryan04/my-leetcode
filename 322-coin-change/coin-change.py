class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # MEMOIZATION SOLUTION
        t = amount
        n = len(coins)
        dp = [[-1] * (t+1) for _ in range(n)]

        def f(i, t):
            if i == 0:
                return t // coins[i] if (t % coins[0] == 0) else math.inf 
            if dp[i][t] != -1:
                return dp[i][t]

            not_take = 0 + f(i-1, t)
            take = math.inf
            if coins[i] <= t:
                take = 1 + f(i, t-coins[i])        # we dont move back the i because we can reuse the same coin again
            
            dp[i][t] = min(not_take, take)
            
            return dp[i][t]
        
        ans = f(n-1, t)
        if ans == math.inf:
            return -1
        return int(ans)