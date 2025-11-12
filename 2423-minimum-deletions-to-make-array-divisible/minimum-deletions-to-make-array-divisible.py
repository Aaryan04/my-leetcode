class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        
        def gcd(a,b):
            while b > 0:
                a,b = b, a%b
            return a 

        # Find GCD of all numbers in numsDivide
        total_gcd = reduce(gcd, numsDivide)
        
        # Sort nums for easy traversal
        nums.sort()
        
        # Find the first number in nums that divides total_gcd
        for i, num in enumerate(nums):
            if total_gcd % num == 0:
                return i  # i elements before this need to be removed
        return -1