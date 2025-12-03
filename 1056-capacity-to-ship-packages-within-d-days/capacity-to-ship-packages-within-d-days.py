class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # ship must have minimum capacity of max(weights) to carry atleast 1 package in one day (packages cannot be split)
        # and max capacity of the ship can be sum(weights)
        # Can implement binary search here [max(weights), sum(weights)]
        # we need to find optimal capacity of ship which helps us ship all the packages in d days

        def daysNeeded(capacity):
            days = 1
            total = 0

            for w in weights:
                total += w
                if total > mid:
                    days += 1
                    total = w
            return days

        l = max(weights)
        r = sum(weights)

        res = r         # will start our res as worst case scenario
        
        while l <= r:
            mid = (l+r) // 2

            if daysNeeded(mid) <= days:          # we are quick so check left
                res = mid
                r = mid - 1
            else:
                l = mid + 1
            
        return res
            



            


