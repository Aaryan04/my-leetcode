class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        last_rain_on = defaultdict(int)
        zero_idx = []
        ans = [1]*len(rains)

        for i, lake in enumerate(rains):
            if lake > 0:                   # raining on the lake
                if lake in last_rain_on:       # if already full, we need to dry it before today
                    # find earliest dry day after full[lake]
                    idx = bisect.bisect_right(zero_idx, last_rain_on[lake])
                    if idx == len(zero_idx):        # no dry day possible
                        return []
                    dry_day = zero_idx.pop(idx)     # use that day
                    ans[dry_day] = lake             # and update that dry day in the ans

                # make this lake as now filled (rained today)
                last_rain_on[lake] = i
                ans[i] = -1
                
            else:                           # found 0
                zero_idx.append(i)
                ans[i] = 1                  # placeholder for now (may change later)
        return ans