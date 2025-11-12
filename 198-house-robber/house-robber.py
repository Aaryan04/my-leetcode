class Solution:
    def rob(self, nums: List[int]) -> int:
        # DP with Tabulation (space optimized)
        prev2, prev1 = 0, 0
        for num in nums:
            curr = max(num + prev2, prev1)
            prev2 = prev1
            prev1 = curr
        return prev1
        # TC = O(N)
        # SC = O(1)

        # DP with Tabulation (iterative)
        # n = len(nums)
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return nums[0]

        # dp = [0]*n
        # dp[0] = nums[0]         # max to reach index 0 
        # dp[1] = max(nums[0], nums[1])       # max to reach index 1, and similarly we have to find max to reach last index

        # for i in range(2,n):
        #     dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        # return dp[-1]
        # TC => O(N)
        # SC => O(N)
        
        
        
        
        # Recursion with memoization
        # memo = {}
        # def helper(i):
        #     if i == 0:
        #         return nums[0]
                
        #     if i < 0:
        #         return 0

        #     if i in memo:
        #         return memo[i]

        #     rob = nums[i] + helper(i-2)
        #     skip = helper(i-1)

        #     memo[i] = max(rob, skip)
        #     return memo[i]

        # return helper(len(nums)-1)

        # TC - O(N)
        # SC - O(N) + O(N)