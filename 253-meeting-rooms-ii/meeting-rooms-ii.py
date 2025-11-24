class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x: x[0])
        free = []               # min heap (store end times of each meeting)
        heapq.heappush(free, intervals[0][1])

        for interval in intervals[1:]:
            if free[0] <= interval[0]:  # prev meeting end before new meeting start
                heapq.heappop(free)     # new meeting can start in the same room so pop prev meeting end time
            
            # if same room is continued, then we need to push the updated times
            # if new room is needed then we need to push that as well
            heapq.heappush(free, interval[1])

        return len(free)        