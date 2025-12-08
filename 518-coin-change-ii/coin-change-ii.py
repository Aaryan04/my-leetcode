class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        t = amount
        n = len(coins)
        dp = [[-1] * (t+1) for _ in range(n)]

        def f(i, t):
            if i == 0:
                return 1 if (t % coins[0] == 0) else 0 
            if dp[i][t] != -1:
                return dp[i][t]

            not_take = f(i-1, t)
            take = 0
            if coins[i] <= t:
                take = f(i, t-coins[i])        # we dont move back the i because we can reuse the same coin again
            
            dp[i][t] = not_take + take
            
            return dp[i][t]
        
        return f(n-1, t)
                