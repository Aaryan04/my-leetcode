class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        num1 = 0 
        g = 0

        # --- Phase 1: Pre-calculation ---
        # Iterate through the array to:
        # 1. Count how many 1s already exist.
        # 2. Calculate the GCD of the entire array.
        for x in nums:
            if x == 1:
                num1 += 1
            g = gcd(g, x)

        # --- Phase 2: Handle Existing 1s ---
        # If there are any 1s, we can use them to convert adjacent non-1 numbers.
        # Cost = Total elements (n) - Elements that are already 1 (num1).
        if num1 > 0:
            return n - num1
            
        # --- Phase 3: Check for Impossibility ---
        # If the GCD of the entire array is > 1, it is impossible to generate a 1 
        # because every operation will result in a multiple of that GCD.
        if g > 1:
            return -1

        # --- Phase 4: Create the First 1 ---
        # We don't have a 1, so we need to find the shortest subarray 
        # that can be combined to form a 1.
        min_len = n + 1  # Initialize with a value larger than any possible length
        
        for i in range(n):
            g = 0 
            for j in range(i, n):
                g = gcd(g, nums[j])
                
                # If we find a subarray with GCD 1, record its length.
                if g == 1:
                    min_len = min(min_len, j - i + 1)
                    break # Optimization: A longer subarray starting at 'i' isn't useful.
        
        # --- Final Calculation ---
        # 1. Operations to create the first 1: (min_len - 1)
        # 2. Operations to convert the rest of the array using that 1: (n - 1)
        # Total = (min_len - 1) + (n - 1) = min_len + n - 2
        return min_len + n - 2