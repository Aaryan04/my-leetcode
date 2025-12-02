class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.events:
            self.events.append([startTime, endTime])
            return True
        else:
            # binary search to find the insertion point
            i = bisect.bisect_left(self.events, [startTime, endTime])
            
            if i < len(self.events) and endTime > self.events[i][0]:
                return False

            if i > 0 and self.events[i-1][1] > startTime:
                return False
            

            
            self.events.insert(i, [startTime, endTime])
            return True



# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)