class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # ship must have minimum capacity of max(weights) to carry atleast 1 package in one day (packages cannot be split)
        # and max capacity of the ship can be sum(weights)
        # Can implement binary search here [max(weights), sum(weights)]
        # we need to find optimal capacity of ship which helps us ship all the packages in d days

        def daysNeeded(capacity):
            days = 1
            curr_load = 0

            for w in weights:
                if curr_load + w > capacity:        # if curr_load increases more than capacity then increase the days
                    days += 1
                    curr_load = w           # start new day with this load in the iteration
                else:
                    curr_load += w          # else keep adding to curr_load
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
            



            


