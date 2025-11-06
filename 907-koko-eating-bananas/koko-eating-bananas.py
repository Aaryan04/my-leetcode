class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search range: minimum eating speed is 1, maximum is the largest pile
        # treat the problem as [1,2,3,4,5,6,7,8,9,10,11]
        l, r = 1, max(piles)
        # Initialize result with the upper bound (worst-case speed)
        res = r

        # Binary search to find the minimum valid eating speed
        while l <= r:
            # Try the middle speed
            k = (l + r) // 2        # 6
            hours = 0

            # Calculate total hours needed if eating at speed k
            for p in piles:
                # Use ceiling to count partial hours as full ones
                hours += math.ceil(p / k)

            # If the total hours is within the allowed time i.e we are eating fast, need to slow down
            if hours <= h:
                # Try to minimize the eating speed
                res = min(res, k)       # update the res - 6 
                r = k - 1  # Search in the lower half
            else:
                # Too slow, need to increase speed
                l = k + 1  # Search in the upper half

        # Return the minimum valid eating speed
        return res