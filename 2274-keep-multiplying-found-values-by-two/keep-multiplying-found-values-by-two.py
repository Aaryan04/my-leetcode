class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == original:
                original = 2 * original
                i = 0
                continue
            
            i += 1

        return original