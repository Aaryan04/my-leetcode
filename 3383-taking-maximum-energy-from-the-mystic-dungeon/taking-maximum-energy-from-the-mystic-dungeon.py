class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        # dp[i] = maximum energy you can collect starting from index i
        # f(i) = energy[i] + f(i + k) if i + k < n
        # f(i) = energy[i] otherwise
        # ans will max( f(i) ) for all i in [0, n-1]
        
        # def dfs(i):
        #     if i >= n:          # base case
        #         return 0
        #     if i in memo:
        #         return memo[i]
        #     # take energy[i] and jump
        #     next_energy = dfs(i+k) if i + k < n else 0
        #     memo[i] = energy[i] + next_energy
        #     return memo[i]
        
        # n = len(energy)
        # memo = {}
        # ans = -math.inf
        # for i in range(n):
        #     ans = max(ans, dfs(i))
        # return ans


        n = len(energy)
        ans = -math.inf

        for i in range(n-k, n):
            total = 0
            j = i
            while j >= 0:
                total += energy[j]
                j = j-k
                ans = max(ans, total)

        return ans

        # THIS RUNS FASTER!