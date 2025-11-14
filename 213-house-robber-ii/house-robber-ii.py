class Solution:
    def helper(self, nums: List[int]) -> int:
        # DP with Tabulation (space optimized)
        prev2, prev1 = 0, 0
        for num in nums:
            curr = max(num + prev2, prev1)
            prev2 = prev1
            prev1 = curr
        return prev1

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]   # handle single house
        ans = max(self.helper(nums[:-1]), self.helper(nums[1:]))
        return ans
