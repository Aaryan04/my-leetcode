from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        n = len(nums)

        # dp[i][t] = can we form sum t using elements 0...i
        dp = [[False] * (target + 1) for _ in range(n)]

        # base case : sum 0 is always possible (take no elements)
        for i in range(n):
            dp[i][0] = True
        
        # base case for the first element
        if nums[0] <= target:
            dp[0][nums[0]] = True
        
        # fill the table
        for i in range(1, n):
            for t in range(1, target + 1):
                not_take = dp[i-1][t]
                take = False
                if t >= nums[i]:
                    take = dp[i-1][t-nums[i]]

                dp[i][t] = take or not_take

        return dp[n-1][target]



        
        # RECURSION + MEMOIZATION
        # dp[i][t] = -1 (uncomputed), 0 (False), 1 (True)
        # dp = [[-1] * (target + 1) for _ in range(n)]

        # def is_target_exist(i: int, t: int) -> bool:
        #     # base cases
        #     if t == 0:
        #         return True
        #     if i == 0:
        #         return nums[0] == t

        #     if dp[i][t] != -1:
        #         return dp[i][t] == 1

        #     # not take current element
        #     not_take = is_target_exist(i - 1, t)

        #     # take current element (if possible)
        #     take = False
        #     if t >= nums[i]:
        #         take = is_target_exist(i - 1, t - nums[i])

        #     ans = take or not_take
        #     dp[i][t] = 1 if ans else 0
        #     return ans

        # return is_target_exist(n - 1, target)
